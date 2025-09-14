import dspy
import os
import random
import json
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
lm = dspy.LM(
    "openrouter/meta-llama/llama-4-scout",
    api_key=OPENROUTER_API_KEY,
    cache=False,
    provider="groq"
)
if not hasattr(dspy.settings, "lm") or dspy.settings.lm is None:
    dspy.configure(lm=lm)

import time
import pandas as pd
import random
import json
from utils import (
    plot_prediction_distributions,
    get_summary_metrics,
    plot_stacked_priority_topics,
    plot_heatmap_topics_sentiment,
)
from classification import optimized_agent
from rag_agent import load_rag_agent
from embeddings import load_embedder

st.set_page_config(page_title="Atlan Customer Support Copilot", layout="wide")

# ------------------- INIT SESSION STATE -------------------
# Use our own key to track page so buttons can update it
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# ------------------- SIDEBAR NAVIGATION -------------------
st.sidebar.title("Navigation")
choice = st.sidebar.radio(
    "Go to:",
    ["Home", "Bulk Classification", "Interactive Agent"],
    index=["Home", "Bulk Classification", "Interactive Agent"].index(
        st.session_state.current_page
    ),
    key="sidebar_radio",  # a different key than our state variable
)

# keep the session value in sync with sidebar selection
st.session_state.current_page = choice
page = st.session_state.current_page

# ------------------- HOME -------------------
if page == "Home":
    col_logo, col_text = st.columns([1, 2], vertical_alignment="center")
    with col_logo:
        st.image("data/atlan_logo.png", use_container_width=True)
    with col_text:
        st.title("Atlan Customer Support Copilot")
        st.markdown(
            """
            <style>
            .big-tagline {font-size: 1.2rem; line-height: 1.6;}
            </style>
            <p class="big-tagline">
            🚀 <b>Your AI-powered sidekick</b> for fast, accurate customer-ticket classification and instant responses.
            </p>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.subheader("✨ What We Can Do")
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown("### 📊 Bulk Classification")
        st.caption("Upload or process all your support tickets and view rich analytics.")
    with f2:
        st.markdown("### 🤖 Interactive AI Agent")
        st.caption("Chat directly with the AI to classify and draft responses in real time.")
    with f3:
        st.markdown("### 🔍 Insights & Trends")
        st.caption("Explore sentiments, priorities, and topic distributions for insights.")

    st.divider()

    # ✅ Buttons that navigate by updating our own session key
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 Go to Bulk Classification", use_container_width=True):
            st.session_state.current_page = "Bulk Classification"
            st.rerun()
    with c2:
        if st.button("💬 Try the Interactive Agent", use_container_width=True):
            st.session_state.current_page = "Interactive Agent"
            st.rerun()

    st.markdown(
        """
        <hr>
        <center>
        <small>Built with ❤️ using Streamlit and Atlan’s AI stack</small>
        </center>
        """,
        unsafe_allow_html=True,
    )




# ------------------- BULK CLASSIFICATION -------------------
elif page == "Bulk Classification":
    st.title("Bulk Ticket Classification Dashboard")
    default_json_path = "data/sample_tickets.json"

    if "json_path" not in st.session_state:
        st.session_state.json_path = default_json_path

    if "bulk_results" not in st.session_state:
        st.session_state.bulk_results = None
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    # --- File uploader ---
    uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])
    if uploaded_file is not None:
        save_path = os.path.join("data", uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state.json_path = save_path
        st.success(f"Uploaded file saved as `{save_path}`")

    def run_classification(sample_size=None):
        """Run classification on tickets whether or not they
        already contain a `classification` field."""
        with open(st.session_state.json_path, "r") as f:
            data = json.load(f)

        if sample_size:
            data = random.sample(data, min(sample_size, len(data)))

        results = []
        ticket_placeholder = st.empty()

        for item in data:
            # required basic keys
            if not all(k in item for k in ("id", "subject", "body")):
                continue

            id_ = item["id"]
            subject = item["subject"]
            body = item["body"]

            # if classification exists, treat as ground truth
            gt_class = item.get("classification")

            try:
                # always predict so we have comparable results
                pred = optimized_agent(id=id_, subject=subject, body=body).parsed_document
                results.append({
                    "id": id_,
                    "subject": subject,
                    "body": body,
                    "ground_truth": gt_class,  # may be None
                    "prediction": {
                        "topics": getattr(pred, "topics", []),
                        "sentiment": getattr(pred, "sentiment", ""),
                        "priority": getattr(pred, "priority", "")
                    }
                })
                ticket_placeholder.markdown(f"**Processing Ticket:** {id_} – {subject}")
                time.sleep(0.2)
            except Exception as e:
                st.warning(f"Skipping {id_}: {e}")
                continue

        ticket_placeholder.empty()
        return results

    # --- UI buttons remain the same ---
    col1, col2 = st.columns(2)
    if col1.button("Start Bulk Classification"):
        st.write("Running classification... please wait ⏳")
        st.session_state.bulk_results = run_classification()
        st.success("Classification completed ✅")

    if col2.button("Classify Random 5 Tickets"):
        st.write("Running classification on 5 random tickets... please wait ⏳")
        st.session_state.bulk_results = run_classification(sample_size=5)
        st.success("Random classification completed ✅")

    results = st.session_state.bulk_results
    # ▼▼ remainder of filtering / metrics / plots code stays unchanged ▼▼


    if results:
        # ---------- FILTERING ----------
        st.subheader("Filter Tickets")
        all_topics = sorted({t for r in results for t in r["prediction"]["topics"] if t})
        all_sentiments = sorted({r["prediction"]["sentiment"] for r in results if r["prediction"]["sentiment"]})
        all_priorities = sorted({r["prediction"]["priority"] for r in results if r["prediction"]["priority"]})

        selected_topics = st.multiselect("Topics", all_topics)
        selected_sentiments = st.multiselect("Sentiment", all_sentiments)
        selected_priorities = st.multiselect("Priority", all_priorities)

        df = pd.DataFrame([{
            "id": r["id"],
            "subject": r["subject"],
            "body": r["body"],
            "topics": r["prediction"]["topics"],
            "sentiment": r["prediction"]["sentiment"],
            "priority": r["prediction"]["priority"]
        } for r in results])

        mask = pd.Series(True, index=df.index)
        if selected_topics:
            mask &= df["topics"].apply(lambda x: any(t in x for t in selected_topics))
        if selected_sentiments:
            mask &= df["sentiment"].isin(selected_sentiments)
        if selected_priorities:
            mask &= df["priority"].isin(selected_priorities)

        filtered = df[mask].to_dict("records")

        if st.session_state.current_index >= len(filtered):
            st.session_state.current_index = 0

        # ---------- SUMMARY METRICS ----------
        st.subheader("Summary Metrics")
        if filtered:
            metrics = get_summary_metrics(filtered)
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Total Tickets", metrics.get("total", 0))
            c2.metric("Unique Topics", metrics.get("unique_topics", 0))
            c3.metric("Unique Sentiments", metrics.get("unique_sentiments", 0))
            c4.metric("Unique Priorities", metrics.get("unique_priorities", 0))
        else:
            st.info("No tickets available for summary.")

        # ---------- RESULTS WITH NAVIGATION ----------
        st.subheader("Classification Results")
        if filtered:
            current_ticket = filtered[st.session_state.current_index]
            with st.container():
                col_a, col_b = st.columns([7, 3])
                with col_a:
                    st.markdown(f"**ID:** {current_ticket['id']}")
                    st.markdown(f"**Subject:** {current_ticket['subject']}")
                    st.markdown(f"**Body:** {current_ticket['body']}")
                with col_b:
                    st.markdown("**Classification Result**")
                    st.markdown(f"- **Topics:** {', '.join(current_ticket['topics']) if current_ticket['topics'] else 'N/A'}")
                    st.markdown(f"- **Sentiment:** {current_ticket['sentiment'] or 'N/A'}")
                    st.markdown(f"- **Priority:** {current_ticket['priority'] or 'N/A'}")

            cprev, cnext = st.columns([1, 1])
            if cprev.button("⬅️ Previous") and st.session_state.current_index > 0:
                st.session_state.current_index -= 1
            if cnext.button("Next ➡️") and st.session_state.current_index < len(filtered) - 1:
                st.session_state.current_index += 1
        else:
            st.warning("No tickets match the selected filters.")

        # ---------- ANALYTICS & PLOTS ----------
        st.subheader("Classification Analytics")
        if filtered:
            if any(r["topics"] for r in filtered):
                st.markdown("### Distributions")
                plot_prediction_distributions(filtered)

                st.markdown("### Topics vs Priority (Stacked Bar)")
                plot_stacked_priority_topics(filtered)

                st.markdown("### Topics vs Sentiment (Heatmap)")
                plot_heatmap_topics_sentiment(filtered)
            else:
                st.info("Not enough data to generate analytics.")
        else:
            st.info("No data available for analytics.")

    else:
        st.info("Click one of the buttons above to start classification.")

# ------------------- INTERACTIVE AGENT -------------------
elif page == "Interactive Agent":
    st.title("💬 Interactive AI Agent")
    st.markdown(
        "Provide your ticket details below and let the Copilot classify, analyze, "
        "and draft an appropriate response."
    )
    st.divider()

    # Two-column layout for input and output
    input_col, output_col = st.columns([1, 1])

    with input_col:
        st.subheader("📝 Ticket Details")
        user_subject = st.text_input("Subject", placeholder="e.g. Unable to connect to API")
        user_body = st.text_area(
            "Body",
            placeholder="Describe your issue in detail...",
            height=200,
        )

        run_btn = st.button("🚀 Analyze & Respond", type="primary", use_container_width=True)

    with output_col:
        st.subheader("🔎 Analysis & Response")

        if run_btn:
            with st.spinner("Analyzing ticket..."):
                pred = optimized_agent(id="NEW", subject=user_subject, body=user_body).parsed_document

            # ---- Internal Analysis ----
            with st.expander("Internal Analysis", expanded=True):
                def chip(label, color):
                    return f"<span style='background:{color};padding:3px 8px;border-radius:12px;color:white;font-size:0.85em'>{label}</span>"

                topics = ", ".join(pred.topics) if pred.topics else "N/A"
                sentiment = pred.sentiment or "N/A"
                priority = pred.priority or "N/A"

                st.markdown(
                    f"**Topics:** {', '.join([chip(t, '#4B8BF4') for t in pred.topics]) if pred.topics else chip('N/A', '#999999')}",
                    unsafe_allow_html=True,
                )
                st.markdown(f"**Sentiment:** {chip(sentiment, '#E57C23')}", unsafe_allow_html=True)
                st.markdown(f"**Priority:** {chip(priority, '#A23E48')}", unsafe_allow_html=True)

            # ---- Final Response ----
            rag_topics = {"How-to", "Product", "Best practices", "API/SDK", "SSO"}
            if any(t in rag_topics for t in pred.topics):
                with st.spinner("Generating detailed response..."):
                    embed_model = load_embedder("BAAI/bge-large-en-v1.5")
                    rag_agent = load_rag_agent(embed_model)
                    rag_response = rag_agent(user_body)

                with st.expander("AI-Generated Response", expanded=True):
                    st.markdown(rag_response["answer"])
                    st.caption(f"**Sources:** {', '.join(rag_response['sources'])}")
            else:
                with st.expander("AI-Generated Response", expanded=True):
                    st.markdown(
                        f"This ticket is classified as **{topics}** "
                        "and routed to the appropriate team."
                    )

            st.success(
                f"✅ Ticket categorized and response prepared for topics: {topics}",
                icon="📨",
            )
        else:
            st.info("Enter ticket details on the left and click **Analyze & Respond** to see results.")

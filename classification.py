import dspy
from dspy_essentials.models import classification
from dspy_essentials.optimization_examples import examples
import os





class complaint_classification(dspy.Signature):
    """
    Given inputs: id, subject, and body of a complaint message,
    classify topics, sentiment, and priority with strict adherence to schema.

    TOPIC CLASSIFICATION:
    please be very strict about the topics you choose. and make sure you are smartly picking the best topics
    - Choose 1 to 3 topics strictly from the following fixed list:
        ["How-to", "Product", "Connector", "Lineage", "API/SDK", "SSO", "Glossary", "Best practices", "Sensitive data"]
    - Do NOT invent or substitute synonyms.
    - Words like "webhook" or "lambda" are NOT topics; assign to closest valid topic such as "Product" or "API/SDK".
    - Always assign "Sensitive data" if complaint mentions PII, GDPR, security, or privacy concerns.

    SENTIMENT CLASSIFICATION (choose exactly one):

    - Curious: Exploratory, asking questions, seeking understanding.
      Example: "How do I configure the new API?"
    - Frustrated: Experiencing issues, dissatisfied but polite tone. Strong negative tone, urgency, or emotional intensity.
      Example: "The connector is failing repeatedly and slowing us down."
      Example: "This system failure is unacceptable and must be fixed immediately!"
    - Neutral: Factual, no clear emotional tone.
      Example: "Please provide the latest audit logs."

    PRIORITY CLASSIFICATION (choose exactly one):

    - P0: Blocking, urgent issues causing system failures, major business impact.
      Example: "Our entire team is blocked, cannot proceed with critical project."
    - P1: Important issues or time-sensitive requests that are not blocking.
      Example: "Need assistance configuring a connector to meet upcoming deadlines."
    - P2: General questions, informational requests, low urgency.
      Example: "Can you share best practices for catalog hygiene?"

    DECISION RULES:

    - If complaint explicitly states blocks, downtime, critical failure → P0.
    - If complaint expresses concern or requests help with moderate urgency → P1.
    - Informational or exploratory queries → P2.
    - For sentiment, carefully analyze tone and language cues in subject and body.
    - For topics, prefer the 1-3 most relevant based on technical content, never more.

    The ID must exactly match the input ID.

    --- Few-shot examples: ---

    Example 1:
    ID: TICKET-245
    Subject: "Connecting Snowflake to Atlan - permissions?"
    Body: "Connection failing with service account. Entire BI team blocked for major project. Need definitive permissions."
    Topics: ["How-to", "Connector"]
    Sentiment: Frustrated
    Priority: P0

    Example 2:
    ID: TICKET-246
    Subject: "Which connectors capture lineage automatically?"
    Body: "Trying to understand lineage for Fivetran, dbt, Tableau. Need clear explanation for leadership."
    Topics: ["Connector", "Lineage"]
    Sentiment: Curious
    Priority: P1

    Example 3:
    ID: TICKET-253
    Subject: "Upstream lineage missing, view untrustworthy"
    Body: "Critical Snowflake view missing upstream lineage after multiple re-crawls. This is infuriating and a huge problem."
    Topics: ["Lineage", "Connector"]
    Sentiment: Angry
    Priority: P0

    Example 4:
    ID: TICKET-259
    Subject: "How does Atlan surface sensitive fields like PII?"
    Body: "Security team wants to know how Atlan identifies PII and applies tags or masking."
    Topics: ["How-to", "Sensitive data"]
    Sentiment: Curious
    Priority: P1

    Example 5:
    ID: TICKET-270
    Subject: "Connector failed - where to check logs?"
    Body: "Nightly Snowflake crawler failed, reports missing lineage. Need error logs ASAP."
    Topics: ["Connector"]
    Sentiment: Frustrated
    Priority: P0
    
    {
    "id": "TICKET-256",
    "subject": "Mapping Active Directory groups to Atlan teams",
    "body": "Our company policy requires us to manage all user access through Active Directory groups. We need to map our existing AD groups (e.g., 'data-analyst-finance', 'data-engineer-core') to teams within Atlan to automatically grant the correct permissions. I can't find the settings for this. How is this configured?",
    "classification": {
      "topics": ["How-to", "SSO"],
      "sentiment": "Frustrated",
      "priority": "P1"
    }
  },
  {
    "id": "TICKET-257",
    "subject": "RBAC for assets vs. glossaries",
    "body": "I need clarification on how Atlan's role-based access control works. If a user is denied access to a specific Snowflake schema, can they still see the glossary terms that are linked to the tables in that schema? I need to ensure our PII governance is airtight.",
    "classification": {
      "topics": ["Product", "Glossary", "Sensitive data"],
      "sentiment": "Curious",
      "priority": "P1"
    }
  },
  {
    "id": "TICKET-258",
    "subject": "Process for onboarding asset owners",
    "body": "We've started identifying owners for our key data assets. What is the recommended workflow in Atlan to assign these owners and automatically notify them? We want to make sure they are aware of their responsibilities without us having to send manual emails for every assignment.",
    "classification": {
      "topics": ["How-to", "Best practices"],
      "sentiment": "Curious",
      "priority": "P2"
    }
  },
  {
    "id": "TICKET-259",
    "subject": "How does Atlan surface sensitive fields like PII?",
    "body": "Our security team is evaluating Atlan and their main question is around PII and sensitive data. How does Atlan automatically identify fields containing PII? What are our options to apply tags or masks to these fields once they are identified to prevent unauthorized access?",
    "classification": {
      "topics": ["How-to", "Sensitive data"],
      "sentiment": "Curious",
      "priority": "P1"
    }
  },
  
  above are some messages you should pay special attention to
  
  {
    """

    id: str = dspy.InputField(desc="ID of the complaint message")
    subject: str = dspy.InputField(desc="Subject of the complaint raised")
    body: str = dspy.InputField(desc="Main body of the complaint message")

    parsed_document: classification = dspy.OutputField(
        desc="Extracted topics, sentiment, and priority"
    )
    
    

class complaint_classification_agent(dspy.Module):
    """agent to classify and extract topics, sentiment and priority from the complaint message"""

    def __init__(self):
        super().__init__()
        self.classifier = dspy.Predict(complaint_classification)

    def forward(self, id: str, subject: str, body: str) -> complaint_classification:
        result = self.classifier(id=id, subject=subject, body=body)
        result.id = id  # Force output id to match input id
        return result
    
    
ext_agent = complaint_classification_agent()
optimizer = dspy.LabeledFewShot(k=40)
optimized_agent = optimizer.compile(ext_agent, trainset=examples)



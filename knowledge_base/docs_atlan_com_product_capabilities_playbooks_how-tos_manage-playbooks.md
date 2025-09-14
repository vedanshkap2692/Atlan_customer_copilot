# Manage playbooks
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/manage-playbooks)

PlaybooksGet StartedManagementManage playbooksAutomate data profilingTroubleshooting

Get Started

ManagementManage playbooksAutomate data profiling

Manage playbooks

Automate data profiling

Troubleshooting

Configure Atlan

Playbooks

Management

Manage playbooks

Once you'vecreated a playbook, you can monitor, modify, or delete it at any time. You can alsoenable notificationsto monitor your playbook runs directly in Slack or Microsoft Teams.



## Monitor a playbookâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/manage-playbooks)

To monitor your playbooks runs:

When running a playbook immediately, you will be redirected to the monitoring page within 5 seconds.

At any other moment:From the left menu of any screen in Atlan, clickGovernance.Under theGovernanceheading of theGovernance center, clickPlaybooks.In the playbooks manager, selectthe playbookyou'd like to view.In theOverviewsection of your playbook, you'll be able to monitor:A summary of the rules, actions, and updated assets.An activity log for recent runs and updates over time.

From the left menu of any screen in Atlan, clickGovernance.

Under theGovernanceheading of theGovernance center, clickPlaybooks.

In the playbooks manager, selectthe playbookyou'd like to view.

In theOverviewsection of your playbook, you'll be able to monitor:A summary of the rules, actions, and updated assets.An activity log for recent runs and updates over time.

A summary of the rules, actions, and updated assets.

An activity log for recent runs and updates over time.

The activity log in the playbooks manager can help you keep track of playbook runs, ranging from 24 hours to 30 days. Select any of the entries to navigate to the corresponding playbook.



## Modify a playbookâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/manage-playbooks)

To modify an existing playbook:

From the left menu of any screen in Atlan, clickGovernance.

Under theGovernanceheading of theGovernance center, clickPlaybooks.

In the playbooks manager, click the playbook you'd like to modify.

On your playbook page:To edit the name and description of your playbook, hover over your playbook and clickEdit.To modify the rules of your playbook, clickRulesto make your changes and then clickUpdateto save them.(Optional) To add a new rule to an existing playbook, in the left menu for playbook rules, click+ Add new Rule.ÂTo turn off a playbook filter, to the right of any filter, click the three horizontal dots and then clickDisable. ClickEnableto turn on any disabled filters.To modify the schedule for your playbook, in the upper right of your screen:ClickRun Nowto run it immediately.Click thepencil iconto modify or remove the schedule.

To edit the name and description of your playbook, hover over your playbook and clickEdit.

To modify the rules of your playbook, clickRulesto make your changes and then clickUpdateto save them.(Optional) To add a new rule to an existing playbook, in the left menu for playbook rules, click+ Add new Rule.Â

(Optional) To add a new rule to an existing playbook, in the left menu for playbook rules, click+ Add new Rule.Â

To turn off a playbook filter, to the right of any filter, click the three horizontal dots and then clickDisable. ClickEnableto turn on any disabled filters.

To modify the schedule for your playbook, in the upper right of your screen:ClickRun Nowto run it immediately.Click thepencil iconto modify or remove the schedule.

ClickRun Nowto run it immediately.

Click thepencil iconto modify or remove the schedule.



## Delete a playbookâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/manage-playbooks)

To delete an existing playbook:

From the left menu of any screen in Atlan, clickGovernance.

Under theGovernanceheading of theGovernance center, clickPlaybooks.

In the playbooks manager, hover over the playbook you'd like to delete and clickDelete Playbook.

ClickDeleteto confirm.



## Enable playbook notificationsâ
(source: https://docs.atlan.com/product/capabilities/playbooks/how-tos/manage-playbooks)

You can set up Slack or Microsoft Teams alerts for your playbook runs in Atlan. This can help you monitor your playbooks directly in Slack or Microsoft Teams. You can also choose to receive alerts for failed playbook runs only.

Before you can enable notifications for playbooks, you will need to either:

Integrate Slack and Atlan

Integrate Microsoft Teams and Atlan

To enable notifications for playbook runs:

From the left menu of any screen in Atlan, clickGovernance.

Under theGovernanceheading of theGovernance center, clickPlaybooks.

In the upper-right of the playbooks manager, underActivity, click the bell icon.

In theEnable notificationspopup:ClickSetup nowto integrateSlackorMicrosoft Teams.If you have already integrated Slack or Microsoft Teams, clickEnable.

ClickSetup nowto integrateSlackorMicrosoft Teams.

If you have already integrated Slack or Microsoft Teams, clickEnable.

In the notifications setup dialog, configure the following:ForNotifications channel, you can either:If you have already configured aSlackorMicrosoft Teamschannel to receive workflow alerts, that channel will be preselected. You can use the same channel to receive both workflow and playbook run alerts and skip to the next step.If you have not configured a workflow alerts channel or want to add a different one, enter the channel name to receive notifications for playbook runs. This channel will be displayed as thePlaybooks alert channelÂ in yourÂSlackorMicrosoft Teamsintegration.To select the type of notifications you want to receive, you can either:ClickBoth success and failure alertsto receive notifications for both successful and failed playbook runs.ClickFailure alerts onlyto limit notifications to failed playbook runs only.ClickSaveto save your notification preferences.

ForNotifications channel, you can either:If you have already configured aSlackorMicrosoft Teamschannel to receive workflow alerts, that channel will be preselected. You can use the same channel to receive both workflow and playbook run alerts and skip to the next step.If you have not configured a workflow alerts channel or want to add a different one, enter the channel name to receive notifications for playbook runs. This channel will be displayed as thePlaybooks alert channelÂ in yourÂSlackorMicrosoft Teamsintegration.

If you have already configured aSlackorMicrosoft Teamschannel to receive workflow alerts, that channel will be preselected. You can use the same channel to receive both workflow and playbook run alerts and skip to the next step.

If you have not configured a workflow alerts channel or want to add a different one, enter the channel name to receive notifications for playbook runs. This channel will be displayed as thePlaybooks alert channelÂ in yourÂSlackorMicrosoft Teamsintegration.

To select the type of notifications you want to receive, you can either:ClickBoth success and failure alertsto receive notifications for both successful and failed playbook runs.ClickFailure alerts onlyto limit notifications to failed playbook runs only.

ClickBoth success and failure alertsto receive notifications for both successful and failed playbook runs.

ClickFailure alerts onlyto limit notifications to failed playbook runs only.

ClickSaveto save your notification preferences.

(Optional) To disable notifications, from the notifications setup dialog, remove the playbook alerts channel configured forSlackorMicrosoft Teams.

You will now receiveSlackorMicrosoft Teamsnotifications for all your playbook runs in Atlan! ð

The Atlan bot will share playbook run alerts, including details like run status, start time, run time, trigger type, last three runs, and more.

atlan

documentation

Monitor a playbook

Modify a playbook

Delete a playbook

Enable playbook notifications

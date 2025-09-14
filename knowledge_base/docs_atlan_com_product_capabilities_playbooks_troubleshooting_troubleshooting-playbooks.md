# Troubleshooting playbooks
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

PlaybooksGet StartedManagementTroubleshootingTroubleshooting playbooks

Get Started

Management

TroubleshootingTroubleshooting playbooks

Troubleshooting playbooks

Configure Atlan

Playbooks

Troubleshooting

Troubleshooting playbooks

ð¤ Who can do this?You will need to be an admin user in Atlan to create playbooks.

Here are a few things to know aboutsetting up playbooks:



#### What are the known limitations of the domain action?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

Following are the known issues or limitations when using thedomain action:

Atlan currently does not support adding glossaries, categories, and terms to domains.

If you do not have read permission on the assets you want to add to a domain, those assets will be removed from the playbook workflow during processing.Â

If you do not have update permission on the assets you want to add to a domain, the playbook workflow will fail. However, some assets may still be linked to the domain before the failure occurs.



#### What type of infrastructure costs can I expect to incur?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

Atlan uses Elasticsearch to run playbooks, so expect infrastructure costs to be minimal and not a determining factor for utilizing playbooks.



#### What is the maximum number of playbooks that can be run?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

We recommend building no more than a maximum of 20 rules per playbook. However, the total number of playbooks that can be run is still to be determined. From a technical standpoint, playbooks leverage the workflow infrastructure, which means there are no hard limits. Depending on the number of playbooks that need to be run, the infrastructure will have to be scaled accordingly.Â



#### Do I also need to have update permissions for playbooks?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

Yes. You need to have the permission to update assets in Atlan in order to run playbooks for updating them.Â If you do not have the permission to update an asset, you will be unable to update it using playbooks.

Additionally, Atlan uses the permissions of the playbook creator in determining the assets to be updated and not that of the user who runs the playbook. Your user permissions are used to determine the bulk updates you can make to ensure that there is no adverse impact on assets beyond your scope of access.



#### Can I automate requests for updates through playbooks?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

No, Atlan currently does not support automating asset updaterequeststhrough playbooks.



#### Is there a way to undo updates made through playbooks?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

Currently, there is no button to undo asset updates. However, you canmodify your existing playbooks. You can either turn off the filters or add new rules to reverse the updates.



#### Is there a way to view or download a report of updated assets from previous playbook runs?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

Currently, no. You canmonitor your existing playbooksto view a high-level summary of asset updates from previous playbook runs. Observability of results is on the roadmap.



#### Can I get email notifications for playbook run successes or failures?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

Currently, no. However, you canset up Slack or Microsoft Teams alertsfor your playbook runs in Atlan.



#### How to handle anoffload node status is not supportederror?â
(source: https://docs.atlan.com/product/capabilities/playbooks/troubleshooting/troubleshooting-playbooks)

If you encounter anoffload node status is not supportederror message, the playbook workflow may have exceededÂ the EtcD size limit. Playbooks use Argo workflow templates, which are stored as Kubernetes resources. This creates a limit to their size.

offload node status is not supported

To handle this error, Atlan recommends the following:

Reduce the number of rules in your playbook

Optimize filters for asset selection

atlan

documentation

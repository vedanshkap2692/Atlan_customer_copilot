# Cloud logging and monitoring
(source: https://docs.atlan.com/platform/references/cloud-logging-and-monitoring)

Get StartedWhat is Atlan?Quick Start GuidesCore ConceptsAdministrationCloud logging and monitoringGenerate HAR files and console logsTenant access managementTenant logsTenant monitoringTenant offboardingSecurity & ComplianceReferencesFAQs

What is Atlan?

Quick Start Guides

Core Concepts

AdministrationCloud logging and monitoringGenerate HAR files and console logsTenant access managementTenant logsTenant monitoringTenant offboarding

Cloud logging and monitoring

Generate HAR files and console logs

Tenant access management

Tenant logs

Tenant monitoring

Tenant offboarding

Security & Compliance

References

FAQs

Get Started

Administration

Cloud logging and monitoring

Atlan exports IAM service event logs in the OpenTelemetry Protocol (OTLP) specification and securely delivers them to the Amazon S3 or Google Cloud Storage (GCS) bucket of your organization. This enables you to monitor login events and integrate logs with security information and event management (SIEM) systems for real-time security monitoring and alerts.



## Key aspectsâ
(source: https://docs.atlan.com/platform/references/cloud-logging-and-monitoring)

Log format and structure: The OTLP format ensures seamless integration with SIEM systems, and logs are organized by date and event type. Logs are stored in a compressed format in your organization's preferred object storage (S3 or GCS). Once uncompressed, the logs will be available in a JSON file format containing multiple log entries.

Each file is saved for an hour in the following folder structure in gzip:/year=YYYY/month=MM/day=DD/hour=HH/logs_<rnd-9-digit-int>.json.gz

Each file is saved for an hour in the following folder structure in gzip:

/year=YYYY/month=MM/day=DD/hour=HH/logs_<rnd-9-digit-int>.json.gz

/year=YYYY/month=MM/day=DD/hour=HH/logs_<rnd-9-digit-int>.json.gz

The JSON file structure is as follows:{"resourceLogs":[{"resource":{"attributes":[// k8s metadata]},"scopeLogs":[{"scope":{},"logRecords":[{"timeUnixNano":"1725861538220747913","observedTimeUnixNano":"1726071786185095727","body":{"stringValue":"//redacted logline"},"traceId":"","spanId":""}]},{...},]},{"resource":{...},"scopeLogs":[...]}]}

The JSON file structure is as follows:

{"resourceLogs":[{"resource":{"attributes":[// k8s metadata]},"scopeLogs":[{"scope":{},"logRecords":[{"timeUnixNano":"1725861538220747913","observedTimeUnixNano":"1726071786185095727","body":{"stringValue":"//redacted logline"},"traceId":"","spanId":""}]},{...},]},{"resource":{...},"scopeLogs":[...]}]}

{"resourceLogs":[{"resource":{"attributes":[// k8s metadata]},"scopeLogs":[{"scope":{},"logRecords":[{"timeUnixNano":"1725861538220747913","observedTimeUnixNano":"1726071786185095727","body":{"stringValue":"//redacted logline"},"traceId":"","spanId":""}]},{...},]},{"resource":{...},"scopeLogs":[...]}]}

Secure delivery- Logs are encrypted in transit and at rest, with mechanisms to validate data integrity.

Secure delivery- Logs are encrypted in transit and at rest, with mechanisms to validate data integrity.

Customer access: Logs are easily accessible through S3 or GCS, allowing for a flexible monitoring and alerting setup.

Customer access: Logs are easily accessible through S3 or GCS, allowing for a flexible monitoring and alerting setup.



## Enabling event logs in AWSâ
(source: https://docs.atlan.com/platform/references/cloud-logging-and-monitoring)



### Prerequisitesâ
(source: https://docs.atlan.com/platform/references/cloud-logging-and-monitoring)

Enable bucket versioning. Both source and destination buckets must have versioning enabled. SeeAWS documentation.

Customer-provided bucket details: account ID, bucket name, and region.

Atlan will use these details to create an IAM role on the Atlan side and then provide you with the bucket policy to be attached.

Once you have confirmed that the bucket policy has been attached, Atlan will complete the final step of setting up log replication. Atlan support will complete the configuration on the Atlan side.

You will need to attach the following policy to your destination bucket:

{"Version":"2012-10-17","Id":"","Statement":[{"Sid":"Set-permissions-for-objects","Effect":"Allow","Principal":{"AWS":"<Atlan Role ARN>"},"Action":["s3:ReplicateObject","s3:ReplicateDelete","s3:GetBucketVersioning","s3:PutBucketVersioning"],"Resource":["arn:aws:s3:::<Customer S3 Bucket Name>/*","arn:aws:s3:::<Customer S3 Bucket Name>"]}]}

{"Version":"2012-10-17","Id":"","Statement":[{"Sid":"Set-permissions-for-objects","Effect":"Allow","Principal":{"AWS":"<Atlan Role ARN>"},"Action":["s3:ReplicateObject","s3:ReplicateDelete","s3:GetBucketVersioning","s3:PutBucketVersioning"],"Resource":["arn:aws:s3:::<Customer S3 Bucket Name>/*","arn:aws:s3:::<Customer S3 Bucket Name>"]}]}



### Continuous replication to S3 bucketâ
(source: https://docs.atlan.com/platform/references/cloud-logging-and-monitoring)

Application audit logs are streamed to Atlan's S3 bucket in near real time â within 10 seconds of being generated. This is a continuous process. Once the logs are available in Atlan's bucket, the logs will be replicated to your organization's S3 bucket within 15 minutes. The replication is ongoing and occurs without delays. This ensures that logs are continuously transferred as they are generated, with no waiting period between replications.



## Enabling event logs in GCPâ
(source: https://docs.atlan.com/platform/references/cloud-logging-and-monitoring)

For Google Cloud Platform (GCP), Atlan utilizesLogs Routerto transfer logs from the GCS bucket of your Atlan tenant to a destination bucket of your choice. The destination must be supported by the Logs Router.

The organization must provide details of the destination where the logs should be synced. This destination must be supported by the Logs Router.

Atlan will create a Log Router sink and provide you with a service account.

Depending on the selected destination, you will need to configure the necessary permissions for the service account as outlined inGoogle documentation.

Once you have configured the permissions, the logs will begin syncing to your preferred destination.

New sinks to Cloud Storage buckets may take several hours to start routing log entries. Sinks to Cloud Storage are processed hourly while other destination types are processed in real time.

security

monitoring

logs

compliance

siem

opentelemetry

otlp

Key aspects

Enabling event logs in AWS

Enabling event logs in GCP

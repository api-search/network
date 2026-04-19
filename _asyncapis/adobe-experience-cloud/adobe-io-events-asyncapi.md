---
channels:
- description: Events emitted when batch ingestion operations complete or fail on Adobe Experience Platform datasets.
  name: experience-platform/dataset-ingestion
  operation: subscribe
  operation_id: onDatasetIngestionEvent
  summary: Receive dataset ingestion events
- description: Events emitted when unified profile records are created or updated in Adobe Experience Platform.
  name: experience-platform/profile-update
  operation: subscribe
  operation_id: onProfileUpdateEvent
  summary: Receive profile update events
- description: Events emitted when audience segment evaluation jobs complete in Adobe Experience Platform.
  name: experience-platform/segment-evaluation
  operation: subscribe
  operation_id: onSegmentEvaluationEvent
  summary: Receive segment evaluation events
- description: Events emitted when configuration changes are made to Adobe Analytics report suites.
  name: analytics/report-suite-change
  operation: subscribe
  operation_id: onReportSuiteChangeEvent
  summary: Receive report suite change events
- description: Events emitted when Adobe Campaign email or message deliveries change status, including sends, bounces, and opens.
  name: campaign/delivery-status
  operation: subscribe
  operation_id: onDeliveryStatusEvent
  summary: Receive delivery status events
- description: Events emitted when Adobe Campaign workflow executions start, complete, or encounter errors.
  name: campaign/workflow-execution
  operation: subscribe
  operation_id: onWorkflowExecutionEvent
  summary: Receive workflow execution events
- description: Events emitted when Adobe Target activities change state, such as activation, deactivation, or archival.
  name: target/activity-state-change
  operation: subscribe
  operation_id: onActivityStateChangeEvent
  summary: Receive activity state change events
- description: Events emitted when profiles progress through journey steps in Adobe Journey Optimizer.
  name: journey-optimizer/journey-step
  operation: subscribe
  operation_id: onJourneyStepEvent
  summary: Receive journey step events
description: Adobe I/O Events enables developers to receive near-real-time notifications from Adobe services via webhooks and journal polling. Events are emitted when significant changes occur across Adobe Experience Cloud products including Experience Platform, Creative Cloud, Campaign, and Analytics. Developers register webhook endpoints or poll a journaling API to consume events for building reactive integrations and automated workflows.
layout: asyncapi
messages:
- description: ''
  name: DatasetIngestionEvent
  summary: Notification of a dataset batch ingestion completion or failure.
  title: Dataset Ingestion Event
- description: ''
  name: ProfileUpdateEvent
  summary: Notification of a unified profile creation or update.
  title: Profile Update Event
- description: ''
  name: SegmentEvaluationEvent
  summary: Notification of a segment evaluation job completion.
  title: Segment Evaluation Event
- description: ''
  name: ReportSuiteChangeEvent
  summary: Notification of an Analytics report suite configuration change.
  title: Report Suite Change Event
- description: ''
  name: DeliveryStatusEvent
  summary: Notification of a Campaign delivery status change.
  title: Delivery Status Event
- description: ''
  name: WorkflowExecutionEvent
  summary: Notification of a Campaign workflow execution status change.
  title: Workflow Execution Event
- description: ''
  name: ActivityStateChangeEvent
  summary: Notification of a Target activity state transition.
  title: Activity State Change Event
- description: ''
  name: JourneyStepEvent
  summary: Notification of a profile progressing through a journey step.
  title: Journey Step Event
name: Adobe I/O Events
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
servers:
- description: Your webhook endpoint that receives Adobe I/O Events via HTTP POST. Must respond to a challenge request for registration verification.
  name: webhook
  protocol: https
  url: https://{yourDomain}/webhook
- description: Adobe I/O Events journaling API for polling events. Use this as an alternative to webhooks for reliable, at-least-once event delivery.
  name: journal
  protocol: https
  url: https://events.adobe.io
slug: adobe-io-events-asyncapi
spec_file: asyncapi/adobe-io-events-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/asyncapi/adobe-io-events-asyncapi.yml
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---

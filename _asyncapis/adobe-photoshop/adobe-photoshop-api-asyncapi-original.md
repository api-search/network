---
channels:
- description: Notification delivered when a Photoshop API job has completed successfully. The event payload contains the job ID, output locations, and job metadata. Applies to all PSD service operations including document operations, renditions, Smart Objects, text editing, and Actions execution.
  name: photoshop/job/completed
  operation: subscribe
  operation_id: onJobCompleted
  summary: Receive job completion notifications
- description: Notification delivered when a Photoshop API job has failed. The event payload contains the job ID, error details, and failure reason.
  name: photoshop/job/failed
  operation: subscribe
  operation_id: onJobFailed
  summary: Receive job failure notifications
- description: Notification delivered when a Sensei AI service job has completed successfully. Applies to background removal, mask creation, and other AI-powered image operations.
  name: sensei/job/completed
  operation: subscribe
  operation_id: onSenseiJobCompleted
  summary: Receive Sensei AI job completion notifications
- description: Notification delivered when a Sensei AI service job has failed.
  name: sensei/job/failed
  operation: subscribe
  operation_id: onSenseiJobFailed
  summary: Receive Sensei AI job failure notifications
description: Event-driven notifications for Adobe Photoshop API asynchronous job processing. When registered through Adobe I/O Events, webhooks deliver real-time notifications when Photoshop API jobs complete or fail, eliminating the need to poll status endpoints. Covers all asynchronous operations including background removal, PSD document operations, rendition creation, Smart Object replacement, text editing, Actions execution, product crop, depth blur, and generative fill.
layout: asyncapi
messages:
- description: Webhook event payload delivered when an asynchronous Photoshop API job has completed successfully. Contains the job identifier, output details, and timestamps.
  name: JobCompletedEvent
  summary: Job completed successfully
  title: JobCompletedEvent
- description: Webhook event payload delivered when an asynchronous Photoshop API job has failed. Contains the job identifier, error details, and failure reason.
  name: JobFailedEvent
  summary: Job failed
  title: JobFailedEvent
name: Adobe Photoshop API Webhook Events
provider_name: Adobe Photoshop
provider_slug: adobe-photoshop
servers:
- description: Adobe Photoshop API production server. Webhook events are delivered via Adobe I/O Events to your registered webhook URL when async jobs complete or fail.
  name: production
  protocol: https
  url: https://image.adobe.io
slug: adobe-photoshop-api-asyncapi-original
spec_file: asyncapi/adobe-photoshop-api-asyncapi-original.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/asyncapi/adobe-photoshop-api-asyncapi-original.yml
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---

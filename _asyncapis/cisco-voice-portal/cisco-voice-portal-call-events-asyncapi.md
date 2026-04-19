---
channels:
- description: Published when a new call is received by the CVP Call Server. This event is generated after the initial SIP INVITE is processed and a call GUID is assigned.
  name: cvp/calls/started
  operation: subscribe
  operation_id: onCallStarted
  summary: Receive call started events
- description: Published when a call is terminated. Includes the final call disposition, duration, and summary of the call treatment.
  name: cvp/calls/ended
  operation: subscribe
  operation_id: onCallEnded
  summary: Receive call ended events
- description: Published when a call is transferred to another destination, such as an agent queue, external number, or another application.
  name: cvp/calls/transferred
  operation: subscribe
  operation_id: onCallTransferred
  summary: Receive call transfer events
- description: Published when a call enters a queue waiting for an agent. This event is generated when ICM/UCCE routes the call to a skill group and the call is placed in queue.
  name: cvp/calls/queued
  operation: subscribe
  operation_id: onCallQueued
  summary: Receive call queued events
- description: Published when a VXML application is invoked to handle a call. This occurs when the Call Server sends the call to a VXML Server for self-service treatment.
  name: cvp/calls/application-invoked
  operation: subscribe
  operation_id: onApplicationInvoked
  summary: Receive application invocation events
- description: Published when a call processing error occurs, such as a SIP failure, VXML application error, or ICM communication failure.
  name: cvp/calls/error
  operation: subscribe
  operation_id: onCallError
  summary: Receive call error events
- description: Published when the status of a managed CVP device changes, such as transitioning from online to offline or entering maintenance mode.
  name: cvp/system/device-status-changed
  operation: subscribe
  operation_id: onDeviceStatusChanged
  summary: Receive device status change events
- description: Published when a monitored system threshold is exceeded, such as concurrent call limits, CPU usage, memory usage, or disk space. These events correspond to SNMP traps that CVP generates.
  name: cvp/system/threshold-exceeded
  operation: subscribe
  operation_id: onThresholdExceeded
  summary: Receive threshold exceeded alerts
- description: Published when a CVP service starts, stops, or encounters an error. Monitors service health across the deployment.
  name: cvp/system/service-state-changed
  operation: subscribe
  operation_id: onServiceStateChanged
  summary: Receive service state change events
- description: Published when a configuration deployment operation completes, either successfully or with errors.
  name: cvp/deployment/config-deployed
  operation: subscribe
  operation_id: onConfigDeployed
  summary: Receive deployment completion events
description: The Cisco Unified Customer Voice Portal (CVP) generates real-time events during call processing that can be consumed for monitoring, analytics, and integration purposes. CVP publishes call lifecycle events, system alerts, and operational notifications through multiple channels including JMS messaging, SNMP traps, and syslog. This specification documents the event-driven interfaces for consuming CVP call processing events and system notifications.
layout: asyncapi
messages:
- description: ''
  name: CallStartedEvent
  summary: A new call has been received by CVP
  title: Call Started
- description: ''
  name: CallEndedEvent
  summary: A call has been terminated
  title: Call Ended
- description: ''
  name: CallTransferredEvent
  summary: A call has been transferred to a new destination
  title: Call Transferred
- description: ''
  name: CallQueuedEvent
  summary: A call has been placed in an agent queue
  title: Call Queued
- description: ''
  name: ApplicationInvokedEvent
  summary: A VXML application has been invoked to handle a call
  title: Application Invoked
- description: ''
  name: CallErrorEvent
  summary: A call processing error has occurred
  title: Call Error
- description: ''
  name: DeviceStatusChangedEvent
  summary: A managed device status has changed
  title: Device Status Changed
- description: ''
  name: ThresholdExceededEvent
  summary: A system monitoring threshold has been exceeded
  title: Threshold Exceeded
- description: ''
  name: ServiceStateChangedEvent
  summary: A CVP service has changed state
  title: Service State Changed
- description: ''
  name: ConfigDeployedEvent
  summary: A configuration deployment operation has completed
  title: Configuration Deployed
name: Cisco Voice Portal Call Events API
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
servers:
- description: CVP JMS message broker for call event notifications. The CVP Call Server and VXML Server publish events to JMS topics that can be consumed by external applications.
  name: jms
  protocol: jms
  url: tcp://{cvp-server}:61616
- description: Syslog endpoint for receiving CVP system events and alerts. CVP components forward structured syslog messages for operational events.
  name: syslog
  protocol: syslog
  url: udp://{syslog-server}:514
slug: cisco-voice-portal-call-events-asyncapi
spec_file: asyncapi/cisco-voice-portal-call-events-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/cisco-voice-portal/refs/heads/main/asyncapi/cisco-voice-portal-call-events-asyncapi.yml
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
- AsyncAPI
- Webhooks
- Events
version: 12.6.0
---

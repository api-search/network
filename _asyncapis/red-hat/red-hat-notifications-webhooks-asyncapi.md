---
channels:
- description: Triggered when the Advisor service identifies a new recommendation for one or more registered RHEL systems based on rule evaluation.
  name: advisor.newRecommendation
  operation: subscribe
  operation_id: onAdvisorNewRecommendation
  summary: New advisor recommendation
- description: Triggered when an Advisor recommendation is resolved on systems, either through remediation or configuration change.
  name: advisor.resolvedRecommendation
  operation: subscribe
  operation_id: onAdvisorResolvedRecommendation
  summary: Advisor recommendation resolved
- description: Triggered when a new CVE is detected affecting registered systems through the Vulnerability service.
  name: vulnerability.newCve
  operation: subscribe
  operation_id: onVulnerabilityNewCve
  summary: New CVE detected
- description: Triggered when the severity rating of a CVE affecting registered systems changes.
  name: vulnerability.cveSeverityChange
  operation: subscribe
  operation_id: onVulnerabilityCveSeverityChange
  summary: CVE severity changed
- description: Triggered when a system fails compliance against an assigned SCAP policy profile.
  name: compliance.policyViolation
  operation: subscribe
  operation_id: onCompliancePolicyViolation
  summary: Compliance policy violation
- description: Triggered when new errata advisories become applicable to registered systems through the Patch service.
  name: patch.newAdvisory
  operation: subscribe
  operation_id: onPatchNewAdvisory
  summary: New patch advisory
- description: Triggered when a new system is registered with Red Hat Insights through the Inventory service.
  name: inventory.systemRegistered
  operation: subscribe
  operation_id: onInventorySystemRegistered
  summary: System registered
- description: Triggered when a registered system becomes stale after failing to check in within the configured stale period.
  name: inventory.systemBecameStale
  operation: subscribe
  operation_id: onInventorySystemBecameStale
  summary: System became stale
description: The Red Hat Hybrid Cloud Console notifications service delivers event-driven notifications when significant events occur across Insights services, including advisor recommendations, vulnerability alerts, compliance changes, patch advisories, and inventory updates. Events can be forwarded via webhook integrations to third-party applications, email notifications, or integration endpoints such as Splunk, ServiceNow, and PagerDuty.
layout: asyncapi
messages:
- description: Payload delivered when the Advisor service identifies a new recommendation for one or more registered RHEL systems.
  name: AdvisorRecommendationEvent
  summary: A new Advisor recommendation was identified for systems.
  title: Advisor New Recommendation Event
- description: ''
  name: AdvisorResolvedEvent
  summary: An Advisor recommendation was resolved.
  title: Advisor Recommendation Resolved Event
- description: ''
  name: VulnerabilityNewCveEvent
  summary: A new CVE was detected affecting systems.
  title: New CVE Detected Event
- description: ''
  name: VulnerabilitySeverityChangeEvent
  summary: A CVE severity rating was changed.
  title: CVE Severity Change Event
- description: ''
  name: CompliancePolicyViolationEvent
  summary: A compliance policy violation was detected.
  title: Compliance Policy Violation Event
- description: ''
  name: PatchNewAdvisoryEvent
  summary: New patch advisories are available for systems.
  title: New Patch Advisory Event
- description: ''
  name: InventorySystemRegisteredEvent
  summary: A new system was registered with Insights.
  title: System Registered Event
- description: ''
  name: InventorySystemStaleEvent
  summary: A system became stale after missing check-ins.
  title: System Became Stale Event
name: Red Hat Hybrid Cloud Console Notifications Events
provider_name: Red Hat
provider_slug: red-hat
servers:
- description: Red Hat Hybrid Cloud Console notifications service. Events are delivered as HTTP POST requests to configured webhook endpoints when subscribed events occur across Insights services.
  name: hybridCloudConsole
  protocol: https
  url: https://console.redhat.com
slug: red-hat-notifications-webhooks-asyncapi
spec_file: asyncapi/red-hat-notifications-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/red-hat/refs/heads/main/asyncapi/red-hat-notifications-webhooks-asyncapi.yml
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---

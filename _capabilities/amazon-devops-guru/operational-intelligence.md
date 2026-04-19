---
consumed_apis:
- devops-guru
description: Workflow capability for DevOps engineers and SREs to monitor application health, investigate anomalies, follow remediation recommendations, and configure operational intelligence coverage using Amazon DevOps Guru's machine learning powered insights.
layout: capability
name: Amazon DevOps Guru Operational Intelligence
operations:
- description: Get account health with open insight counts
  method: GET
  name: describe-account-health
  path: /v1/account/health
- description: List proactive and reactive insights
  method: GET
  name: list-insights
  path: /v1/insights
- description: Search insights with filters
  method: POST
  name: search-insights
  path: /v1/insights
- description: Get details about a specific insight
  method: GET
  name: describe-insight
  path: /v1/insights/{insightId}
- description: List anomalies associated with an insight
  method: GET
  name: list-anomalies
  path: /v1/insights/{insightId}/anomalies
- description: Get remediation recommendations for an insight
  method: GET
  name: list-recommendations
  path: /v1/recommendations
- description: List events during an insight's time range
  method: GET
  name: list-events
  path: /v1/events
- description: Get the resource collection DevOps Guru monitors
  method: GET
  name: get-resource-collection
  path: /v1/resource-collections
- description: Update which resources DevOps Guru monitors
  method: PUT
  name: update-resource-collection
  path: /v1/resource-collections
- description: List notification channels
  method: GET
  name: list-notification-channels
  path: /v1/notification-channels
- description: Add an SNS notification channel
  method: PUT
  name: add-notification-channel
  path: /v1/notification-channels
personas: []
provider_name: Amazon DevOps Guru
provider_slug: amazon-devops-guru
search_terms:
- describe account health
- devops
- describe insight
- search insights
- add notification channel
- list proactive and reactive insights
- get an overview of open and closed insights for a specified time period
- site reliability engineering
- account-level operational health
- get remediation recommendations for an insight
- machine learning
- search for insights with custom filters on severity, status, and service collection
- anomalies linked to an insight
- remediation recommendations
- events correlated with insights
- list sns notification channels configured for devops guru alerts
- end-to-end operational intelligence workflow for devops engineers and sres
- individual insight details
- get cost estimation
- list events during an insight's time range
- list anomalies associated with an insight
- amazon devops guru
- alert notification configuration
- list anomalies associated with a specific insight to understand the root cause
- resource coverage configuration
- list insights
- search insights with filters
- update resource collection
- get the collection of aws resources that devops guru is currently monitoring
- get the estimated monthly cost for devops guru monitoring your resources
- get the resource collection devops guru monitors
- list recommendations
- get resource collection
- DevOps Engineer
- list anomalies for insight
- describe service integration
- sre using devops guru to maintain service level objectives and reduce mttr
- devops engineer using ml insights to proactively identify and resolve operational issues
- add or remove cloudformation stacks from the devops guru monitoring scope
- aws
- list events
- configuring resource coverage and notification channels
- get the current health of the account including counts of open proactive and reactive insights
- describe anomaly
- get details about a specific insight
- get account health with open insight counts
- describe account overview
- list machine learning powered operational insights by status (ongoing, closed) and type (proactive, reactive)
- get detailed information about a specific insight including its severity and resource details
- list cloudwatch events correlated with an insight during its time window
- operational intelligence
- machine learning powered operational insights
- add an sns notification channel
- Site Reliability Engineer
- get actionable recommendations to resolve a specific insight
- get detailed information about a specific anomaly
- update which resources devops guru monitors
- ml-powered detection and analysis of operational anomalies
- check the integration status with opscenter, cloudwatch logs, and other aws services
- list notification channels
- anomaly detection
- list anomalies
slug: operational-intelligence
tags:
- Amazon DevOps Guru
- Operational Intelligence
- Anomaly Detection
- Site Reliability Engineering
- AWS
tools:
- description: Get the current health of the account including counts of open proactive and reactive insights
  hints:
    openWorld: false
    readOnly: true
  name: describe-account-health
- description: Get an overview of open and closed insights for a specified time period
  hints:
    openWorld: false
    readOnly: true
  name: describe-account-overview
- description: List machine learning powered operational insights by status (ongoing, closed) and type (proactive, reactive)
  hints:
    openWorld: true
    readOnly: true
  name: list-insights
- description: Search for insights with custom filters on severity, status, and service collection
  hints:
    openWorld: true
    readOnly: true
  name: search-insights
- description: Get detailed information about a specific insight including its severity and resource details
  hints:
    openWorld: false
    readOnly: true
  name: describe-insight
- description: List anomalies associated with a specific insight to understand the root cause
  hints:
    openWorld: true
    readOnly: true
  name: list-anomalies-for-insight
- description: Get detailed information about a specific anomaly
  hints:
    openWorld: false
    readOnly: true
  name: describe-anomaly
- description: Get actionable recommendations to resolve a specific insight
  hints:
    openWorld: true
    readOnly: true
  name: list-recommendations
- description: List CloudWatch Events correlated with an insight during its time window
  hints:
    openWorld: true
    readOnly: true
  name: list-events
- description: Get the collection of AWS resources that DevOps Guru is currently monitoring
  hints:
    openWorld: false
    readOnly: true
  name: get-resource-collection
- description: Add or remove CloudFormation stacks from the DevOps Guru monitoring scope
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: update-resource-collection
- description: Check the integration status with OpsCenter, CloudWatch Logs, and other AWS services
  hints:
    openWorld: false
    readOnly: true
  name: describe-service-integration
- description: List SNS notification channels configured for DevOps Guru alerts
  hints:
    openWorld: true
    readOnly: true
  name: list-notification-channels
- description: Get the estimated monthly cost for DevOps Guru monitoring your resources
  hints:
    openWorld: false
    readOnly: true
  name: get-cost-estimation
---

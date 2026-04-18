---
class_count: 90
classes:
- AppSettingsBody
- AppSettingsResponse
- AppSummaryDataResponse
- AppSummaryResponse
- Application
- ApplicationBody
- name
- ApplicationHostLinksResponse
- ApplicationHostResponse
- ApplicationHostResponseType
- ApplicationInstanceLinksResponse
- ApplicationInstanceResponse
- ApplicationInstanceResponseType
- ApplicationLinksResponse
- ApplicationResponse
- ApplicationResponseType
- BrowserApplication
- BrowserApplicationBody
- BrowserApplicationResponse
- BrowserApplicationResponseType
- Channel
- ChannelBody
- ChannelLinksResponse
- ChannelResponse
- ChannelResponseType
- Condition
- ConditionBody
- ConditionResponse
- ConditionResponseType
- CrashSummaryResponse
- Deployment
- DeploymentBody
- description
- DeploymentLinksResponse
- DeploymentResponse
- DeploymentResponseType
- EndUserSummaryDataResponse
- EndUserSummaryResponse
- ExternalServiceCondition
- ExternalServiceConditionBody
- ExternalServiceConditionResponse
- ExternalServiceConditionResponseType
- IJKTermsType
- IncidentLinksResponse
- IncidentResponse
- IncidentResponseType
- KeyTransactionLinksResponse
- KeyTransactionResponse
- KeyTransactionResponseType
- Label
- LabelBody
- LabelLinksBody
- LabelLinksResponse
- LabelOriginsResponse
- LabelResponse
- LabelResponseType
- MetricDataResponse
- MetricDataResponseType
- MetricListResponse
- MetricParserResponse
- MetricParserResponseType
- MetricResponse
- MobileApplicationResponse
- MobileApplicationResponseType
- MobileSummaryDataResponse
- NrqlBody
- NrqlCondition
- NrqlConditionBody
- NrqlConditionResponse
- NrqlConditionResponseType
- NrqlResponse
- Policy
- PolicyBody
- PolicyChannelsResponse
- PolicyChannelsResponseType
- PolicyResponse
- PolicyResponseType
- RecentEventResponse
- RecentEventResponseType
- SyntheticsCondition
- SyntheticsConditionBody
- SyntheticsConditionResponse
- SyntheticsConditionResponseType
- TimesliceResponse
- UserDefinedConditionBody
- UserDefinedConditionResponse
- ViolationEntityResponse
- ViolationLinksResponse
- ViolationResponse
- ViolationResponseType
context_file: json-ld/new-relic-openapi-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-ld/new-relic-openapi-context.jsonld
description: JSON-LD context defining the semantic vocabulary for New Relic Openapi from New Relic.
layout: jsonld
name: New Relic Openapi Context
namespaces:
- prefix: nr
  uri: https://docs.newrelic.com/docs/schemas/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: appApdexThreshold
  type: decimal
- container: ''
  name: enableRealUserMonitoring
  type: boolean
- container: ''
  name: endUserApdexThreshold
  type: decimal
- container: ''
  name: useServerSideConfig
  type: boolean
- container: ''
  name: apdexScore
  type: decimal
- container: ''
  name: errorRate
  type: decimal
- container: ''
  name: instanceCount
  type: integer
- container: ''
  name: responseTime
  type: decimal
- container: ''
  name: throughput
  type: decimal
- container: ''
  name: apdexTarget
  type: decimal
- container: ''
  name: concurrentInstanceCount
  type: integer
- container: ''
  name: hostCount
  type: integer
- container: ''
  name: application
  type: string
- container: ''
  name: settings
  type: string
- container: set
  name: applicationInstances
  type: string
- container: ''
  name: server
  type: integer
- container: set
  name: applicationHosts
  type: string
- container: ''
  name: host
  type: string
- container: ''
  name: applicationName
  type: string
- container: ''
  name: applicationSummary
  type: string
- container: ''
  name: endUserSummary
  type: string
- container: ''
  name: healthStatus
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: language
  type: integer
- container: ''
  name: links
  type: string
- container: ''
  name: applicationHost
  type: integer
- container: ''
  name: applicationInstance
  type: string
- container: ''
  name: port
  type: integer
- container: set
  name: servers
  type: string
- container: ''
  name: lastReportedAt
  type: string
- container: ''
  name: reporting
  type: boolean
- container: ''
  name: browserApplication
  type: string
- container: ''
  name: browserMonitoringKey
  type: string
- container: ''
  name: loaderScript
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: configuration
  type: reference
- container: ''
  name: type
  type: string
- container: set
  name: policyIds
  type: string
- container: ''
  name: condition
  type: string
- container: ''
  name: conditionScope
  type: string
- container: ''
  name: enabled
  type: boolean
- container: set
  name: entities
  type: string
- container: ''
  name: gcMetric
  type: string
- container: ''
  name: metric
  type: string
- container: set
  name: terms
  type: string
- container: ''
  name: userDefined
  type: string
- container: ''
  name: violationCloseTimer
  type: integer
- container: ''
  name: runbookUrl
  type: string
- container: ''
  name: crashCount
  type: integer
- container: ''
  name: crashRate
  type: decimal
- container: ''
  name: supportsCrashData
  type: boolean
- container: ''
  name: unresolvedCrashCount
  type: integer
- container: ''
  name: deployment
  type: string
- container: ''
  name: changelog
  type: string
- container: ''
  name: revision
  type: string
- container: ''
  name: user
  type: string
- container: ''
  name: timestamp
  type: string
- container: ''
  name: externalServiceCondition
  type: string
- container: ''
  name: externalServiceUrl
  type: string
- container: ''
  name: duration
  type: string
- container: ''
  name: operator
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: threshold
  type: string
- container: ''
  name: timeFunction
  type: string
- container: ''
  name: policyId
  type: integer
- container: set
  name: violations
  type: string
- container: ''
  name: incident
  type: string
- container: ''
  name: closedAt
  type: integer
- container: ''
  name: incidentPreference
  type: integer
- container: ''
  name: openedAt
  type: integer
- container: ''
  name: keyTransaction
  type: string
- container: ''
  name: transactionName
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: category
  type: string
- container: set
  name: applications
  type: string
- container: set
  name: agents
  type: string
- container: set
  name: apm
  type: string
- container: set
  name: synthetics
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: origins
  type: string
- container: ''
  name: metricData
  type: string
- container: ''
  name: from
  type: string
- container: set
  name: metrics
  type: string
- container: ''
  name: metricsFound
  type: string
- container: ''
  name: metricsNotFound
  type: string
- container: ''
  name: to
  type: string
- container: set
  name: values
  type: string
- container: set
  name: timeslices
  type: string
- container: ''
  name: crashSummary
  type: string
- container: ''
  name: mobileSummary
  type: string
- container: ''
  name: activeUsers
  type: integer
- container: ''
  name: callsPerSession
  type: decimal
- container: ''
  name: failedCallRate
  type: decimal
- container: ''
  name: interactionTime
  type: decimal
- container: ''
  name: launchCount
  type: integer
- container: ''
  name: remoteErrorRate
  type: decimal
- container: ''
  name: query
  type: string
- container: ''
  name: sinceValue
  type: string
- container: ''
  name: nrqlCondition
  type: string
- container: ''
  name: expectedGroups
  type: integer
- container: ''
  name: ignoreOverlap
  type: boolean
- container: ''
  name: nrql
  type: string
- container: ''
  name: valueFunction
  type: string
- container: ''
  name: policy
  type: string
- container: set
  name: channelIds
  type: string
- container: ''
  name: createdAt
  type: integer
- container: ''
  name: updatedAt
  type: integer
- container: ''
  name: recentEvent
  type: string
- container: ''
  name: entityGroupId
  type: integer
- container: ''
  name: entityId
  type: integer
- container: ''
  name: entityType
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: incidentId
  type: integer
- container: ''
  name: product
  type: string
- container: ''
  name: syntheticsCondition
  type: string
- container: ''
  name: monitorId
  type: string
- container: ''
  name: groupId
  type: integer
- container: ''
  name: conditionId
  type: integer
- container: ''
  name: violation
  type: string
- container: ''
  name: conditionName
  type: string
- container: ''
  name: entity
  type: string
- container: ''
  name: policyName
  type: string
property_count: 122
provider_name: New Relic
provider_slug: new-relic
slug: new-relic-openapi-context
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
- JSON-LD
- Linked Data
- Semantic Web
---

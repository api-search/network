---
class_count: 71
classes:
- AddNotificationChannelsResponse
- Channel
- BatchGetFrameMetricDataResponse
- FrameMetric
- ConfigureAgentResponse
- CreateProfilingGroupResponse
- DeleteProfilingGroupResponse
- DescribeProfilingGroupResponse
- GetFindingsReportAccountSummaryResponse
- GetNotificationConfigurationResponse
- GetPolicyResponse
- GetProfileResponse
- GetRecommendationsResponse
- ListFindingsReportsResponse
- ListProfileTimesResponse
- ListProfilingGroupsResponse
- ListTagsForResourceResponse
- PostAgentProfileResponse
- PutPermissionResponse
- RemoveNotificationChannelResponse
- RemovePermissionResponse
- SubmitFeedbackResponse
- TagResourceResponse
- UntagResourceResponse
- UpdateProfilingGroupResponse
- AddNotificationChannelsRequest
- NotificationConfiguration
- AgentParameters
- AgentConfiguration
- AgentOrchestrationConfig
- AggregatedProfileTime
- Anomaly
- Metric
- UserFeedback
- AnomalyInstance
- BatchGetFrameMetricDataRequest
- UnprocessedEndTimeMap
- Metadata
- ConfigureAgentRequest
- TagsMap
- CreateProfilingGroupRequest
- ProfilingGroupDescription
- DeleteProfilingGroupRequest
- DescribeProfilingGroupRequest
- FindingsReportSummary
- FrameMetricDatum
- GetFindingsReportAccountSummaryRequest
- GetNotificationConfigurationRequest
- GetPolicyRequest
- GetProfileRequest
- GetRecommendationsRequest
- ListFindingsReportsRequest
- TimestampStructure
- ListProfileTimesRequest
- ListProfilingGroupsRequest
- ListTagsForResourceRequest
- Match
- Pattern
- PostAgentProfileRequest
- ProfileTime
- ProfilingStatus
- PutPermissionRequest
- Recommendation
- RemoveNotificationChannelRequest
- RemovePermissionRequest
- SubmitFeedbackRequest
- TagResourceRequest
- UntagResourceRequest
- UpdateProfilingGroupRequest
- name
- description
context_file: json-ld/amazon-codeguru-profiler-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-profiler/refs/heads/main/json-ld/amazon-codeguru-profiler-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codeguru Profiler from Amazon CodeGuru Profiler.
layout: jsonld
name: Amazon Codeguru Profiler Context
namespaces:
- prefix: amazon-code-guru-profiler
  uri: https://amazon-code-guru-profiler.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: notificationConfiguration
  type: string
- container: ''
  name: eventPublishers
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: uri
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: endTimes
  type: string
- container: ''
  name: frameMetricData
  type: string
- container: ''
  name: resolution
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: unprocessedEndTimes
  type: string
- container: ''
  name: frameName
  type: string
- container: ''
  name: threadStates
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: configuration
  type: string
- container: ''
  name: profilingGroup
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: reportSummaries
  type: string
- container: ''
  name: policy
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: profile
  type: string
- container: ''
  name: anomalies
  type: string
- container: ''
  name: profileEndTime
  type: string
- container: ''
  name: profileStartTime
  type: string
- container: ''
  name: profilingGroupName
  type: string
- container: ''
  name: recommendations
  type: string
- container: ''
  name: findingsReportSummaries
  type: string
- container: ''
  name: profileTimes
  type: string
- container: ''
  name: profilingGroupNames
  type: string
- container: ''
  name: profilingGroups
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: channels
  type: string
- container: ''
  name: agentParameters
  type: string
- container: ''
  name: periodInSeconds
  type: string
- container: ''
  name: shouldProfile
  type: string
- container: ''
  name: profilingEnabled
  type: string
- container: ''
  name: period
  type: string
- container: ''
  name: start
  type: string
- container: ''
  name: instances
  type: string
- container: ''
  name: metric
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: userFeedback
  type: string
- container: ''
  name: frameMetrics
  type: string
- container: ''
  name: fleetInstanceId
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: agentOrchestrationConfig
  type: string
- container: ''
  name: computePlatform
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: profilingStatus
  type: string
- container: ''
  name: updatedAt
  type: string
- container: ''
  name: totalNumberOfFindings
  type: string
- container: ''
  name: frameMetric
  type: string
- container: ''
  name: values
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: frameAddress
  type: string
- container: ''
  name: targetFramesIndex
  type: string
- container: ''
  name: thresholdBreachValue
  type: string
- container: ''
  name: countersToAggregate
  type: string
- container: ''
  name: resolutionSteps
  type: string
- container: ''
  name: targetFrames
  type: string
- container: ''
  name: thresholdPercent
  type: string
- container: ''
  name: agentProfile
  type: string
- container: ''
  name: latestAgentOrchestratedAt
  type: string
- container: ''
  name: latestAgentProfileReportedAt
  type: string
- container: ''
  name: latestAggregatedProfile
  type: string
- container: ''
  name: principals
  type: string
- container: ''
  name: allMatchesCount
  type: string
- container: ''
  name: allMatchesSum
  type: string
- container: ''
  name: pattern
  type: string
- container: ''
  name: topMatches
  type: string
- container: ''
  name: comment
  type: string
property_count: 71
provider_name: Amazon CodeGuru Profiler
provider_slug: amazon-codeguru-profiler
slug: amazon-codeguru-profiler-context
tags:
- Amazon
- AWS
- Application Performance
- Profiling
- DevOps
- Machine Learning
- JSON-LD
- Linked Data
- Semantic Web
---

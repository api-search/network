---
class_count: 61
classes:
- HoursOfOperationSummary
- UserSummary
- InstanceSummary
- CreateContactFlowRequest
- GetCurrentMetricDataRequest
- MediaConcurrency
- Queue
- CreateQueueResponse
- ListAgentStatusesResponse
- HoursOfOperationConfig
- CreateUserResponse
- ContactFlowSummary
- ContactSummary
- DescribeContactFlowResponse
- StartTaskContactRequest
- ListContactFlowsResponse
- DescribeQueueResponse
- DescribeInstanceResponse
- QueueSummary
- StartOutboundVoiceContactRequest
- UserPhoneConfig
- Instance
- StartChatContactResponse
- ListRoutingProfilesResponse
- CreateHoursOfOperationRequest
- ContactFlow
- ListQueuesResponse
- SecurityProfileSummary
- SearchContactsRequest
- HoursOfOperationTimeSlice
- UpdateUserIdentityInfoRequest
- DescribeContactResponse
- GetCurrentMetricDataResponse
- DescribeRoutingProfileResponse
- Amazon Connect Instance
- ListInstancesResponse
- GetMetricDataResponse
- DescribeUserResponse
- CreateUserRequest
- CreateQueueRequest
- CreateHoursOfOperationResponse
- CreateInstanceRequest
- ListHoursOfOperationsResponse
- ListSecurityProfilesResponse
- RoutingProfile
- CreateRoutingProfileResponse
- GetMetricDataRequest
- UserIdentityInfo
- CreateContactFlowResponse
- CreateInstanceResponse
- User
- StartChatContactRequest
- Contact
- ListUsersResponse
- RoutingProfileSummary
- SearchContactsResponse
- CreateRoutingProfileRequest
- AgentStatusSummary
- description
- email
- name
context_file: json-ld/amazon-connect-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-connect/refs/heads/main/json-ld/amazon-connect-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Connect from Amazon Connect.
layout: jsonld
name: Amazon Connect Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/connect/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: afterContactWorkTimeLimit
  type: integer
- container: set
  name: agentIds
  type: string
- container: ''
  name: agentInfo
  type: reference
- container: set
  name: agentStatusSummaryList
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: attributes
  type: reference
- container: ''
  name: autoAccept
  type: boolean
- container: ''
  name: channel
  type: string
- container: set
  name: channels
  type: string
- container: ''
  name: chatDurationInMinutes
  type: integer
- container: ''
  name: clientToken
  type: string
- container: set
  name: collections
  type: reference
- container: ''
  name: concurrency
  type: integer
- container: set
  name: config
  type: string
- container: ''
  name: connectedToAgentTimestamp
  type: dateTime
- container: ''
  name: contact
  type: string
- container: ''
  name: contactFlow
  type: string
- container: ''
  name: contactFlowArn
  type: string
- container: ''
  name: contactFlowId
  type: string
- container: ''
  name: contactFlowState
  type: string
- container: set
  name: contactFlowSummaryList
  type: string
- container: ''
  name: contactFlowType
  type: string
- container: ''
  name: contactId
  type: string
- container: set
  name: contacts
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: contentType
  type: string
- container: ''
  name: createdTime
  type: dateTime
- container: set
  name: currentMetrics
  type: reference
- container: ''
  name: dataSnapshotTime
  type: dateTime
- container: ''
  name: day
  type: string
- container: ''
  name: defaultOutboundQueueId
  type: string
- container: ''
  name: delay
  type: integer
- container: ''
  name: deskPhoneNumber
  type: string
- container: ''
  name: destinationPhoneNumber
  type: string
- container: ''
  name: dimensions
  type: reference
- container: ''
  name: directoryId
  type: string
- container: ''
  name: directoryUserId
  type: string
- container: ''
  name: disconnectTimestamp
  type: dateTime
- container: ''
  name: displayName
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: enqueueTimestamp
  type: dateTime
- container: ''
  name: fieldName
  type: string
- container: ''
  name: filters
  type: reference
- container: ''
  name: firstName
  type: string
- container: set
  name: groupings
  type: string
- container: ''
  name: hierarchyGroupId
  type: string
- container: set
  name: historicalMetrics
  type: reference
- container: ''
  name: hours
  type: integer
- container: ''
  name: hoursOfOperationArn
  type: string
- container: ''
  name: hoursOfOperationId
  type: string
- container: set
  name: hoursOfOperationSummaryList
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: identityInfo
  type: string
- container: ''
  name: identityManagementType
  type: string
- container: ''
  name: inboundCallsEnabled
  type: boolean
- container: ''
  name: initialContactId
  type: string
- container: ''
  name: initialMessage
  type: reference
- container: ''
  name: initiationMethod
  type: string
- container: ''
  name: initiationTimestamp
  type: dateTime
- container: ''
  name: instance
  type: string
- container: ''
  name: instanceAlias
  type: string
- container: ''
  name: instanceId
  type: string
- container: ''
  name: instanceStatus
  type: string
- container: set
  name: instanceSummaryList
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: lastUpdateTimestamp
  type: dateTime
- container: ''
  name: maxContacts
  type: integer
- container: ''
  name: maxResults
  type: integer
- container: set
  name: mediaConcurrencies
  type: string
- container: ''
  name: metric
  type: reference
- container: set
  name: metricResults
  type: reference
- container: ''
  name: minutes
  type: integer
- container: ''
  name: mobile
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: numberOfAssociatedQueues
  type: integer
- container: ''
  name: numberOfAssociatedUsers
  type: integer
- container: ''
  name: order
  type: string
- container: ''
  name: outboundCallerConfig
  type: reference
- container: ''
  name: outboundCallerIdName
  type: string
- container: ''
  name: outboundCallerIdNumberId
  type: string
- container: ''
  name: outboundCallsEnabled
  type: boolean
- container: ''
  name: outboundFlowId
  type: string
- container: ''
  name: participantDetails
  type: reference
- container: ''
  name: participantId
  type: string
- container: ''
  name: participantToken
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: phoneConfig
  type: string
- container: ''
  name: phoneType
  type: string
- container: ''
  name: previousContactId
  type: string
- container: ''
  name: priority
  type: integer
- container: ''
  name: queue
  type: string
- container: ''
  name: queueArn
  type: string
- container: set
  name: queueConfigs
  type: reference
- container: ''
  name: queueId
  type: string
- container: set
  name: queueIds
  type: string
- container: ''
  name: queueInfo
  type: reference
- container: ''
  name: queueReference
  type: reference
- container: set
  name: queueSummaryList
  type: string
- container: ''
  name: queueType
  type: string
- container: set
  name: queues
  type: string
- container: ''
  name: quickConnectId
  type: string
- container: ''
  name: references
  type: reference
- container: ''
  name: relatedContactId
  type: string
- container: ''
  name: routingProfile
  type: string
- container: ''
  name: routingProfileArn
  type: string
- container: ''
  name: routingProfileId
  type: string
- container: set
  name: routingProfileSummaryList
  type: string
- container: ''
  name: scheduledTime
  type: dateTime
- container: ''
  name: searchCriteria
  type: reference
- container: ''
  name: secondaryEmail
  type: string
- container: set
  name: securityProfileIds
  type: string
- container: set
  name: securityProfileSummaryList
  type: string
- container: ''
  name: serviceRole
  type: string
- container: ''
  name: sort
  type: reference
- container: ''
  name: sourcePhoneNumber
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: statistic
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: tags
  type: reference
- container: ''
  name: taskTemplateId
  type: string
- container: ''
  name: timeRange
  type: reference
- container: ''
  name: timeZone
  type: string
- container: ''
  name: totalCount
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: user
  type: string
- container: ''
  name: userArn
  type: string
- container: ''
  name: userId
  type: string
- container: set
  name: userSummaryList
  type: string
- container: ''
  name: username
  type: string
- container: ''
  name: value
  type: decimal
property_count: 132
provider_name: Amazon Connect
provider_slug: amazon-connect
slug: amazon-connect-context
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
- JSON-LD
- Linked Data
- Semantic Web
---

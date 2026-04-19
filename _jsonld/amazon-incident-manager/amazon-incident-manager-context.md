---
class_count: 100
classes:
- Action
- AddRegionAction
- AttributeValueList
- AutomationExecution
- ChatChannel
- Condition
- CreateReplicationSetInput
- CreateReplicationSetOutput
- CreateResponsePlanInput
- CreateResponsePlanOutput
- CreateTimelineEventInput
- CreateTimelineEventOutput
- DeleteIncidentRecordInput
- DeleteIncidentRecordOutput
- DeleteRegionAction
- DeleteReplicationSetInput
- DeleteReplicationSetOutput
- DeleteResourcePolicyInput
- DeleteResourcePolicyOutput
- DeleteResponsePlanInput
- DeleteResponsePlanOutput
- DeleteTimelineEventInput
- DeleteTimelineEventOutput
- DynamicSsmParameterValue
- DynamicSsmParameters
- EmptyChatChannel
- EventReference
- EventSummary
- Filter
- GetIncidentRecordInput
- GetIncidentRecordOutput
- GetReplicationSetInput
- GetReplicationSetOutput
- GetResourcePoliciesInput
- GetResourcePoliciesOutput
- GetResponsePlanInput
- GetResponsePlanOutput
- GetTimelineEventInput
- GetTimelineEventOutput
- IncidentRecord
- IncidentRecordSource
- IncidentRecordSummary
- IncidentTemplate
- Integration
- ItemIdentifier
- ItemValue
- ListIncidentRecordsInput
- ListIncidentRecordsOutput
- ListRelatedItemsInput
- ListRelatedItemsOutput
- ListReplicationSetsInput
- ListReplicationSetsOutput
- ListResponsePlansInput
- ListResponsePlansOutput
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- ListTimelineEventsInput
- ListTimelineEventsOutput
- NotificationTargetItem
- PagerDutyConfiguration
- PagerDutyIncidentConfiguration
- PagerDutyIncidentDetail
- PutResourcePolicyInput
- PutResourcePolicyOutput
- RegionInfo
- RegionInfoMap
- RegionMapInput
- RegionMapInputValue
- RelatedItem
- RelatedItemsUpdate
- ReplicationSet
- ResourcePolicy
- ResponsePlanSummary
- SsmAutomation
- SsmParameters
- StartIncidentInput
- StartIncidentOutput
- TagMap
- TagMapUpdate
- TagResourceRequest
- TagResourceResponse
- TimelineEvent
- TriggerDetails
- UntagResourceRequest
- UntagResourceResponse
- UpdateDeletionProtectionInput
- UpdateDeletionProtectionOutput
- UpdateIncidentRecordInput
- UpdateIncidentRecordOutput
- UpdateRelatedItemsInput
- UpdateRelatedItemsOutput
- UpdateReplicationSetAction
- UpdateReplicationSetInput
- UpdateReplicationSetOutput
- UpdateResponsePlanInput
- UpdateResponsePlanOutput
- UpdateTimelineEventInput
- UpdateTimelineEventOutput
- name
- url
context_file: json-ld/amazon-incident-manager-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-incident-manager/refs/heads/main/json-ld/amazon-incident-manager-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Incident Manager from Amazon Incident Manager.
layout: jsonld
name: Amazon Incident Manager Context
namespaces:
- prefix: amzn
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: actions
  type: string
- container: ''
  name: addRegionAction
  type: string
- container: ''
  name: after
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: autoResolve
  type: string
- container: ''
  name: automationExecutions
  type: string
- container: ''
  name: before
  type: string
- container: ''
  name: chatChannel
  type: string
- container: ''
  name: chatbotSns
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: condition
  type: string
- container: ''
  name: createdBy
  type: string
- container: ''
  name: createdTime
  type: string
- container: ''
  name: creationTime
  type: string
- container: ''
  name: dedupeString
  type: string
- container: ''
  name: deleteRegionAction
  type: string
- container: ''
  name: deletionProtected
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: documentName
  type: string
- container: ''
  name: documentVersion
  type: string
- container: ''
  name: dynamicParameters
  type: string
- container: ''
  name: empty
  type: string
- container: ''
  name: engagements
  type: string
- container: ''
  name: equals
  type: string
- container: ''
  name: event
  type: string
- container: ''
  name: eventData
  type: string
- container: ''
  name: eventId
  type: string
- container: ''
  name: eventReferences
  type: string
- container: ''
  name: eventSummaries
  type: string
- container: ''
  name: eventTime
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: eventUpdatedTime
  type: string
- container: ''
  name: filters
  type: string
- container: ''
  name: generatedId
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: identifier
  type: string
- container: ''
  name: impact
  type: string
- container: ''
  name: incidentRecord
  type: string
- container: ''
  name: incidentRecordArn
  type: string
- container: ''
  name: incidentRecordSource
  type: string
- container: ''
  name: incidentRecordSummaries
  type: string
- container: ''
  name: incidentTags
  type: string
- container: ''
  name: incidentTemplate
  type: string
- container: ''
  name: incidentTemplateDedupeString
  type: string
- container: ''
  name: incidentTemplateImpact
  type: string
- container: ''
  name: incidentTemplateNotificationTargets
  type: string
- container: ''
  name: incidentTemplateSummary
  type: string
- container: ''
  name: incidentTemplateTags
  type: string
- container: ''
  name: incidentTemplateTitle
  type: string
- container: ''
  name: integerValues
  type: string
- container: ''
  name: integrations
  type: string
- container: ''
  name: invokedBy
  type: string
- container: ''
  name: itemToAdd
  type: string
- container: ''
  name: itemToRemove
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: lastModifiedBy
  type: string
- container: ''
  name: lastModifiedTime
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: metricDefinition
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: notificationTargets
  type: string
- container: ''
  name: pagerDutyConfiguration
  type: string
- container: ''
  name: pagerDutyIncidentConfiguration
  type: string
- container: ''
  name: pagerDutyIncidentDetail
  type: string
- container: ''
  name: parameters
  type: string
- container: ''
  name: policy
  type: string
- container: ''
  name: policyDocument
  type: string
- container: ''
  name: policyId
  type: string
- container: ''
  name: ramResourceShareRegion
  type: string
- container: ''
  name: rawData
  type: string
- container: ''
  name: regionMap
  type: string
- container: ''
  name: regionName
  type: string
- container: ''
  name: regions
  type: string
- container: ''
  name: relatedItemId
  type: string
- container: ''
  name: relatedItems
  type: string
- container: ''
  name: relatedItemsUpdate
  type: string
- container: ''
  name: replicationSet
  type: string
- container: ''
  name: replicationSetArns
  type: string
- container: ''
  name: resolvedTime
  type: string
- container: ''
  name: resource
  type: string
- container: ''
  name: resourceArn
  type: string
- container: ''
  name: resourcePolicies
  type: string
- container: ''
  name: responsePlanArn
  type: string
- container: ''
  name: responsePlanSummaries
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: secretId
  type: string
- container: ''
  name: serviceId
  type: string
- container: ''
  name: snsTopicArn
  type: string
- container: ''
  name: sortBy
  type: string
- container: ''
  name: sortOrder
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: sseKmsKeyId
  type: string
- container: ''
  name: ssmAutomation
  type: string
- container: ''
  name: ssmExecutionArn
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusMessage
  type: string
- container: ''
  name: statusUpdateDateTime
  type: string
- container: ''
  name: stringValues
  type: string
- container: ''
  name: summary
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: targetAccount
  type: string
- container: ''
  name: timestamp
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: triggerArn
  type: string
- container: ''
  name: triggerDetails
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: variable
  type: string
property_count: 108
provider_name: Amazon Incident Manager
provider_slug: amazon-incident-manager
slug: amazon-incident-manager-context
tags:
- Automation
- AWS
- DevOps
- Incident Management
- Operations
- JSON-LD
- Linked Data
- Semantic Web
---

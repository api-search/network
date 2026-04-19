---
class_count: 51
classes:
- ActivityResponse
- ListJourneysResponse
- JourneysResponse
- GetJourneyExecutionActivityMetricsRequest
- JourneyLimits
- UpdateJourneyResponse
- JourneyResponse
- WaitTime
- EmailMessageActivity
- DeleteJourneyResponse
- JourneyStateRequest
- SimpleCondition
- EventCondition
- JourneyExecutionActivityMetricsResponse
- HoldoutActivity
- JourneyEmailMessage
- GetJourneyResponse
- DeleteJourneyRequest
- GetJourneyDateRangeKpiResponse
- JourneyDateRangeKpiResponse
- JourneyChannelSettings
- GetJourneyExecutionMetricsResponse
- JourneyExecutionMetricsResponse
- JourneySchedule
- JourneyPushMessage
- GetJourneyRequest
- Activity
- EventStartCondition
- MultiConditionalSplitActivity
- WriteJourneyRequest
- StartCondition
- WaitActivity
- UpdateJourneyStateRequest
- UpdateJourneyRequest
- ListJourneysRequest
- JourneyCustomMessage
- SMSMessageActivity
- CustomMessageActivity
- JourneySMSMessage
- UpdateJourneyStateResponse
- ConditionalSplitActivity
- Condition
- GetJourneyExecutionActivityMetricsResponse
- PushMessageActivity
- CreateJourneyRequest
- GetJourneyDateRangeKpiRequest
- RandomSplitActivity
- MultiConditionalBranch
- CreateJourneyResponse
- GetJourneyExecutionMetricsRequest
- ContactCenterActivity
context_file: json-ld/amazon-pinpoint-journeys-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-pinpoint/refs/heads/main/json-ld/amazon-pinpoint-journeys-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Pinpoint Journeys from Amazon Pinpoint.
layout: jsonld
name: Amazon Pinpoint Journeys Context
namespaces:
- prefix: pinpoint
  uri: https://pinpoint.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ApplicationId
  type: string
- container: ''
  name: CampaignId
  type: string
- container: ''
  name: End
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: Result
  type: string
- container: ''
  name: ScheduledStart
  type: string
- container: ''
  name: Start
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: SuccessfulEndpointCount
  type: string
- container: ''
  name: TimezonesCompletedCount
  type: string
- container: ''
  name: TimezonesTotalCount
  type: string
- container: ''
  name: TotalEndpointCount
  type: string
- container: ''
  name: TreatmentId
  type: string
- container: ''
  name: DailyCap
  type: string
- container: ''
  name: EndpointReentryCap
  type: string
- container: ''
  name: MessagesPerSecond
  type: string
- container: ''
  name: EndpointReentryInterval
  type: string
- container: ''
  name: WaitFor
  type: string
- container: ''
  name: WaitUntil
  type: string
- container: ''
  name: MessageConfig
  type: string
- container: ''
  name: NextActivity
  type: string
- container: ''
  name: TemplateName
  type: string
- container: ''
  name: TemplateVersion
  type: string
- container: ''
  name: SegmentCondition
  type: string
- container: ''
  name: SegmentDimensions
  type: string
- container: ''
  name: ActivityType
  type: string
- container: ''
  name: JourneyActivityId
  type: string
- container: ''
  name: JourneyId
  type: string
- container: ''
  name: LastEvaluatedTime
  type: string
- container: ''
  name: Metrics
  type: string
- container: ''
  name: Percentage
  type: string
- container: ''
  name: FromAddress
  type: string
- container: ''
  name: ConnectCampaignArn
  type: string
- container: ''
  name: ConnectCampaignExecutionRoleArn
  type: string
- container: ''
  name: Item
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: EndTime
  type: string
- container: ''
  name: KpiName
  type: string
- container: ''
  name: KpiResult
  type: string
- container: ''
  name: StartTime
  type: string
- container: ''
  name: Timezone
  type: string
- container: ''
  name: TimeToLive
  type: string
- container: ''
  name: CUSTOM
  type: string
- container: ''
  name: ConditionalSplit
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: EMAIL
  type: string
- container: ''
  name: Holdout
  type: string
- container: ''
  name: MultiCondition
  type: string
- container: ''
  name: PUSH
  type: string
- container: ''
  name: RandomSplit
  type: string
- container: ''
  name: SMS
  type: string
- container: ''
  name: Wait
  type: string
- container: ''
  name: ContactCenter
  type: string
- container: ''
  name: EventFilter
  type: string
- container: ''
  name: SegmentId
  type: string
- container: ''
  name: Branches
  type: string
- container: ''
  name: DefaultActivity
  type: string
- container: ''
  name: EvaluationWaitTime
  type: string
- container: ''
  name: Activities
  type: string
- container: ''
  name: CreationDate
  type: string
- container: ''
  name: LastModifiedDate
  type: string
- container: ''
  name: Limits
  type: string
- container: ''
  name: LocalTime
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: QuietTime
  type: string
- container: ''
  name: RefreshFrequency
  type: string
- container: ''
  name: Schedule
  type: string
- container: ''
  name: StartActivity
  type: string
- container: ''
  name: WaitForQuietTime
  type: string
- container: ''
  name: RefreshOnSegmentUpdate
  type: string
- container: ''
  name: SendingSchedule
  type: string
- container: ''
  name: OpenHours
  type: string
- container: ''
  name: ClosedDays
  type: string
- container: ''
  name: Data
  type: string
- container: ''
  name: Dimensions
  type: string
- container: ''
  name: MessageActivity
  type: string
- container: ''
  name: DeliveryUri
  type: string
- container: ''
  name: EndpointTypes
  type: string
- container: ''
  name: MessageType
  type: string
- container: ''
  name: OriginationNumber
  type: string
- container: ''
  name: SenderId
  type: string
- container: ''
  name: EntityId
  type: string
- container: ''
  name: TemplateId
  type: string
- container: ''
  name: FalseActivity
  type: string
- container: ''
  name: TrueActivity
  type: string
- container: ''
  name: Conditions
  type: string
- container: ''
  name: Operator
  type: string
- container: ''
  name: SegmentStartCondition
  type: string
- container: ''
  name: tags
  type: string
property_count: 89
provider_name: Amazon Pinpoint
provider_slug: amazon-pinpoint
slug: amazon-pinpoint-journeys-context
tags:
- AWS
- Campaigns
- Communications
- Email
- Marketing
- Messaging
- Push Notifications
- SMS
- Voice
- Customer Engagement
- Segmentation
- Journeys
- Analytics
- JSON-LD
- Linked Data
- Semantic Web
---

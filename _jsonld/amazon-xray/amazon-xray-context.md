---
class_count: 108
classes:
- BatchGetTracesResult
- CreateGroupResult
- Group
- Tag
- CreateSamplingRuleResult
- SamplingRuleRecord
- AttributeMap
- DeleteGroupResult
- DeleteResourcePolicyResult
- DeleteSamplingRuleResult
- GetEncryptionConfigResult
- EncryptionConfig
- GetGroupResult
- GetGroupsResult
- GetInsightResult
- Insight
- GetInsightEventsResult
- GetInsightImpactGraphResult
- GetInsightSummariesResult
- GetSamplingRulesResult
- GetSamplingStatisticSummariesResult
- GetSamplingTargetsResult
- UnprocessedStatistics
- SamplingStatisticsDocument
- GetServiceGraphResult
- GetTimeSeriesServiceStatisticsResult
- TimeSeriesServiceStatistics
- GetTraceGraphResult
- GetTraceSummariesResult
- ListResourcePoliciesResult
- ListTagsForResourceResponse
- PutEncryptionConfigResult
- PutResourcePolicyResult
- ResourcePolicy
- PutTelemetryRecordsResult
- TelemetryRecord
- BackendConnectionErrors
- PutTraceSegmentsResult
- TagResourceResponse
- UntagResourceResponse
- UpdateGroupResult
- UpdateSamplingRuleResult
- Alias
- AnomalousService
- AvailabilityZoneDetail
- BatchGetTracesRequest
- CreateGroupRequest
- CreateSamplingRuleRequest
- DeleteGroupRequest
- DeleteResourcePolicyRequest
- DeleteSamplingRuleRequest
- EdgeStatistics
- ErrorStatistics
- FaultStatistics
- Edge
- ErrorRootCause
- ErrorRootCauseEntity
- ErrorRootCauseService
- FaultRootCause
- FaultRootCauseEntity
- FaultRootCauseService
- GetEncryptionConfigRequest
- GetGroupRequest
- GetGroupsRequest
- GetInsightEventsRequest
- GetInsightImpactGraphRequest
- GetInsightRequest
- GetInsightSummariesRequest
- GetSamplingRulesRequest
- GetSamplingStatisticSummariesRequest
- GetSamplingTargetsRequest
- GetServiceGraphRequest
- GetTimeSeriesServiceStatisticsRequest
- GetTraceGraphRequest
- GetTraceSummariesRequest
- GroupSummary
- HistogramEntry
- RequestImpactStatistics
- InsightEvent
- InsightImpactGraphEdge
- InsightImpactGraphService
- InsightSummary
- InstanceIdDetail
- ListResourcePoliciesRequest
- ListTagsForResourceRequest
- PutEncryptionConfigRequest
- PutResourcePolicyRequest
- PutTelemetryRecordsRequest
- PutTraceSegmentsRequest
- ResourceARNDetail
- ResponseTimeRootCause
- ResponseTimeRootCauseEntity
- ResponseTimeRootCauseService
- RootCauseException
- SamplingStatisticSummary
- SamplingTargetDocument
- Segment
- ServiceStatistics
- Service
- TagResourceRequest
- Trace
- TraceSummary
- TraceUser
- UnprocessedTraceSegment
- UntagResourceRequest
- UpdateGroupRequest
- UpdateSamplingRuleRequest
- ValueWithServiceIds
context_file: json-ld/amazon-xray-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-xray/refs/heads/main/json-ld/amazon-xray-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Xray from Amazon X-Ray.
layout: jsonld
name: Amazon Xray Context
namespaces:
- prefix: amz
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Traces
  type: string
- container: ''
  name: UnprocessedTraceIds
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: Groups
  type: string
- container: ''
  name: InsightEvents
  type: string
- container: ''
  name: InsightId
  type: string
- container: ''
  name: StartTime
  type: string
- container: ''
  name: EndTime
  type: string
- container: ''
  name: ServiceGraphStartTime
  type: string
- container: ''
  name: ServiceGraphEndTime
  type: string
- container: ''
  name: Services
  type: string
- container: ''
  name: InsightSummaries
  type: string
- container: ''
  name: SamplingRuleRecords
  type: string
- container: ''
  name: SamplingStatisticSummaries
  type: string
- container: ''
  name: SamplingTargetDocuments
  type: string
- container: ''
  name: LastRuleModification
  type: string
- container: ''
  name: RuleName
  type: string
- container: ''
  name: ClientID
  type: string
- container: ''
  name: Timestamp
  type: string
- container: ''
  name: RequestCount
  type: string
- container: ''
  name: SampledCount
  type: string
- container: ''
  name: BorrowCount
  type: string
- container: ''
  name: ContainsOldGroupVersions
  type: string
- container: ''
  name: TraceSummaries
  type: string
- container: ''
  name: ApproximateTime
  type: string
- container: ''
  name: TracesProcessedCount
  type: string
- container: ''
  name: ResourcePolicies
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: SegmentsReceivedCount
  type: string
- container: ''
  name: SegmentsSentCount
  type: string
- container: ''
  name: SegmentsSpilloverCount
  type: string
- container: ''
  name: SegmentsRejectedCount
  type: string
- container: ''
  name: UnprocessedTraceSegments
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Names
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: AnnotationValue
  type: string
- container: ''
  name: NumberValue
  type: string
- container: ''
  name: BooleanValue
  type: string
- container: ''
  name: StringValue
  type: string
- container: ''
  name: Annotations
  type: string
- container: ''
  name: ServiceId
  type: string
- container: ''
  name: AccountId
  type: string
- container: ''
  name: TimeoutCount
  type: string
- container: ''
  name: ConnectionRefusedCount
  type: string
- container: ''
  name: HTTPCode4XXCount
  type: string
- container: ''
  name: HTTPCode5XXCount
  type: string
- container: ''
  name: UnknownHostCount
  type: string
- container: ''
  name: OtherCount
  type: string
- container: ''
  name: TraceIds
  type: string
- container: ''
  name: InsightsConfiguration
  type: string
- container: ''
  name: InsightsEnabled
  type: string
- container: ''
  name: NotificationsEnabled
  type: string
- container: ''
  name: GroupName
  type: string
- container: ''
  name: FilterExpression
  type: string
- container: ''
  name: GroupARN
  type: string
- container: ''
  name: SamplingRule
  type: string
- container: ''
  name: RuleARN
  type: string
- container: ''
  name: ResourceARN
  type: string
- container: ''
  name: Priority
  type: string
- container: ''
  name: FixedRate
  type: string
- container: ''
  name: ReservoirSize
  type: string
- container: ''
  name: ServiceName
  type: string
- container: ''
  name: ServiceType
  type: string
- container: ''
  name: Host
  type: string
- container: ''
  name: HTTPMethod
  type: string
- container: ''
  name: URLPath
  type: string
- container: ''
  name: Version
  type: string
- container: ''
  name: Attributes
  type: string
- container: ''
  name: CreatedAt
  type: string
- container: ''
  name: ModifiedAt
  type: string
- container: ''
  name: PolicyName
  type: string
- container: ''
  name: PolicyRevisionId
  type: string
- container: ''
  name: OkCount
  type: string
- container: ''
  name: TotalCount
  type: string
- container: ''
  name: TotalResponseTime
  type: string
- container: ''
  name: ReferenceId
  type: string
- container: ''
  name: SummaryStatistics
  type: string
- container: ''
  name: ResponseTimeHistogram
  type: string
- container: ''
  name: Aliases
  type: string
- container: ''
  name: EdgeType
  type: string
- container: ''
  name: ReceivedEventAgeHistogram
  type: string
- container: ''
  name: ThrottleCount
  type: string
- container: ''
  name: KeyId
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: ClientImpacting
  type: string
- container: ''
  name: Exceptions
  type: string
- container: ''
  name: Remote
  type: string
- container: ''
  name: EntityPath
  type: string
- container: ''
  name: Inferred
  type: string
- container: ''
  name: ForecastStatistics
  type: string
- container: ''
  name: FaultCountHigh
  type: string
- container: ''
  name: FaultCountLow
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: RootCauseServiceId
  type: string
- container: ''
  name: Categories
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: Summary
  type: string
- container: ''
  name: ClientRequestImpactStatistics
  type: string
- container: ''
  name: RootCauseServiceRequestImpactStatistics
  type: string
- container: ''
  name: TopAnomalousServices
  type: string
- container: ''
  name: States
  type: string
- container: ''
  name: SamplingStatisticsDocuments
  type: string
- container: ''
  name: EntitySelectorExpression
  type: string
- container: ''
  name: Period
  type: string
- container: ''
  name: SamplingStrategy
  type: string
- container: ''
  name: TimeRangeType
  type: string
- container: ''
  name: Sampling
  type: string
- container: ''
  name: Count
  type: string
- container: ''
  name: Http
  type: string
- container: ''
  name: HttpURL
  type: string
- container: ''
  name: HttpStatus
  type: string
- container: ''
  name: HttpMethod
  type: string
- container: ''
  name: UserAgent
  type: string
- container: ''
  name: ClientIp
  type: string
- container: ''
  name: FaultCount
  type: string
- container: ''
  name: EventTime
  type: string
- container: ''
  name: Edges
  type: string
- container: ''
  name: LastUpdateTime
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: PolicyDocument
  type: string
- container: ''
  name: BypassPolicyLockoutCheck
  type: string
- container: ''
  name: LastUpdatedTime
  type: string
- container: ''
  name: TelemetryRecords
  type: string
- container: ''
  name: EC2InstanceId
  type: string
- container: ''
  name: Hostname
  type: string
- container: ''
  name: TraceSegmentDocuments
  type: string
- container: ''
  name: ARN
  type: string
- container: ''
  name: Coverage
  type: string
- container: ''
  name: Message
  type: string
- container: ''
  name: SamplingRuleUpdate
  type: string
- container: ''
  name: ReservoirQuota
  type: string
- container: ''
  name: ReservoirQuotaTTL
  type: string
- container: ''
  name: Interval
  type: string
- container: ''
  name: Document
  type: string
- container: ''
  name: Root
  type: string
- container: ''
  name: DurationHistogram
  type: string
- container: ''
  name: EdgeSummaryStatistics
  type: string
- container: ''
  name: ServiceSummaryStatistics
  type: string
- container: ''
  name: ServiceForecastStatistics
  type: string
- container: ''
  name: Duration
  type: string
- container: ''
  name: LimitExceeded
  type: string
- container: ''
  name: Segments
  type: string
- container: ''
  name: ResponseTime
  type: string
- container: ''
  name: HasFault
  type: string
- container: ''
  name: HasError
  type: string
- container: ''
  name: HasThrottle
  type: string
- container: ''
  name: IsPartial
  type: string
- container: ''
  name: Users
  type: string
- container: ''
  name: ServiceIds
  type: string
- container: ''
  name: ResourceARNs
  type: string
- container: ''
  name: InstanceIds
  type: string
- container: ''
  name: AvailabilityZones
  type: string
- container: ''
  name: EntryPoint
  type: string
- container: ''
  name: FaultRootCauses
  type: string
- container: ''
  name: ErrorRootCauses
  type: string
- container: ''
  name: ResponseTimeRootCauses
  type: string
- container: ''
  name: Revision
  type: string
- container: ''
  name: MatchedEventTime
  type: string
- container: ''
  name: UserName
  type: string
- container: ''
  name: ErrorCode
  type: string
- container: ''
  name: TagKeys
  type: string
property_count: 164
provider_name: Amazon X-Ray
provider_slug: amazon-xray
slug: amazon-xray-context
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
- JSON-LD
- Linked Data
- Semantic Web
---

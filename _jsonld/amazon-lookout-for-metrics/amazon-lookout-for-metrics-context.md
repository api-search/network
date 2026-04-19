---
class_count: 117
classes:
- Action
- ActivateAnomalyDetectorRequest
- ActivateAnomalyDetectorResponse
- Alert
- AlertFilters
- AlertSummary
- AnomalyDetectorConfig
- AnomalyDetectorConfigSummary
- AnomalyDetectorDataQualityMetric
- AnomalyDetectorSummary
- AnomalyGroup
- AnomalyGroupStatistics
- AnomalyGroupSummary
- AnomalyGroupTimeSeries
- AnomalyGroupTimeSeriesFeedback
- AppFlowConfig
- AthenaSourceConfig
- AttributeValue
- AutoDetectionMetricSource
- AutoDetectionS3SourceConfig
- BackTestAnomalyDetectorRequest
- BackTestAnomalyDetectorResponse
- BackTestConfiguration
- CloudWatchConfig
- ContributionMatrix
- CreateAlertRequest
- CreateAlertResponse
- CreateAnomalyDetectorRequest
- CreateAnomalyDetectorResponse
- CreateMetricSetRequest
- CreateMetricSetResponse
- CsvFormatDescriptor
- DataQualityMetric
- DeactivateAnomalyDetectorRequest
- DeactivateAnomalyDetectorResponse
- DeleteAlertRequest
- DeleteAlertResponse
- DeleteAnomalyDetectorRequest
- DeleteAnomalyDetectorResponse
- DescribeAlertRequest
- DescribeAlertResponse
- DescribeAnomalyDetectionExecutionsRequest
- DescribeAnomalyDetectionExecutionsResponse
- DescribeAnomalyDetectorRequest
- DescribeAnomalyDetectorResponse
- DescribeMetricSetRequest
- DescribeMetricSetResponse
- DetectMetricSetConfigRequest
- DetectMetricSetConfigResponse
- DetectedCsvFormatDescriptor
- DetectedField
- DetectedFileFormatDescriptor
- DetectedJsonFormatDescriptor
- DetectedMetricSetConfig
- DetectedMetricSource
- DetectedS3SourceConfig
- DimensionContribution
- DimensionFilter
- DimensionNameValue
- DimensionValueContribution
- ExecutionStatus
- FileFormatDescriptor
- Filter
- GetAnomalyGroupRequest
- GetAnomalyGroupResponse
- GetDataQualityMetricsRequest
- GetDataQualityMetricsResponse
- GetFeedbackRequest
- GetFeedbackResponse
- GetSampleDataRequest
- GetSampleDataResponse
- InterMetricImpactDetails
- ItemizedMetricStats
- JsonFormatDescriptor
- LambdaConfiguration
- ListAlertsRequest
- ListAlertsResponse
- ListAnomalyDetectorsRequest
- ListAnomalyDetectorsResponse
- ListAnomalyGroupRelatedMetricsRequest
- ListAnomalyGroupRelatedMetricsResponse
- ListAnomalyGroupSummariesRequest
- ListAnomalyGroupSummariesResponse
- ListAnomalyGroupTimeSeriesRequest
- ListAnomalyGroupTimeSeriesResponse
- ListMetricSetsRequest
- ListMetricSetsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- Metric
- MetricLevelImpact
- MetricSetDataQualityMetric
- MetricSetDimensionFilter
- MetricSetSummary
- MetricSource
- PutFeedbackRequest
- PutFeedbackResponse
- RDSSourceConfig
- RedshiftSourceConfig
- S3SourceConfig
- SNSConfiguration
- SampleDataS3SourceConfig
- TagMap
- TagResourceRequest
- TagResourceResponse
- TimeSeries
- TimeSeriesFeedback
- TimestampColumn
- UntagResourceRequest
- UntagResourceResponse
- UpdateAlertRequest
- UpdateAlertResponse
- UpdateAnomalyDetectorRequest
- UpdateAnomalyDetectorResponse
- UpdateMetricSetRequest
- UpdateMetricSetResponse
- VpcConfiguration
context_file: json-ld/amazon-lookout-for-metrics-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-metrics/refs/heads/main/json-ld/amazon-lookout-for-metrics-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Lookout For Metrics from Amazon Lookout for Metrics.
layout: jsonld
name: Amazon Lookout For Metrics Context
namespaces:
- prefix: alm
  uri: https://alm.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AggregationFunction
  type: ''
- container: ''
  name: AlertArn
  type: ''
- container: ''
  name: AlertDescription
  type: ''
- container: ''
  name: AlertName
  type: ''
- container: ''
  name: AlertSensitivityThreshold
  type: ''
- container: ''
  name: AlertStatus
  type: ''
- container: ''
  name: AlertSummaryList
  type: ''
- container: ''
  name: AlertType
  type: ''
- container: ''
  name: AnomalyDetectorArn
  type: ''
- container: ''
  name: AnomalyDetectorDataQualityMetricList
  type: ''
- container: ''
  name: AnomalyDetectorDescription
  type: ''
- container: ''
  name: AnomalyDetectorFrequency
  type: ''
- container: ''
  name: AnomalyDetectorName
  type: ''
- container: ''
  name: AnomalyDetectorSummaryList
  type: ''
- container: ''
  name: AnomalyGroupId
  type: ''
- container: ''
  name: AnomalyGroupScore
  type: ''
- container: ''
  name: AnomalyGroupSummaryList
  type: ''
- container: ''
  name: B
  type: ''
- container: ''
  name: BS
  type: ''
- container: ''
  name: Charset
  type: ''
- container: ''
  name: ClusterIdentifier
  type: ''
- container: ''
  name: ColumnFormat
  type: ''
- container: ''
  name: ColumnName
  type: ''
- container: ''
  name: Confidence
  type: ''
- container: ''
  name: ContainsHeader
  type: ''
- container: ''
  name: ContributionPercentage
  type: ''
- container: ''
  name: ContributionScore
  type: ''
- container: ''
  name: CreationTime
  type: ''
- container: ''
  name: DBInstanceIdentifier
  type: ''
- container: ''
  name: DataCatalog
  type: ''
- container: ''
  name: DataQualityMetricList
  type: ''
- container: ''
  name: DatabaseHost
  type: ''
- container: ''
  name: DatabaseName
  type: ''
- container: ''
  name: DatabasePort
  type: ''
- container: ''
  name: Delimiter
  type: ''
- container: ''
  name: DimensionContributionList
  type: ''
- container: ''
  name: DimensionFilterList
  type: ''
- container: ''
  name: DimensionList
  type: ''
- container: ''
  name: DimensionName
  type: ''
- container: ''
  name: DimensionValue
  type: ''
- container: ''
  name: DimensionValueContributionList
  type: ''
- container: ''
  name: DimensionValueList
  type: ''
- container: ''
  name: EndTime
  type: ''
- container: ''
  name: EvaluationStartDate
  type: ''
- container: ''
  name: ExecutionList
  type: ''
- container: ''
  name: FailureReason
  type: ''
- container: ''
  name: FailureType
  type: ''
- container: ''
  name: FileCompression
  type: ''
- container: ''
  name: FilterList
  type: ''
- container: ''
  name: FilterOperation
  type: ''
- container: ''
  name: FlowName
  type: ''
- container: ''
  name: HeaderList
  type: ''
- container: ''
  name: HeaderValues
  type: ''
- container: ''
  name: HistoricalDataPathList
  type: ''
- container: ''
  name: InterMetricImpactList
  type: ''
- container: ''
  name: IsAnomaly
  type: ''
- container: ''
  name: ItemizedMetricStatsList
  type: ''
- container: ''
  name: KmsKeyArn
  type: ''
- container: ''
  name: LambdaArn
  type: ''
- container: ''
  name: LastModificationTime
  type: ''
- container: ''
  name: MaxResults
  type: ''
- container: ''
  name: Message
  type: ''
- container: ''
  name: MetricDescription
  type: ''
- container: ''
  name: MetricLevelImpactList
  type: ''
- container: ''
  name: MetricList
  type: ''
- container: ''
  name: MetricName
  type: ''
- container: ''
  name: MetricSetArn
  type: ''
- container: ''
  name: MetricSetDataQualityMetricList
  type: ''
- container: ''
  name: MetricSetDescription
  type: ''
- container: ''
  name: MetricSetFrequency
  type: ''
- container: ''
  name: MetricSetName
  type: ''
- container: ''
  name: MetricSetSummaryList
  type: ''
- container: ''
  name: MetricType
  type: ''
- container: ''
  name: MetricValue
  type: ''
- container: ''
  name: MetricValueList
  type: ''
- container: ''
  name: N
  type: ''
- container: ''
  name: NS
  type: ''
- container: ''
  name: Name
  type: ''
- container: ''
  name: Namespace
  type: ''
- container: ''
  name: NextToken
  type: ''
- container: ''
  name: NumTimeSeries
  type: ''
- container: ''
  name: OccurrenceCount
  type: ''
- container: ''
  name: Offset
  type: ''
- container: ''
  name: PrimaryMetricName
  type: ''
- container: ''
  name: QuoteSymbol
  type: ''
- container: ''
  name: RelatedColumnName
  type: ''
- container: ''
  name: RelationshipType
  type: ''
- container: ''
  name: RelationshipTypeFilter
  type: ''
- container: ''
  name: RoleArn
  type: ''
- container: ''
  name: RunBackTestMode
  type: ''
- container: ''
  name: S
  type: ''
- container: ''
  name: S3ResultsPath
  type: ''
- container: ''
  name: SS
  type: ''
- container: ''
  name: SampleRows
  type: ''
- container: ''
  name: SecretManagerArn
  type: ''
- container: ''
  name: SecurityGroupIdList
  type: ''
- container: ''
  name: SensitivityThreshold
  type: ''
- container: ''
  name: SnsFormat
  type: ''
- container: ''
  name: SnsTopicArn
  type: ''
- container: ''
  name: StartTime
  type: ''
- container: ''
  name: StartTimestamp
  type: ''
- container: ''
  name: Status
  type: ''
- container: ''
  name: SubnetIdList
  type: ''
- container: ''
  name: TableName
  type: ''
- container: ''
  name: Tags
  type: ''
- container: ''
  name: TemplatedPathList
  type: ''
- container: ''
  name: TimeSeriesId
  type: ''
- container: ''
  name: TimeSeriesList
  type: ''
- container: ''
  name: Timestamp
  type: ''
- container: ''
  name: TimestampList
  type: ''
- container: ''
  name: Timezone
  type: ''
- container: ''
  name: TotalCount
  type: ''
- container: ''
  name: Value
  type: ''
- container: ''
  name: WorkGroupName
  type: ''
property_count: 114
provider_name: Amazon Lookout for Metrics
provider_slug: amazon-lookout-for-metrics
slug: amazon-lookout-for-metrics-context
tags:
- Anomaly Detection
- AWS
- Business Intelligence
- Machine Learning
- Metrics
- Monitoring
- JSON-LD
- Linked Data
- Semantic Web
---

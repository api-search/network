---
class_count: 122
classes:
- DeleteScheduleRequest
- S3TableOutputOptions
- UpdateScheduleRequest
- BatchDeleteRecipeVersionRequest
- ListSchedulesResponse
- ParameterMap
- ListRecipesResponse
- UpdateRecipeRequest
- TagResourceRequest
- ListJobsResponse
- CreateProfileJobRequest
- RecipeAction
- ValidationConfiguration
- StartJobRunResponse
- ListDatasetsResponse
- UpdateRecipeJobResponse
- CreateRulesetRequest
- ListJobRunsRequest
- CsvOutputOptions
- Output
- DeleteDatasetRequest
- StartProjectSessionResponse
- StopJobRunRequest
- CreateDatasetResponse
- DescribeProjectRequest
- DescribeJobRunRequest
- DescribeRulesetResponse
- StartProjectSessionRequest
- ColumnSelector
- PublishRecipeResponse
- ListRecipeVersionsResponse
- DeleteRecipeVersionRequest
- PathParametersMap
- DeleteJobRequest
- CreateRecipeJobRequest
- UpdateProfileJobResponse
- UpdateScheduleResponse
- ListJobRunsResponse
- Recipe
- CsvOptions
- DescribeJobResponse
- UpdateProjectResponse
- DescribeDatasetRequest
- JsonOptions
- DeleteProjectResponse
- UpdateRulesetRequest
- StatisticsConfiguration
- DataCatalogOutput
- DeleteScheduleResponse
- StopJobRunResponse
- CreateRulesetResponse
- UpdateRecipeJobRequest
- SendProjectSessionActionResponse
- DescribeDatasetResponse
- DescribeRecipeResponse
- RulesetItem
- DescribeRecipeRequest
- StartJobRunRequest
- ListProjectsRequest
- DeleteProjectRequest
- ListRulesetsResponse
- DatabaseTableOutputOptions
- PublishRecipeRequest
- FilterExpression
- Schedule
- DescribeScheduleRequest
- TagResourceResponse
- OutputFormatOptions
- ColumnStatisticsConfiguration
- DatasetParameter
- ListTagsForResourceRequest
- UpdateRulesetResponse
- CreateRecipeResponse
- ListRecipeVersionsRequest
- DescribeJobRunResponse
- RecipeVersionErrorDetail
- UpdateProjectRequest
- CreateProfileJobResponse
- DeleteRulesetResponse
- UntagResourceRequest
- Dataset
- CreateProjectResponse
- CreateDatasetRequest
- DeleteRecipeVersionResponse
- ListRulesetsRequest
- ConditionExpression
- DeleteRulesetRequest
- BatchDeleteRecipeVersionResponse
- S3Location
- DescribeJobRequest
- CreateRecipeJobResponse
- CreateScheduleResponse
- Rule
- DeleteJobResponse
- JobRun
- ListRecipesRequest
- ListProjectsResponse
- TagMap
- CreateScheduleRequest
- DatabaseOutput
- StatisticOverride
- DescribeScheduleResponse
- ListTagsForResourceResponse
- UpdateRecipeResponse
- ListJobsRequest
- UpdateDatasetResponse
- SendProjectSessionActionRequest
- CreateProjectRequest
- CreateRecipeRequest
- DeleteDatasetResponse
- UpdateProfileJobRequest
- UntagResourceResponse
- ExcelOptions
- ListSchedulesRequest
- DescribeRulesetRequest
- Project
- ListDatasetsRequest
- UpdateDatasetRequest
- Job
- DescribeProjectResponse
- Description
- Name
context_file: json-ld/amazon-glue-databrew-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-glue-databrew/refs/heads/main/json-ld/amazon-glue-databrew-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Glue Databrew from Amazon Glue DataBrew.
layout: jsonld
name: Amazon Glue Databrew Context
namespaces:
- prefix: databrew
  uri: https://aws.amazon.com/glue/databrew/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: RecipeStep
  type: string
- container: ''
  name: EntityDetectorConfiguration
  type: string
- container: ''
  name: PathOptions
  type: string
- container: ''
  name: Input
  type: string
- container: ''
  name: FilesLimit
  type: string
- container: ''
  name: ViewFrame
  type: string
- container: ''
  name: JobSample
  type: string
- container: ''
  name: Metadata
  type: string
- container: ''
  name: RecipeReference
  type: string
- container: ''
  name: ProfileConfiguration
  type: string
- container: ''
  name: DatabaseInputDefinition
  type: string
- container: ''
  name: AllowedStatistics
  type: string
- container: ''
  name: DataCatalogInputDefinition
  type: string
- container: ''
  name: ValuesMap
  type: string
- container: ''
  name: FormatOptions
  type: string
- container: ''
  name: DatetimeOptions
  type: string
- container: ''
  name: Sample
  type: string
- container: ''
  name: Threshold
  type: string
- container: ''
  name: Location
  type: string
- container: ''
  name: JobNames
  type: string
- container: ''
  name: CronExpression
  type: string
- container: ''
  name: RecipeVersions
  type: string
- container: ''
  name: Schedules
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: Recipes
  type: string
- container: ''
  name: Steps
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: Jobs
  type: string
- container: ''
  name: DatasetName
  type: string
- container: ''
  name: EncryptionKeyArn
  type: string
- container: ''
  name: EncryptionMode
  type: string
- container: ''
  name: LogSubscription
  type: string
- container: ''
  name: MaxCapacity
  type: string
- container: ''
  name: MaxRetries
  type: string
- container: ''
  name: OutputLocation
  type: string
- container: ''
  name: Configuration
  type: string
- container: ''
  name: ValidationConfigurations
  type: string
- container: ''
  name: RoleArn
  type: string
- container: ''
  name: Timeout
  type: string
- container: ''
  name: Action
  type: string
- container: ''
  name: ConditionExpressions
  type: string
- container: ''
  name: Operation
  type: string
- container: ''
  name: Parameters
  type: string
- container: ''
  name: RulesetArn
  type: string
- container: ''
  name: ValidationMode
  type: string
- container: ''
  name: RunId
  type: string
- container: ''
  name: Datasets
  type: string
- container: ''
  name: TargetArn
  type: string
- container: ''
  name: Rules
  type: string
- container: ''
  name: Delimiter
  type: string
- container: ''
  name: CompressionFormat
  type: string
- container: ''
  name: Format
  type: string
- container: ''
  name: PartitionColumns
  type: string
- container: ''
  name: Overwrite
  type: string
- container: ''
  name: MaxOutputFiles
  type: string
- container: ''
  name: ClientSessionId
  type: string
- container: ''
  name: EntityTypes
  type: string
- container: ''
  name: CreateDate
  type: string
- container: ''
  name: CreatedBy
  type: string
- container: ''
  name: LastModifiedBy
  type: string
- container: ''
  name: LastModifiedDate
  type: string
- container: ''
  name: ResourceArn
  type: string
- container: ''
  name: AssumeControl
  type: string
- container: ''
  name: Regex
  type: string
- container: ''
  name: LastModifiedDateCondition
  type: string
- container: ''
  name: Outputs
  type: string
- container: ''
  name: DataCatalogOutputs
  type: string
- container: ''
  name: DatabaseOutputs
  type: string
- container: ''
  name: ProjectName
  type: string
- container: ''
  name: S3InputDefinition
  type: string
- container: ''
  name: JobRuns
  type: string
- container: ''
  name: PublishedBy
  type: string
- container: ''
  name: PublishedDate
  type: string
- container: ''
  name: RecipeVersion
  type: string
- container: ''
  name: HeaderRow
  type: string
- container: ''
  name: MaxFiles
  type: string
- container: ''
  name: OrderedBy
  type: string
- container: ''
  name: Order
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: MultiLine
  type: string
- container: ''
  name: IncludedStatistics
  type: string
- container: ''
  name: Overrides
  type: string
- container: ''
  name: StartColumnIndex
  type: string
- container: ''
  name: ColumnRange
  type: string
- container: ''
  name: HiddenColumns
  type: string
- container: ''
  name: StartRowIndex
  type: string
- container: ''
  name: RowRange
  type: string
- container: ''
  name: Analytics
  type: string
- container: ''
  name: CatalogId
  type: string
- container: ''
  name: DatabaseName
  type: string
- container: ''
  name: TableName
  type: string
- container: ''
  name: S3Options
  type: string
- container: ''
  name: DatabaseOptions
  type: string
- container: ''
  name: Mode
  type: string
- container: ''
  name: Size
  type: string
- container: ''
  name: Result
  type: string
- container: ''
  name: ActionId
  type: string
- container: ''
  name: Source
  type: string
- container: ''
  name: AccountId
  type: string
- container: ''
  name: RuleCount
  type: string
- container: ''
  name: SourceArn
  type: string
- container: ''
  name: Rulesets
  type: string
- container: ''
  name: TempDirectory
  type: string
- container: ''
  name: DatasetStatisticsConfiguration
  type: string
- container: ''
  name: ProfileColumns
  type: string
- container: ''
  name: ColumnStatisticsConfigurations
  type: string
- container: ''
  name: Expression
  type: string
- container: ''
  name: Csv
  type: string
- container: ''
  name: Selectors
  type: string
- container: ''
  name: Statistics
  type: string
- container: ''
  name: CreateColumn
  type: string
- container: ''
  name: Filter
  type: string
- container: ''
  name: GlueConnectionName
  type: string
- container: ''
  name: DatabaseTableName
  type: string
- container: ''
  name: QueryString
  type: string
- container: ''
  name: Attempt
  type: string
- container: ''
  name: CompletedOn
  type: string
- container: ''
  name: ErrorMessage
  type: string
- container: ''
  name: ExecutionTime
  type: string
- container: ''
  name: JobName
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: LogGroupName
  type: string
- container: ''
  name: StartedBy
  type: string
- container: ''
  name: StartedOn
  type: string
- container: ''
  name: ErrorCode
  type: string
- container: ''
  name: Condition
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: TargetColumn
  type: string
- container: ''
  name: Json
  type: string
- container: ''
  name: Excel
  type: string
- container: ''
  name: Errors
  type: string
- container: ''
  name: Bucket
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: BucketOwner
  type: string
- container: ''
  name: TimezoneOffset
  type: string
- container: ''
  name: LocaleCode
  type: string
- container: ''
  name: Disabled
  type: string
- container: ''
  name: CheckExpression
  type: string
- container: ''
  name: SubstitutionMap
  type: string
- container: ''
  name: ColumnSelectors
  type: string
- container: ''
  name: Projects
  type: string
- container: ''
  name: DatabaseOutputMode
  type: string
- container: ''
  name: Statistic
  type: string
- container: ''
  name: Unit
  type: string
- container: ''
  name: Preview
  type: string
- container: ''
  name: StepIndex
  type: string
- container: ''
  name: RecipeName
  type: string
- container: ''
  name: SheetNames
  type: string
- container: ''
  name: SheetIndexes
  type: string
- container: ''
  name: OpenedBy
  type: string
- container: ''
  name: OpenDate
  type: string
- container: ''
  name: SessionStatus
  type: string
property_count: 152
provider_name: Amazon Glue DataBrew
provider_slug: amazon-glue-databrew
slug: amazon-glue-databrew-context
tags:
- AWS
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
- JSON-LD
- Linked Data
- Semantic Web
---

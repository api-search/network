---
class_count: 83
classes:
- AwsVpcConfiguration
- BatchArrayProperties
- BatchContainerOverrides
- BatchEnvironmentVariable
- BatchJobDependency
- BatchParametersMap
- BatchResourceRequirement
- BatchRetryStrategy
- CapacityProviderStrategyItem
- CreatePipeRequest
- CreatePipeResponse
- DeadLetterConfig
- DeletePipeRequest
- DeletePipeResponse
- DescribePipeRequest
- DescribePipeResponse
- EcsContainerOverride
- EcsEnvironmentFile
- EcsEnvironmentVariable
- name
- EcsEphemeralStorage
- EcsInferenceAcceleratorOverride
- EcsResourceRequirement
- EcsTaskOverride
- FilterCriteria
- Filter
- HeaderParametersMap
- ListPipesRequest
- ListPipesResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- MQBrokerAccessCredentials
- MSKAccessCredentials
- NetworkConfiguration
- PipeEnrichmentHttpParameters
- PipeEnrichmentParameters
- Pipe
- PipeSourceActiveMQBrokerParameters
- PipeSourceDynamoDBStreamParameters
- PipeSourceKinesisStreamParameters
- PipeSourceManagedStreamingKafkaParameters
- PipeSourceParameters
- PipeSourceRabbitMQBrokerParameters
- PipeSourceSelfManagedKafkaParameters
- PipeSourceSqsQueueParameters
- PipeTargetBatchJobParameters
- PipeTargetCloudWatchLogsParameters
- PipeTargetEcsTaskParameters
- PlacementStrategy
- PipeTargetEventBridgeEventBusParameters
- PipeTargetHttpParameters
- PipeTargetKinesisStreamParameters
- PipeTargetLambdaFunctionParameters
- PipeTargetParameters
- PipeTargetRedshiftDataParameters
- PipeTargetSageMakerPipelineParameters
- PipeTargetSqsQueueParameters
- PipeTargetStateMachineParameters
- PlacementConstraint
- QueryStringParametersMap
- SageMakerPipelineParameter
- SelfManagedKafkaAccessConfigurationCredentials
- SelfManagedKafkaAccessConfigurationVpc
- StartPipeRequest
- StartPipeResponse
- StopPipeRequest
- StopPipeResponse
- TagMap
- TagResourceRequest
- TagResourceResponse
- Tag
- UntagResourceRequest
- UntagResourceResponse
- UpdatePipeRequest
- UpdatePipeResponse
- UpdatePipeSourceActiveMQBrokerParameters
- UpdatePipeSourceDynamoDBStreamParameters
- UpdatePipeSourceKinesisStreamParameters
- UpdatePipeSourceManagedStreamingKafkaParameters
- UpdatePipeSourceParameters
- UpdatePipeSourceRabbitMQBrokerParameters
- UpdatePipeSourceSelfManagedKafkaParameters
- UpdatePipeSourceSqsQueueParameters
context_file: json-ld/amazon-eventbridge-pipes-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-eventbridge-pipes/refs/heads/main/json-ld/amazon-eventbridge-pipes-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Eventbridge Pipes from Amazon EventBridge Pipes.
layout: jsonld
name: Amazon Eventbridge Pipes Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AssignPublicIp
  type: string
- container: ''
  name: SecurityGroups
  type: string
- container: ''
  name: Subnets
  type: string
- container: ''
  name: Size
  type: string
- container: ''
  name: Command
  type: string
- container: ''
  name: Environment
  type: string
- container: ''
  name: InstanceType
  type: string
- container: ''
  name: ResourceRequirements
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: JobId
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: Attempts
  type: string
- container: ''
  name: base
  type: string
- container: ''
  name: capacityProvider
  type: string
- container: ''
  name: weight
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: DesiredState
  type: string
- container: ''
  name: Enrichment
  type: string
- container: ''
  name: EnrichmentParameters
  type: string
- container: ''
  name: RoleArn
  type: string
- container: ''
  name: Source
  type: string
- container: ''
  name: SourceParameters
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: Target
  type: string
- container: ''
  name: TargetParameters
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: CreationTime
  type: string
- container: ''
  name: CurrentState
  type: string
- container: ''
  name: LastModifiedTime
  type: string
- container: ''
  name: StateReason
  type: string
- container: ''
  name: Cpu
  type: string
- container: ''
  name: EnvironmentFiles
  type: string
- container: ''
  name: Memory
  type: string
- container: ''
  name: MemoryReservation
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: sizeInGiB
  type: string
- container: ''
  name: deviceName
  type: string
- container: ''
  name: deviceType
  type: string
- container: ''
  name: ContainerOverrides
  type: string
- container: ''
  name: EphemeralStorage
  type: string
- container: ''
  name: ExecutionRoleArn
  type: string
- container: ''
  name: InferenceAcceleratorOverrides
  type: string
- container: ''
  name: TaskRoleArn
  type: string
- container: ''
  name: Filters
  type: string
- container: ''
  name: Pattern
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: Pipes
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: BasicAuth
  type: string
- container: ''
  name: ClientCertificateTlsAuth
  type: string
- container: ''
  name: SaslScram512Auth
  type: string
- container: ''
  name: awsvpcConfiguration
  type: string
- container: ''
  name: HeaderParameters
  type: string
- container: ''
  name: PathParameterValues
  type: string
- container: ''
  name: QueryStringParameters
  type: string
- container: ''
  name: HttpParameters
  type: string
- container: ''
  name: InputTemplate
  type: string
- container: ''
  name: BatchSize
  type: string
- container: ''
  name: Credentials
  type: string
- container: ''
  name: MaximumBatchingWindowInSeconds
  type: string
- container: ''
  name: QueueName
  type: string
- container: ''
  name: MaximumRecordAgeInSeconds
  type: string
- container: ''
  name: MaximumRetryAttempts
  type: string
- container: ''
  name: OnPartialBatchItemFailure
  type: string
- container: ''
  name: ParallelizationFactor
  type: string
- container: ''
  name: StartingPosition
  type: string
- container: ''
  name: StartingPositionTimestamp
  type: string
- container: ''
  name: ConsumerGroupID
  type: string
- container: ''
  name: TopicName
  type: string
- container: ''
  name: ActiveMQBrokerParameters
  type: string
- container: ''
  name: DynamoDBStreamParameters
  type: string
- container: ''
  name: KinesisStreamParameters
  type: string
- container: ''
  name: ManagedStreamingKafkaParameters
  type: string
- container: ''
  name: RabbitMQBrokerParameters
  type: string
- container: ''
  name: SelfManagedKafkaParameters
  type: string
- container: ''
  name: SqsQueueParameters
  type: string
- container: ''
  name: VirtualHost
  type: string
- container: ''
  name: AdditionalBootstrapServers
  type: string
- container: ''
  name: ServerRootCaCertificate
  type: string
- container: ''
  name: Vpc
  type: string
- container: ''
  name: ArrayProperties
  type: string
- container: ''
  name: DependsOn
  type: string
- container: ''
  name: JobDefinition
  type: string
- container: ''
  name: JobName
  type: string
- container: ''
  name: Parameters
  type: string
- container: ''
  name: RetryStrategy
  type: string
- container: ''
  name: LogStreamName
  type: string
- container: ''
  name: Timestamp
  type: string
- container: ''
  name: CapacityProviderStrategy
  type: string
- container: ''
  name: EnableECSManagedTags
  type: string
- container: ''
  name: EnableExecuteCommand
  type: string
- container: ''
  name: Group
  type: string
- container: ''
  name: LaunchType
  type: string
- container: ''
  name: Overrides
  type: string
- container: ''
  name: PlacementConstraints
  type: string
- container: ''
  name: PlatformVersion
  type: string
- container: ''
  name: PropagateTags
  type: string
- container: ''
  name: ReferenceId
  type: string
- container: ''
  name: TaskCount
  type: string
- container: ''
  name: TaskDefinitionArn
  type: string
- container: ''
  name: DetailType
  type: string
- container: ''
  name: EndpointId
  type: string
- container: ''
  name: Resources
  type: string
- container: ''
  name: Time
  type: string
- container: ''
  name: PartitionKey
  type: string
- container: ''
  name: InvocationType
  type: string
- container: ''
  name: BatchJobParameters
  type: string
- container: ''
  name: CloudWatchLogsParameters
  type: string
- container: ''
  name: EcsTaskParameters
  type: string
- container: ''
  name: EventBridgeEventBusParameters
  type: string
- container: ''
  name: LambdaFunctionParameters
  type: string
- container: ''
  name: RedshiftDataParameters
  type: string
- container: ''
  name: SageMakerPipelineParameters
  type: string
- container: ''
  name: StepFunctionStateMachineParameters
  type: string
- container: ''
  name: Database
  type: string
- container: ''
  name: DbUser
  type: string
- container: ''
  name: SecretManagerArn
  type: string
- container: ''
  name: Sqls
  type: string
- container: ''
  name: StatementName
  type: string
- container: ''
  name: WithEvent
  type: string
- container: ''
  name: PipelineParameterList
  type: string
- container: ''
  name: MessageDeduplicationId
  type: string
- container: ''
  name: MessageGroupId
  type: string
- container: ''
  name: expression
  type: string
- container: ''
  name: field
  type: string
- container: ''
  name: SaslScram256Auth
  type: string
- container: ''
  name: SecurityGroup
  type: string
- container: ''
  name: Key
  type: string
property_count: 130
provider_name: Amazon EventBridge Pipes
provider_slug: amazon-eventbridge-pipes
slug: amazon-eventbridge-pipes-context
tags:
- Amazon Web Services
- AWS
- Event-Driven
- Integration
- Messaging
- Serverless
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 48
classes:
- AcceleratorCountRequest
- AcceleratorTotalMemoryMiBRequest
- ActivitiesType
- Activity
- ActivityType
- Alarm
- AttachInstancesQuery
- AttachLoadBalancerTargetGroupsResultType
- AttachLoadBalancerTargetGroupsType
- AttachLoadBalancersResultType
- AttachLoadBalancersType
- AttachTrafficSourcesResultType
- AttachTrafficSourcesType
- AutoScalingGroup
- AutoScalingGroupNamesType
- AutoScalingGroupsType
- AutoScalingInstanceDetails
- AutoScalingInstancesType
- BaselineEbsBandwidthMbpsRequest
- BatchDeleteScheduledActionAnswer
- BatchDeleteScheduledActionType
- BatchPutScheduledUpdateGroupActionAnswer
- BatchPutScheduledUpdateGroupActionType
- BlockDeviceMapping
- CancelInstanceRefreshAnswer
- CancelInstanceRefreshType
- CapacityForecast
- CompleteLifecycleActionAnswer
- CompleteLifecycleActionType
- CreateAutoScalingGroupType
- CreateLaunchConfigurationType
- CreateOrUpdateTagsType
- DeleteAutoScalingGroupType
- DeleteLifecycleHookAnswer
- DeleteLifecycleHookType
- DeleteNotificationConfigurationType
- DeletePolicyType
- DeleteScheduledActionType
- DeleteTagsType
- DeleteWarmPoolAnswer
- DeleteWarmPoolType
- DescribeAccountLimitsAnswer
- DescribeAdjustmentTypesAnswer
- DescribeAutoScalingInstancesType
- DescribeAutoScalingNotificationTypesAnswer
- DescribeInstanceRefreshesAnswer
- DescribeInstanceRefreshesType
- DescribeLifecycleHookTypesAnswer
context_file: json-ld/amazon-ec2-auto-scaling-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-ec2-auto-scaling/refs/heads/main/json-ld/amazon-ec2-auto-scaling-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Ec2 Auto Scaling from Amazon EC2 Auto Scaling.
layout: jsonld
name: Amazon Ec2 Auto Scaling Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: pan
  uri: https://aws.amazon.com/schema/
properties:
- container: ''
  name: AdjustmentType
  type: string
- container: ''
  name: CustomizedMetricSpecification
  type: string
- container: ''
  name: MetricSpecifications
  type: string
- container: ''
  name: Mode
  type: string
- container: ''
  name: SchedulingBufferTime
  type: string
- container: ''
  name: MaxCapacityBreachBehavior
  type: string
- container: ''
  name: MaxCapacityBuffer
  type: string
- container: ''
  name: LifecycleHookName
  type: string
- container: ''
  name: LifecycleTransition
  type: string
- container: ''
  name: NotificationMetadata
  type: string
- container: ''
  name: HeartbeatTimeout
  type: string
- container: ''
  name: DefaultResult
  type: string
- container: ''
  name: NotificationTargetARN
  type: string
- container: ''
  name: RoleARN
  type: string
- container: ''
  name: PolicyARN
  type: string
- container: ''
  name: Alarms
  type: string
- container: ''
  name: AutoScalingGroupName
  type: string
- container: ''
  name: PolicyName
  type: string
- container: ''
  name: PercentageComplete
  type: string
- container: ''
  name: InstancesToUpdate
  type: string
- container: ''
  name: MetricIntervalLowerBound
  type: string
- container: ''
  name: MetricIntervalUpperBound
  type: string
- container: ''
  name: ScalingAdjustment
  type: string
- container: ''
  name: MetricDataQueries
  type: string
- container: ''
  name: LoadBalancers
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: PolicyNames
  type: string
- container: ''
  name: PolicyTypes
  type: string
- container: ''
  name: MaxRecords
  type: string
- container: ''
  name: AdjustmentTypes
  type: string
- container: ''
  name: Min
  type: string
- container: ''
  name: Max
  type: string
- container: ''
  name: Metrics
  type: string
- container: ''
  name: TrafficSourceType
  type: string
- container: ''
  name: MetricName
  type: string
- container: ''
  name: Namespace
  type: string
- container: ''
  name: Dimensions
  type: string
- container: ''
  name: Statistic
  type: string
- container: ''
  name: Unit
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: Activities
  type: string
- container: ''
  name: LaunchTemplate
  type: string
- container: ''
  name: InstancesDistribution
  type: string
- container: ''
  name: Granularity
  type: string
- container: ''
  name: LifecycleHookNames
  type: string
- container: ''
  name: LaunchConfigurations
  type: string
- container: ''
  name: InstanceId
  type: string
- container: ''
  name: ShouldDecrementDesiredCapacity
  type: string
- container: ''
  name: ScheduledUpdateGroupActions
  type: string
- container: ''
  name: MinHealthyPercentage
  type: string
- container: ''
  name: InstanceWarmup
  type: string
- container: ''
  name: CheckpointPercentages
  type: string
- container: ''
  name: CheckpointDelay
  type: string
- container: ''
  name: SkipMatching
  type: string
- container: ''
  name: AutoRollback
  type: string
- container: ''
  name: ScaleInProtectedInstances
  type: string
- container: ''
  name: StandbyInstances
  type: string
- container: ''
  name: Metric
  type: string
- container: ''
  name: Stat
  type: string
- container: ''
  name: AutoScalingInstances
  type: string
- container: ''
  name: InstanceType
  type: string
- container: ''
  name: WeightedCapacity
  type: string
- container: ''
  name: LaunchTemplateSpecification
  type: string
- container: ''
  name: InstanceRequirements
  type: string
- container: ''
  name: LoadBalancerName
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: LoadBalancerTargetGroupARN
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: Strategy
  type: string
- container: ''
  name: DesiredConfiguration
  type: string
- container: ''
  name: Preferences
  type: string
- container: ''
  name: Timestamps
  type: string
- container: ''
  name: Values
  type: string
- container: ''
  name: InstanceRefreshId
  type: string
- container: ''
  name: TrafficSource
  type: string
- container: ''
  name: Identifier
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: TopicARN
  type: string
- container: ''
  name: ScheduledActionName
  type: string
- container: ''
  name: Time
  type: string
- container: ''
  name: StartTime
  type: string
- container: ''
  name: EndTime
  type: string
- container: ''
  name: Recurrence
  type: string
- container: ''
  name: MinSize
  type: string
- container: ''
  name: MaxSize
  type: string
- container: ''
  name: DesiredCapacity
  type: string
- container: ''
  name: TimeZone
  type: string
- container: ''
  name: OnDemandAllocationStrategy
  type: string
- container: ''
  name: OnDemandBaseCapacity
  type: string
- container: ''
  name: OnDemandPercentageAboveBaseCapacity
  type: string
- container: ''
  name: SpotAllocationStrategy
  type: string
- container: ''
  name: SpotInstancePools
  type: string
- container: ''
  name: SpotMaxPrice
  type: string
- container: ''
  name: LaunchConfigurationName
  type: string
- container: ''
  name: MixedInstancesPolicy
  type: string
- container: ''
  name: DefaultCooldown
  type: string
- container: ''
  name: AvailabilityZones
  type: string
- container: ''
  name: HealthCheckType
  type: string
- container: ''
  name: HealthCheckGracePeriod
  type: string
- container: ''
  name: PlacementGroup
  type: string
- container: ''
  name: VPCZoneIdentifier
  type: string
- container: ''
  name: TerminationPolicies
  type: string
- container: ''
  name: NewInstancesProtectedFromScaleIn
  type: string
- container: ''
  name: ServiceLinkedRoleARN
  type: string
- container: ''
  name: MaxInstanceLifetime
  type: string
- container: ''
  name: CapacityRebalance
  type: string
- container: ''
  name: Context
  type: string
- container: ''
  name: DesiredCapacityType
  type: string
- container: ''
  name: DefaultInstanceWarmup
  type: string
- container: ''
  name: LoadBalancerNames
  type: string
- container: ''
  name: FailedScheduledActions
  type: string
- container: ''
  name: VirtualName
  type: string
- container: ''
  name: DeviceName
  type: string
- container: ''
  name: Ebs
  type: string
- container: ''
  name: NoDevice
  type: string
- container: ''
  name: Enabled
  type: string
- container: ''
  name: ScheduledActionARN
  type: string
- container: ''
  name: LifecycleHookTypes
  type: string
- container: ''
  name: InstanceIds
  type: string
- container: ''
  name: WarmPoolConfiguration
  type: string
- container: ''
  name: Instances
  type: string
- container: ''
  name: FailedScheduledUpdateGroupActions
  type: string
- container: ''
  name: MetricSpecification
  type: string
- container: ''
  name: LoadBalancerTargetGroups
  type: string
- container: ''
  name: PolicyType
  type: string
- container: ''
  name: MinAdjustmentStep
  type: string
- container: ''
  name: MinAdjustmentMagnitude
  type: string
- container: ''
  name: Cooldown
  type: string
- container: ''
  name: MetricAggregationType
  type: string
- container: ''
  name: StepAdjustments
  type: string
- container: ''
  name: EstimatedInstanceWarmup
  type: string
- container: ''
  name: TargetTrackingConfiguration
  type: string
- container: ''
  name: PredictiveScalingConfiguration
  type: string
- container: ''
  name: PredefinedMetricSpecification
  type: string
- container: ''
  name: TargetValue
  type: string
- container: ''
  name: DisableScaleIn
  type: string
- container: ''
  name: Overrides
  type: string
- container: ''
  name: PredefinedMetricType
  type: string
- container: ''
  name: ResourceLabel
  type: string
- container: ''
  name: ReuseOnScaleIn
  type: string
- container: ''
  name: ResourceId
  type: string
- container: ''
  name: ResourceType
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: PropagateAtLaunch
  type: string
- container: ''
  name: LaunchConfigurationARN
  type: string
- container: ''
  name: ImageId
  type: string
- container: ''
  name: KeyName
  type: string
- container: ''
  name: SecurityGroups
  type: string
- container: ''
  name: ClassicLinkVPCId
  type: string
- container: ''
  name: ClassicLinkVPCSecurityGroups
  type: string
- container: ''
  name: UserData
  type: string
- container: ''
  name: KernelId
  type: string
- container: ''
  name: RamdiskId
  type: string
- container: ''
  name: BlockDeviceMappings
  type: string
- container: ''
  name: InstanceMonitoring
  type: string
- container: ''
  name: SpotPrice
  type: string
- container: ''
  name: IamInstanceProfile
  type: string
- container: ''
  name: CreatedTime
  type: string
- container: ''
  name: EbsOptimized
  type: string
- container: ''
  name: AssociatePublicIpAddress
  type: string
- container: ''
  name: PlacementTenancy
  type: string
- container: ''
  name: MetadataOptions
  type: string
- container: ''
  name: ScheduledActionNames
  type: string
- container: ''
  name: LifecycleActionToken
  type: string
- container: ''
  name: LifecycleActionResult
  type: string
- container: ''
  name: ActivityIds
  type: string
- container: ''
  name: IncludeDeletedGroups
  type: string
- container: ''
  name: TrafficSources
  type: string
- container: ''
  name: RollbackReason
  type: string
- container: ''
  name: RollbackStartTime
  type: string
- container: ''
  name: PercentageCompleteOnRollback
  type: string
- container: ''
  name: InstancesToUpdateOnRollback
  type: string
- container: ''
  name: ProgressDetailsOnRollback
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: StatusReason
  type: string
- container: ''
  name: ProgressDetails
  type: string
- container: ''
  name: RollbackDetails
  type: string
- container: ''
  name: InstanceRefreshes
  type: string
- container: ''
  name: TargetGroupARNs
  type: string
- container: ''
  name: ErrorCode
  type: string
- container: ''
  name: ErrorMessage
  type: string
- container: ''
  name: AutoScalingGroupARN
  type: string
- container: ''
  name: PredictedCapacity
  type: string
- container: ''
  name: SuspendedProcesses
  type: string
- container: ''
  name: EnabledMetrics
  type: string
- container: ''
  name: WarmPoolSize
  type: string
- container: ''
  name: LaunchTemplateId
  type: string
- container: ''
  name: LaunchTemplateName
  type: string
- container: ''
  name: Version
  type: string
- container: ''
  name: Processes
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: Expression
  type: string
- container: ''
  name: MetricStat
  type: string
- container: ''
  name: Label
  type: string
- container: ''
  name: ReturnData
  type: string
- container: ''
  name: HonorCooldown
  type: string
- container: ''
  name: MetricValue
  type: string
- container: ''
  name: BreachThreshold
  type: string
- container: ''
  name: LivePoolProgress
  type: string
property_count: 200
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
slug: amazon-ec2-auto-scaling-context
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
- JSON-LD
- Linked Data
- Semantic Web
---

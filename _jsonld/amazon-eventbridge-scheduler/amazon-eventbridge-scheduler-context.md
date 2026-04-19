---
class_count: 44
classes:
- AwsVpcConfiguration
- CapacityProviderStrategyItem
- CreateScheduleGroupInput
- CreateScheduleGroupOutput
- CreateScheduleInput
- FlexibleTimeWindow
- Target
- CreateScheduleOutput
- DeadLetterConfig
- DeleteScheduleGroupInput
- DeleteScheduleGroupOutput
- DeleteScheduleInput
- DeleteScheduleOutput
- EcsParameters
- NetworkConfiguration
- PlacementStrategy
- EventBridgeParameters
- GetScheduleGroupInput
- GetScheduleGroupOutput
- GetScheduleInput
- GetScheduleOutput
- KinesisParameters
- ListScheduleGroupsInput
- ListScheduleGroupsOutput
- ListSchedulesInput
- ListSchedulesOutput
- ListTagsForResourceInput
- ListTagsForResourceOutput
- PlacementConstraint
- RetryPolicy
- SageMakerPipelineParameter
- SageMakerPipelineParameters
- ScheduleGroupSummary
- ScheduleSummary
- SqsParameters
- TagMap
- TagResourceInput
- TagResourceOutput
- Tag
- TargetSummary
- UntagResourceInput
- UntagResourceOutput
- UpdateScheduleInput
- UpdateScheduleOutput
context_file: json-ld/amazon-eventbridge-scheduler-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-eventbridge-scheduler/refs/heads/main/json-ld/amazon-eventbridge-scheduler-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Eventbridge Scheduler from Amazon EventBridge Scheduler.
layout: jsonld
name: Amazon Eventbridge Scheduler Context
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
  name: base
  type: string
- container: ''
  name: capacityProvider
  type: string
- container: ''
  name: weight
  type: string
- container: ''
  name: ClientToken
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: ScheduleGroupArn
  type: string
- container: ''
  name: ActionAfterCompletion
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: EndDate
  type: string
- container: ''
  name: GroupName
  type: string
- container: ''
  name: KmsKeyArn
  type: string
- container: ''
  name: ScheduleExpression
  type: string
- container: ''
  name: ScheduleExpressionTimezone
  type: string
- container: ''
  name: StartDate
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: ScheduleArn
  type: string
- container: ''
  name: Arn
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
  name: Source
  type: string
- container: ''
  name: MaximumWindowInMinutes
  type: string
- container: ''
  name: Mode
  type: string
- container: ''
  name: CreationDate
  type: string
- container: ''
  name: LastModificationDate
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: PartitionKey
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: ScheduleGroups
  type: string
- container: ''
  name: Schedules
  type: string
- container: ''
  name: awsvpcConfiguration
  type: string
- container: ''
  name: expression
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: field
  type: string
- container: ''
  name: MaximumEventAgeInSeconds
  type: string
- container: ''
  name: MaximumRetryAttempts
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: PipelineParameterList
  type: string
- container: ''
  name: MessageGroupId
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Input
  type: string
- container: ''
  name: RoleArn
  type: string
property_count: 54
provider_name: Amazon EventBridge Scheduler
provider_slug: amazon-eventbridge-scheduler
slug: amazon-eventbridge-scheduler-context
tags:
- Amazon Web Services
- AWS
- Cron
- Event-Driven
- Scheduling
- Serverless
- JSON-LD
- Linked Data
- Semantic Web
---

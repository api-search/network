---
class_count: 121
classes:
- DescribeMapRunInput
- DescribeMapRunOutput
- StartExecutionOutput
- ActivitySucceededEventDetails
- LambdaFunctionTimedOutEventDetails
- LambdaFunctionFailedEventDetails
- CreateStateMachineOutput
- ExecutionAbortedEventDetails
- ListStateMachineAliasesInput
- ListStateMachineAliasesOutput
- TaskStartedEventDetails
- StopExecutionOutput
- DeleteStateMachineAliasInput
- LambdaFunctionScheduledEventDetails
- StateExitedEventDetails
- UpdateMapRunOutput
- DeleteStateMachineVersionInput
- StartSyncExecutionInput
- StartExecutionInput
- DescribeActivityOutput
- MapRunFailedEventDetails
- DescribeStateMachineAliasOutput
- DeleteActivityOutput
- StateMachineVersionListItem
- LoggingConfiguration
- ActivityFailedEventDetails
- GetExecutionHistoryInput
- StartSyncExecutionOutput
- SendTaskHeartbeatInput
- MapIterationEventDetails
- SendTaskSuccessInput
- TaskCredentials
- CloudWatchEventsExecutionDataDetails
- RoutingConfigurationListItem
- GetActivityTaskInput
- ExecutionSucceededEventDetails
- BillingDetails
- CreateActivityInput
- DescribeExecutionInput
- ListActivitiesOutput
- ActivityScheduleFailedEventDetails
- DeleteStateMachineAliasOutput
- LogDestination
- SendTaskSuccessOutput
- TaskScheduledEventDetails
- PublishStateMachineVersionOutput
- LambdaFunctionStartFailedEventDetails
- ListStateMachineVersionsInput
- Amazon Step Functions State Machine
- ExecutionFailedEventDetails
- MapRunItemCounts
- SendTaskHeartbeatOutput
- DescribeStateMachineInput
- TaskTimedOutEventDetails
- DeleteActivityInput
- ListTagsForResourceInput
- UpdateStateMachineAliasOutput
- MapRunStartedEventDetails
- MapStateStartedEventDetails
- ListActivitiesInput
- TaskSubmitFailedEventDetails
- UpdateStateMachineInput
- DeleteStateMachineVersionOutput
- TaskStartFailedEventDetails
- TaskFailedEventDetails
- ListExecutionsOutput
- DescribeActivityInput
- UntagResourceInput
- ExecutionTimedOutEventDetails
- PublishStateMachineVersionInput
- ActivityListItem
- CreateStateMachineInput
- StopExecutionInput
- ListMapRunsOutput
- TaskSubmittedEventDetails
- CreateStateMachineAliasInput
- CreateActivityOutput
- MapRunExecutionCounts
- TaskSucceededEventDetails
- DescribeExecutionOutput
- HistoryEvent
- DeleteStateMachineInput
- ListStateMachinesInput
- ExecutionStartedEventDetails
- StateEnteredEventDetails
- StateMachineListItem
- StateMachineAliasListItem
- DescribeStateMachineAliasInput
- DescribeStateMachineOutput
- TagResourceOutput
- UpdateMapRunInput
- ActivityTimedOutEventDetails
- DeleteStateMachineOutput
- ListStateMachinesOutput
- ListStateMachineVersionsOutput
- SendTaskFailureInput
- ListExecutionsInput
- CloudWatchLogsLogGroup
- LambdaFunctionSucceededEventDetails
- TracingConfiguration
- TagResourceInput
- ListMapRunsInput
- MapRunListItem
- GetExecutionHistoryOutput
- ExecutionListItem
- Tag
- GetActivityTaskOutput
- DescribeStateMachineForExecutionInput
- UpdateStateMachineAliasInput
- HistoryEventExecutionDataDetails
- LambdaFunctionScheduleFailedEventDetails
- UpdateStateMachineOutput
- CreateStateMachineAliasOutput
- ListTagsForResourceOutput
- ActivityStartedEventDetails
- DescribeStateMachineForExecutionOutput
- ActivityScheduledEventDetails
- UntagResourceOutput
- SendTaskFailureOutput
- name
- description
context_file: json-ld/amazon-step-functions-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-step-functions/refs/heads/main/json-ld/amazon-step-functions-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Step Functions from Amazon Step Functions.
layout: jsonld
name: Amazon Step Functions Context
namespaces:
- prefix: aws
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: mapRunArn
  type: string
- container: ''
  name: executionArn
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: startDate
  type: string
- container: ''
  name: stopDate
  type: string
- container: ''
  name: maxConcurrency
  type: string
- container: ''
  name: toleratedFailurePercentage
  type: string
- container: ''
  name: toleratedFailureCount
  type: string
- container: ''
  name: itemCounts
  type: string
- container: ''
  name: executionCounts
  type: string
- container: ''
  name: output
  type: string
- container: ''
  name: outputDetails
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: cause
  type: string
- container: ''
  name: stateMachineArn
  type: string
- container: ''
  name: creationDate
  type: string
- container: ''
  name: stateMachineVersionArn
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: stateMachineAliases
  type: string
- container: ''
  name: resourceType
  type: string
- container: ''
  name: resource
  type: string
- container: ''
  name: stateMachineAliasArn
  type: string
- container: ''
  name: input
  type: string
- container: ''
  name: inputDetails
  type: string
- container: ''
  name: timeoutInSeconds
  type: string
- container: ''
  name: taskCredentials
  type: string
- container: ''
  name: traceHeader
  type: string
- container: ''
  name: activityArn
  type: string
- container: ''
  name: routingConfiguration
  type: string
- container: ''
  name: updateDate
  type: string
- container: ''
  name: level
  type: string
- container: ''
  name: includeExecutionData
  type: string
- container: ''
  name: destinations
  type: string
- container: ''
  name: reverseOrder
  type: string
- container: ''
  name: billingDetails
  type: string
- container: ''
  name: taskToken
  type: string
- container: ''
  name: index
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: included
  type: string
- container: ''
  name: weight
  type: string
- container: ''
  name: workerName
  type: string
- container: ''
  name: billedMemoryUsedInMB
  type: string
- container: ''
  name: billedDurationInMilliseconds
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: activities
  type: string
- container: ''
  name: cloudWatchLogsLogGroup
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: parameters
  type: string
- container: ''
  name: heartbeatInSeconds
  type: string
- container: ''
  name: definition
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: loggingConfiguration
  type: string
- container: ''
  name: tracingConfiguration
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: pending
  type: string
- container: ''
  name: running
  type: string
- container: ''
  name: succeeded
  type: string
- container: ''
  name: failed
  type: string
- container: ''
  name: timedOut
  type: string
- container: ''
  name: aborted
  type: string
- container: ''
  name: total
  type: string
- container: ''
  name: resultsWritten
  type: string
- container: ''
  name: resourceArn
  type: string
- container: ''
  name: length
  type: string
- container: ''
  name: publish
  type: string
- container: ''
  name: versionDescription
  type: string
- container: ''
  name: executions
  type: string
- container: ''
  name: tagKeys
  type: string
- container: ''
  name: mapRuns
  type: string
- container: ''
  name: timestamp
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: previousEventId
  type: string
- container: ''
  name: activityFailedEventDetails
  type: string
- container: ''
  name: activityScheduleFailedEventDetails
  type: string
- container: ''
  name: activityScheduledEventDetails
  type: string
- container: ''
  name: activityStartedEventDetails
  type: string
- container: ''
  name: activitySucceededEventDetails
  type: string
- container: ''
  name: activityTimedOutEventDetails
  type: string
- container: ''
  name: taskFailedEventDetails
  type: string
- container: ''
  name: taskScheduledEventDetails
  type: string
- container: ''
  name: taskStartFailedEventDetails
  type: string
- container: ''
  name: taskStartedEventDetails
  type: string
- container: ''
  name: taskSubmitFailedEventDetails
  type: string
- container: ''
  name: taskSubmittedEventDetails
  type: string
- container: ''
  name: taskSucceededEventDetails
  type: string
- container: ''
  name: taskTimedOutEventDetails
  type: string
- container: ''
  name: executionFailedEventDetails
  type: string
- container: ''
  name: executionStartedEventDetails
  type: string
- container: ''
  name: executionSucceededEventDetails
  type: string
- container: ''
  name: executionAbortedEventDetails
  type: string
- container: ''
  name: executionTimedOutEventDetails
  type: string
- container: ''
  name: mapStateStartedEventDetails
  type: string
- container: ''
  name: mapIterationStartedEventDetails
  type: string
- container: ''
  name: mapIterationSucceededEventDetails
  type: string
- container: ''
  name: mapIterationFailedEventDetails
  type: string
- container: ''
  name: mapIterationAbortedEventDetails
  type: string
- container: ''
  name: lambdaFunctionFailedEventDetails
  type: string
- container: ''
  name: lambdaFunctionScheduleFailedEventDetails
  type: string
- container: ''
  name: lambdaFunctionScheduledEventDetails
  type: string
- container: ''
  name: lambdaFunctionStartFailedEventDetails
  type: string
- container: ''
  name: lambdaFunctionSucceededEventDetails
  type: string
- container: ''
  name: lambdaFunctionTimedOutEventDetails
  type: string
- container: ''
  name: stateEnteredEventDetails
  type: string
- container: ''
  name: stateExitedEventDetails
  type: string
- container: ''
  name: mapRunStartedEventDetails
  type: string
- container: ''
  name: mapRunFailedEventDetails
  type: string
- container: ''
  name: stateMachines
  type: string
- container: ''
  name: stateMachineVersions
  type: string
- container: ''
  name: statusFilter
  type: string
- container: ''
  name: logGroupArn
  type: string
- container: ''
  name: enabled
  type: string
- container: ''
  name: events
  type: string
- container: ''
  name: itemCount
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: truncated
  type: string
property_count: 118
provider_name: Amazon Step Functions
provider_slug: amazon-step-functions
slug: amazon-step-functions-context
tags:
- AWS
- Orchestration
- Serverless
- State Machine
- Workflow
- JSON-LD
- Linked Data
- Semantic Web
---

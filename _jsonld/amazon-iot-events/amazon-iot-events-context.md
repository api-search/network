---
class_count: 101
classes:
- AcknowledgeFlow
- Action
- AlarmAction
- AlarmCapabilities
- AlarmEventActions
- AlarmModelSummary
- AlarmModelVersionSummary
- AlarmNotification
- AlarmRule
- AnalysisResult
- AnalysisResultLocation
- AssetPropertyTimestamp
- AssetPropertyValue
- AssetPropertyVariant
- Attribute
- ClearTimerAction
- CreateAlarmModelRequest
- CreateAlarmModelResponse
- CreateDetectorModelRequest
- CreateDetectorModelResponse
- CreateInputRequest
- CreateInputResponse
- DeleteAlarmModelRequest
- DeleteAlarmModelResponse
- DeleteDetectorModelRequest
- DeleteDetectorModelResponse
- DeleteInputRequest
- DeleteInputResponse
- DescribeAlarmModelRequest
- DescribeAlarmModelResponse
- DescribeDetectorModelAnalysisRequest
- DescribeDetectorModelAnalysisResponse
- DescribeDetectorModelRequest
- DescribeDetectorModelResponse
- DescribeInputRequest
- DescribeInputResponse
- DescribeLoggingOptionsRequest
- DescribeLoggingOptionsResponse
- DetectorDebugOption
- DetectorModel
- DetectorModelConfiguration
- DetectorModelDefinition
- DetectorModelSummary
- DetectorModelVersionSummary
- DynamoDBAction
- DynamoDBv2Action
- EmailConfiguration
- EmailContent
- EmailRecipients
- Event
- FirehoseAction
- GetDetectorModelAnalysisResultsRequest
- GetDetectorModelAnalysisResultsResponse
- InitializationConfiguration
- Input
- InputConfiguration
- InputDefinition
- InputIdentifier
- InputSummary
- IotEventsAction
- IotEventsInputIdentifier
- IotSiteWiseAction
- IotSiteWiseAssetModelPropertyIdentifier
- IotSiteWiseInputIdentifier
- IotTopicPublishAction
- LambdaAction
- ListAlarmModelVersionsRequest
- ListAlarmModelVersionsResponse
- ListAlarmModelsRequest
- ListAlarmModelsResponse
- ListDetectorModelVersionsRequest
- ListDetectorModelVersionsResponse
- ListDetectorModelsRequest
- ListDetectorModelsResponse
- ListInputRoutingsRequest
- ListInputRoutingsResponse
- ListInputsRequest
- ListInputsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- LoggingOptions
- NotificationAction
- NotificationTargetActions
- OnEnterLifecycle
- OnExitLifecycle
- OnInputLifecycle
- Payload
- PutLoggingOptionsRequest
- RecipientDetail
- ResetTimerAction
- RoutedResource
- SMSConfiguration
- SNSTopicPublishAction
- SSOIdentity
- SetTimerAction
- SetVariableAction
- SimpleRule
- SqsAction
- StartDetectorModelAnalysisRequest
- StartDetectorModelAnalysisResponse
- name
context_file: json-ld/amazon-iot-events-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-events/refs/heads/main/json-ld/amazon-iot-events-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Iot Events from Amazon IoT Events.
layout: jsonld
name: Amazon Iot Events Context
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
  name: acknowledgeFlow
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: actions
  type: string
- container: ''
  name: additionalMessage
  type: string
- container: ''
  name: alarmActions
  type: string
- container: ''
  name: alarmCapabilities
  type: string
- container: ''
  name: alarmEventActions
  type: string
- container: ''
  name: alarmModelArn
  type: string
- container: ''
  name: alarmModelDescription
  type: string
- container: ''
  name: alarmModelName
  type: string
- container: ''
  name: alarmModelSummaries
  type: string
- container: ''
  name: alarmModelVersion
  type: string
- container: ''
  name: alarmModelVersionSummaries
  type: string
- container: ''
  name: alarmNotification
  type: string
- container: ''
  name: alarmRule
  type: string
- container: ''
  name: analysisId
  type: string
- container: ''
  name: analysisResults
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: assetId
  type: string
- container: ''
  name: assetModelId
  type: string
- container: ''
  name: attributes
  type: string
- container: ''
  name: booleanValue
  type: string
- container: ''
  name: clearTimer
  type: string
- container: ''
  name: comparisonOperator
  type: string
- container: ''
  name: condition
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: contentExpression
  type: string
- container: ''
  name: creationTime
  type: string
- container: ''
  name: deliveryStreamName
  type: string
- container: ''
  name: detectorDebugOptions
  type: string
- container: ''
  name: detectorModel
  type: string
- container: ''
  name: detectorModelArn
  type: string
- container: ''
  name: detectorModelConfiguration
  type: string
- container: ''
  name: detectorModelDefinition
  type: string
- container: ''
  name: detectorModelDescription
  type: string
- container: ''
  name: detectorModelName
  type: string
- container: ''
  name: detectorModelSummaries
  type: string
- container: ''
  name: detectorModelVersion
  type: string
- container: ''
  name: detectorModelVersionSummaries
  type: string
- container: ''
  name: disabledOnInitialization
  type: string
- container: ''
  name: doubleValue
  type: string
- container: ''
  name: durationExpression
  type: string
- container: ''
  name: dynamoDB
  type: string
- container: ''
  name: dynamoDBv2
  type: string
- container: ''
  name: emailConfigurations
  type: string
- container: ''
  name: enabled
  type: string
- container: ''
  name: entryId
  type: string
- container: ''
  name: evaluationMethod
  type: string
- container: ''
  name: eventName
  type: string
- container: ''
  name: events
  type: string
- container: ''
  name: firehose
  type: string
- container: ''
  name: from
  type: string
- container: ''
  name: functionArn
  type: string
- container: ''
  name: hashKeyField
  type: string
- container: ''
  name: hashKeyType
  type: string
- container: ''
  name: hashKeyValue
  type: string
- container: ''
  name: identityStoreId
  type: string
- container: ''
  name: initialStateName
  type: string
- container: ''
  name: initializationConfiguration
  type: string
- container: ''
  name: input
  type: string
- container: ''
  name: inputArn
  type: string
- container: ''
  name: inputConfiguration
  type: string
- container: ''
  name: inputDefinition
  type: string
- container: ''
  name: inputDescription
  type: string
- container: ''
  name: inputIdentifier
  type: string
- container: ''
  name: inputName
  type: string
- container: ''
  name: inputProperty
  type: string
- container: ''
  name: inputSummaries
  type: string
- container: ''
  name: integerValue
  type: string
- container: ''
  name: iotEvents
  type: string
- container: ''
  name: iotEventsInputIdentifier
  type: string
- container: ''
  name: iotSiteWise
  type: string
- container: ''
  name: iotSiteWiseAssetModelPropertyIdentifier
  type: string
- container: ''
  name: iotSiteWiseInputIdentifier
  type: string
- container: ''
  name: iotTopicPublish
  type: string
- container: ''
  name: jsonPath
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: keyValue
  type: string
- container: ''
  name: lambda
  type: string
- container: ''
  name: lambdaAction
  type: string
- container: ''
  name: lastUpdateTime
  type: string
- container: ''
  name: level
  type: string
- container: ''
  name: locations
  type: string
- container: ''
  name: loggingOptions
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: mqttTopic
  type: string
- container: ''
  name: nextState
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: notificationActions
  type: string
- container: ''
  name: offsetInNanos
  type: string
- container: ''
  name: onEnter
  type: string
- container: ''
  name: onExit
  type: string
- container: ''
  name: onInput
  type: string
- container: ''
  name: operation
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: payload
  type: string
- container: ''
  name: payloadField
  type: string
- container: ''
  name: propertyAlias
  type: string
- container: ''
  name: propertyId
  type: string
- container: ''
  name: propertyValue
  type: string
- container: ''
  name: quality
  type: string
- container: ''
  name: queueUrl
  type: string
- container: ''
  name: rangeKeyField
  type: string
- container: ''
  name: rangeKeyType
  type: string
- container: ''
  name: rangeKeyValue
  type: string
- container: ''
  name: recipients
  type: string
- container: ''
  name: resetTimer
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: routedResources
  type: string
- container: ''
  name: seconds
  type: string
- container: ''
  name: senderId
  type: string
- container: ''
  name: separator
  type: string
- container: ''
  name: setTimer
  type: string
- container: ''
  name: setVariable
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: simpleRule
  type: string
- container: ''
  name: smsConfigurations
  type: string
- container: ''
  name: sns
  type: string
- container: ''
  name: sqs
  type: string
- container: ''
  name: ssoIdentity
  type: string
- container: ''
  name: stateName
  type: string
- container: ''
  name: states
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusMessage
  type: string
- container: ''
  name: stringValue
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: tableName
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: targetArn
  type: string
- container: ''
  name: threshold
  type: string
- container: ''
  name: timeInSeconds
  type: string
- container: ''
  name: timerName
  type: string
- container: ''
  name: timestamp
  type: string
- container: ''
  name: to
  type: string
- container: ''
  name: transitionEvents
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: useBase64
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: variableName
  type: string
property_count: 141
provider_name: Amazon IoT Events
provider_slug: amazon-iot-events
slug: amazon-iot-events-context
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
- JSON-LD
- Linked Data
- Semantic Web
---

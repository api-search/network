---
class_count: 102
classes:
- Action
- AddThingToBillingGroupResponse
- AddThingToThingGroupResponse
- AddThingsToThingGroupParams
- AlertTarget
- AssociateTargetsWithJobResponse
- AttachSecurityProfileResponse
- AttachThingPrincipalResponse
- AttributePayload
- Attributes
- AwsJobExponentialRolloutRate
- Behavior
- CancelAuditMitigationActionsTaskResponse
- CancelAuditTaskResponse
- CancelDetectMitigationActionsTaskResponse
- CancelJobResponse
- ClearDefaultAuthorizerResponse
- ConfirmTopicRuleDestinationResponse
- CreateAuditSuppressionResponse
- CreateAuthorizerResponse
- CreateBillingGroupResponse
- CreateCertificateFromCsrResponse
- CreateCustomMetricResponse
- CreateDimensionResponse
- CreateDomainConfigurationResponse
- CreateDynamicThingGroupResponse
- CreateFleetMetricResponse
- CreateJobResponse
- CreateJobTemplateResponse
- CreateKeysAndCertificateResponse
- CreateMitigationActionResponse
- CreateOTAUpdateResponse
- CreatePolicyResponse
- CreatePolicyVersionResponse
- CreateProvisioningClaimResponse
- CreateProvisioningTemplateResponse
- CreateProvisioningTemplateVersionResponse
- CreateRoleAliasResponse
- CreateScheduledAuditResponse
- CreateSecurityProfileResponse
- CreateStreamResponse
- CreateThingGroupResponse
- CreateThingResponse
- CreateThingTypeResponse
- CreateTopicRuleDestinationResponse
- DeleteAccountAuditConfigurationResponse
- DeleteAuditSuppressionResponse
- DeleteAuthorizerResponse
- DeleteBillingGroupResponse
- DeleteCACertificateResponse
- DeleteCustomMetricResponse
- DeleteDimensionResponse
- DeleteDomainConfigurationResponse
- DeleteDynamicThingGroupResponse
- DeleteMitigationActionResponse
- DeleteOTAUpdateResponse
- DeleteProvisioningTemplateResponse
- DeleteProvisioningTemplateVersionResponse
- DeleteRegistrationCodeResponse
- DeleteRoleAliasResponse
- DeleteScheduledAuditResponse
- DeleteSecurityProfileResponse
- DeleteStreamResponse
- DeleteThingGroupResponse
- DeleteThingResponse
- DeleteThingTypeResponse
- DeleteTopicRuleDestinationResponse
- DeprecateThingTypeResponse
- DescribeAccountAuditConfigurationResponse
- DescribeAuditFindingResponse
- DescribeAuditMitigationActionsTaskResponse
- DescribeAuditSuppressionResponse
- DescribeAuditTaskResponse
- DescribeAuthorizerResponse
- DescribeBillingGroupResponse
- DescribeCACertificateResponse
- DescribeCertificateResponse
- DescribeCustomMetricResponse
- DescribeDefaultAuthorizerResponse
- DescribeDetectMitigationActionsTaskResponse
- DescribeDimensionResponse
- DescribeDomainConfigurationResponse
- DescribeEndpointResponse
- DescribeEventConfigurationsResponse
- DescribeFleetMetricResponse
- DescribeIndexResponse
- DescribeJobExecutionResponse
- DescribeJobResponse
- DescribeJobTemplateResponse
- DescribeManagedJobTemplateResponse
- DescribeMitigationActionResponse
- DescribeProvisioningTemplateResponse
- DescribeProvisioningTemplateVersionResponse
- DescribeRoleAliasResponse
- DescribeScheduledAuditResponse
- DescribeSecurityProfileResponse
- DescribeStreamResponse
- DescribeThingGroupResponse
- DescribeThingRegistrationTaskResponse
- DescribeThingResponse
- description
- name
context_file: json-ld/amazon-iot-device-defender-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-device-defender/refs/heads/main/json-ld/amazon-iot-device-defender-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Iot Device Defender from Amazon IoT Device Defender.
layout: jsonld
name: Amazon Iot Device Defender Context
namespaces:
- prefix: amzn
  uri: https://amazonaws.com/schema/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: schema
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: abortConfig
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: actionArn
  type: string
- container: ''
  name: actionId
  type: string
- container: ''
  name: actionIdentifiers
  type: string
- container: ''
  name: actionName
  type: string
- container: ''
  name: actionParams
  type: string
- container: ''
  name: actionType
  type: string
- container: ''
  name: actionsDefinition
  type: string
- container: ''
  name: actionsExecutions
  type: string
- container: ''
  name: activeViolations
  type: string
- container: ''
  name: additionalMetricsToRetain
  type: string
- container: ''
  name: additionalMetricsToRetainV2
  type: string
- container: ''
  name: aggregationField
  type: string
- container: ''
  name: aggregationType
  type: string
- container: ''
  name: alertTargetArn
  type: string
- container: ''
  name: alertTargets
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: attributes
  type: string
- container: ''
  name: auditCheckConfigurations
  type: string
- container: ''
  name: auditCheckToActionsMapping
  type: string
- container: ''
  name: auditDetails
  type: string
- container: ''
  name: auditNotificationTargetConfigurations
  type: string
- container: ''
  name: authorizerArn
  type: string
- container: ''
  name: authorizerConfig
  type: string
- container: ''
  name: authorizerDescription
  type: string
- container: ''
  name: authorizerName
  type: string
- container: ''
  name: authorizers
  type: string
- container: ''
  name: awsIotJobArn
  type: string
- container: ''
  name: awsIotJobId
  type: string
- container: ''
  name: baseRatePerMinute
  type: string
- container: ''
  name: behaviors
  type: string
- container: ''
  name: billingGroupArn
  type: string
- container: ''
  name: billingGroupId
  type: string
- container: ''
  name: billingGroupMetadata
  type: string
- container: ''
  name: billingGroupName
  type: string
- container: ''
  name: billingGroupProperties
  type: string
- container: ''
  name: billingGroups
  type: string
- container: ''
  name: buckets
  type: string
- container: ''
  name: cardinality
  type: string
- container: ''
  name: certificateArn
  type: string
- container: ''
  name: certificateDescription
  type: string
- container: ''
  name: certificateId
  type: string
- container: ''
  name: certificatePem
  type: string
- container: ''
  name: certificates
  type: string
- container: ''
  name: checkName
  type: string
- container: ''
  name: cloudwatchAlarm
  type: string
- container: ''
  name: cloudwatchLogs
  type: string
- container: ''
  name: cloudwatchMetric
  type: string
- container: ''
  name: codeSigning
  type: string
- container: ''
  name: confirmationUrl
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: creationDate
  type: string
- container: ''
  name: criteria
  type: string
- container: ''
  name: dayOfMonth
  type: string
- container: ''
  name: dayOfWeek
  type: string
- container: ''
  name: defaultClientId
  type: string
- container: ''
  name: defaultLogLevel
  type: string
- container: ''
  name: defaultVersionId
  type: string
- container: ''
  name: destinationSummaries
  type: string
- container: ''
  name: dimensionNames
  type: string
- container: ''
  name: disableAllLogs
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: document
  type: string
- container: ''
  name: documentParameters
  type: string
- container: ''
  name: documentSource
  type: string
- container: ''
  name: domainConfigurationArn
  type: string
- container: ''
  name: domainConfigurationName
  type: string
- container: ''
  name: domainConfigurationStatus
  type: string
- container: ''
  name: domainConfigurations
  type: string
- container: ''
  name: domainName
  type: string
- container: ''
  name: domainType
  type: string
- container: ''
  name: durationInMinutes
  type: string
- container: ''
  name: dynamoDB
  type: string
- container: ''
  name: dynamoDBv2
  type: string
- container: ''
  name: effectivePolicies
  type: string
- container: ''
  name: elasticsearch
  type: string
- container: ''
  name: enabled
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: endpointAddress
  type: string
- container: ''
  name: environments
  type: string
- container: ''
  name: eventConfigurations
  type: string
- container: ''
  name: execution
  type: string
- container: ''
  name: executionSummaries
  type: string
- container: ''
  name: expiration
  type: string
- container: ''
  name: expirationDate
  type: string
- container: ''
  name: failureCount
  type: string
- container: ''
  name: fileId
  type: string
- container: ''
  name: fileLocation
  type: string
- container: ''
  name: fileName
  type: string
- container: ''
  name: fileType
  type: string
- container: ''
  name: fileVersion
  type: string
- container: ''
  name: finding
  type: string
- container: ''
  name: findings
  type: string
- container: ''
  name: firehose
  type: string
- container: ''
  name: fleetMetrics
  type: string
- container: ''
  name: frequency
  type: string
- container: ''
  name: generationId
  type: string
- container: ''
  name: http
  type: string
- container: ''
  name: incrementFactor
  type: string
- container: ''
  name: indexName
  type: string
- container: ''
  name: indexNames
  type: string
- container: ''
  name: indexStatus
  type: string
- container: ''
  name: inputFileBucket
  type: string
- container: ''
  name: inputFileKey
  type: string
- container: ''
  name: iotAnalytics
  type: string
- container: ''
  name: iotEvents
  type: string
- container: ''
  name: iotSiteWise
  type: string
- container: ''
  name: isDefaultVersion
  type: string
- container: ''
  name: issuerCertificateSerialNumber
  type: string
- container: ''
  name: issuerCertificateSubject
  type: string
- container: ''
  name: issuerId
  type: string
- container: ''
  name: job
  type: string
- container: ''
  name: jobArn
  type: string
- container: ''
  name: jobExecutionsRetryConfig
  type: string
- container: ''
  name: jobExecutionsRolloutConfig
  type: string
- container: ''
  name: jobId
  type: string
- container: ''
  name: jobTemplateArn
  type: string
- container: ''
  name: jobTemplateId
  type: string
- container: ''
  name: jobTemplates
  type: string
- container: ''
  name: jobs
  type: string
- container: ''
  name: kafka
  type: string
- container: ''
  name: keyPair
  type: string
- container: ''
  name: kinesis
  type: string
- container: ''
  name: lambda
  type: string
- container: ''
  name: lastModifiedDate
  type: string
- container: ''
  name: lastStatusChangeDate
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: logLevel
  type: string
- container: ''
  name: maintenanceWindows
  type: string
- container: ''
  name: managedJobTemplates
  type: string
- container: ''
  name: maxBuckets
  type: string
- container: ''
  name: merge
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: metric
  type: string
- container: ''
  name: metricArn
  type: string
- container: ''
  name: metricDatumList
  type: string
- container: ''
  name: metricDimension
  type: string
- container: ''
  name: metricName
  type: string
- container: ''
  name: metricNames
  type: string
- container: ''
  name: metricType
  type: string
- container: ''
  name: nextMarker
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: openSearch
  type: string
- container: ''
  name: otaUpdateArn
  type: string
- container: ''
  name: otaUpdateId
  type: string
- container: ''
  name: otaUpdateInfo
  type: string
- container: ''
  name: otaUpdateStatus
  type: string
- container: ''
  name: otaUpdates
  type: string
- container: ''
  name: outgoingCertificates
  type: string
- container: ''
  name: overrideDynamicGroups
  type: string
- container: ''
  name: percentageProgress
  type: string
- container: ''
  name: percentiles
  type: string
- container: ''
  name: period
  type: string
- container: ''
  name: policies
  type: string
- container: ''
  name: policyArn
  type: string
- container: ''
  name: policyDocument
  type: string
- container: ''
  name: policyName
  type: string
- container: ''
  name: policyVersionId
  type: string
- container: ''
  name: policyVersions
  type: string
- container: ''
  name: preProvisioningHook
  type: string
- container: ''
  name: presignedUrlConfig
  type: string
- container: ''
  name: principals
  type: string
- container: ''
  name: provisioningRoleArn
  type: string
- container: ''
  name: queryString
  type: string
- container: ''
  name: queryVersion
  type: string
- container: ''
  name: rateIncreaseCriteria
  type: string
- container: ''
  name: registrationCode
  type: string
- container: ''
  name: registrationConfig
  type: string
- container: ''
  name: relatedResources
  type: string
- container: ''
  name: reportType
  type: string
- container: ''
  name: republish
  type: string
- container: ''
  name: resourceIdentifier
  type: string
- container: ''
  name: resourceLinks
  type: string
- container: ''
  name: roleAlias
  type: string
- container: ''
  name: roleAliasArn
  type: string
- container: ''
  name: roleAliasDescription
  type: string
- container: ''
  name: roleAliases
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: roleArnForLogging
  type: string
- container: ''
  name: rule
  type: string
- container: ''
  name: ruleArn
  type: string
- container: ''
  name: rules
  type: string
- container: ''
  name: s3
  type: string
- container: ''
  name: s3Location
  type: string
- container: ''
  name: salesforce
  type: string
- container: ''
  name: scheduledAuditArn
  type: string
- container: ''
  name: scheduledAuditName
  type: string
- container: ''
  name: scheduledAudits
  type: string
- container: ''
  name: securityGroups
  type: string
- container: ''
  name: securityProfileArn
  type: string
- container: ''
  name: securityProfileDescription
  type: string
- container: ''
  name: securityProfileIdentifiers
  type: string
- container: ''
  name: securityProfileName
  type: string
- container: ''
  name: securityProfileTargetMappings
  type: string
- container: ''
  name: securityProfileTargets
  type: string
- container: ''
  name: serverCertificates
  type: string
- container: ''
  name: serviceType
  type: string
- container: ''
  name: sns
  type: string
- container: ''
  name: sqs
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: statistics
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: stepFunctions
  type: string
- container: ''
  name: streamArn
  type: string
- container: ''
  name: streamId
  type: string
- container: ''
  name: streamInfo
  type: string
- container: ''
  name: streamVersion
  type: string
- container: ''
  name: streams
  type: string
- container: ''
  name: stringValues
  type: string
- container: ''
  name: subnetIds
  type: string
- container: ''
  name: successCount
  type: string
- container: ''
  name: summaries
  type: string
- container: ''
  name: suppressAlerts
  type: string
- container: ''
  name: suppressIndefinitely
  type: string
- container: ''
  name: suppressions
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: target
  type: string
- container: ''
  name: targetCheckNames
  type: string
- container: ''
  name: targets
  type: string
- container: ''
  name: taskId
  type: string
- container: ''
  name: taskIds
  type: string
- container: ''
  name: taskStartTime
  type: string
- container: ''
  name: taskStatistics
  type: string
- container: ''
  name: taskStatus
  type: string
- container: ''
  name: taskSummary
  type: string
- container: ''
  name: taskType
  type: string
- container: ''
  name: tasks
  type: string
- container: ''
  name: templateArn
  type: string
- container: ''
  name: templateBody
  type: string
- container: ''
  name: templateName
  type: string
- container: ''
  name: templateVersion
  type: string
- container: ''
  name: templates
  type: string
- container: ''
  name: thingArn
  type: string
- container: ''
  name: thingGroupArn
  type: string
- container: ''
  name: thingGroupId
  type: string
- container: ''
  name: thingGroupIndexingConfiguration
  type: string
- container: ''
  name: thingGroupMetadata
  type: string
- container: ''
  name: thingGroupName
  type: string
- container: ''
  name: thingGroupNames
  type: string
- container: ''
  name: thingGroupProperties
  type: string
- container: ''
  name: thingGroups
  type: string
- container: ''
  name: thingId
  type: string
- container: ''
  name: thingIndexingConfiguration
  type: string
- container: ''
  name: thingName
  type: string
- container: ''
  name: thingTypeArn
  type: string
- container: ''
  name: thingTypeId
  type: string
- container: ''
  name: thingTypeMetadata
  type: string
- container: ''
  name: thingTypeName
  type: string
- container: ''
  name: thingTypeProperties
  type: string
- container: ''
  name: thingTypes
  type: string
- container: ''
  name: things
  type: string
- container: ''
  name: timeoutConfig
  type: string
- container: ''
  name: timestream
  type: string
- container: ''
  name: topicArn
  type: string
- container: ''
  name: topicRuleDestination
  type: string
- container: ''
  name: totalCount
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: versionId
  type: string
- container: ''
  name: versions
  type: string
- container: ''
  name: vpcId
  type: string
property_count: 266
provider_name: Amazon IoT Device Defender
provider_slug: amazon-iot-device-defender
slug: amazon-iot-device-defender-context
tags:
- AWS
- Compliance
- IoT
- Security
- Vulnerability Management
- JSON-LD
- Linked Data
- Semantic Web
---

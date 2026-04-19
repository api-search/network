---
class_count: 76
classes:
- RebootBrokerRequest
- CreateUserRequest
- CreateUserResponse
- EngineType
- BrokerSummary
- BrokerStorageType
- DescribeBrokerInstanceOptionsResponse
- UpdateConfigurationResponse
- Logs
- UpdateUserRequest
- BrokerEngineType
- BrokerInstance
- DescribeConfigurationRequest
- DescribeConfigurationRevisionResponse
- DayOfWeek
- ListUsersRequest
- DeleteUserRequest
- Configuration
- UpdateUserResponse
- ListConfigurationsResponse
- CreateConfigurationRequest
- DeploymentMode
- DeleteBrokerRequest
- DeleteBrokerResponse
- LogsSummary
- ListUsersResponse
- DescribeBrokerEngineTypesResponse
- ListTagsRequest
- DeleteTagsRequest
- PendingLogs
- DescribeConfigurationResponse
- SanitizationWarningReason
- ListConfigurationsRequest
- ListConfigurationRevisionsResponse
- CreateTagsRequest
- CreateBrokerRequest
- DescribeUserResponse
- DeleteUserResponse
- ListTagsResponse
- DescribeConfigurationRevisionRequest
- UnauthorizedException
- BrokerInstanceOption
- UpdateBrokerRequest
- UserSummary
- DescribeBrokerResponse
- UpdateBrokerResponse
- ListBrokersResponse
- User
- CreateConfigurationResponse
- UpdateConfigurationRequest
- AuthenticationStrategy
- ConfigurationRevision
- LdapServerMetadataOutput
- WeeklyStartTime
- LdapServerMetadataInput
- BrokerState
- RebootBrokerResponse
- Configurations
- DescribeBrokerEngineTypesRequest
- ConfigurationId
- DescribeBrokerInstanceOptionsRequest
- ListConfigurationRevisionsRequest
- MaxResults
- UserPendingChanges
- CreateBrokerResponse
- DescribeBrokerRequest
- ChangeType
- ActionRequired
- DescribeUserRequest
- ListBrokersRequest
- EncryptionOptions
- EngineVersion
- AvailabilityZone
- SanitizationWarning
- name
- description
context_file: json-ld/amazon-mq-mq-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-mq/refs/heads/main/json-ld/amazon-mq-mq-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Mq Mq Api from Amazon MQ.
layout: jsonld
name: Amazon Mq Mq Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: consoleAccess
  type: string
- container: ''
  name: groups
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: brokerArn
  type: string
- container: ''
  name: brokerId
  type: string
- container: ''
  name: brokerName
  type: string
- container: ''
  name: brokerState
  type: string
- container: ''
  name: created
  type: string
- container: ''
  name: deploymentMode
  type: string
- container: ''
  name: engineType
  type: string
- container: ''
  name: hostInstanceType
  type: string
- container: ''
  name: brokerInstanceOptions
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: latestRevision
  type: string
- container: ''
  name: warnings
  type: string
- container: ''
  name: audit
  type: string
- container: ''
  name: general
  type: string
- container: ''
  name: engineVersions
  type: string
- container: ''
  name: consoleUrl
  type: string
- container: ''
  name: endpoints
  type: string
- container: ''
  name: ipAddress
  type: string
- container: ''
  name: configurationId
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: authenticationStrategy
  type: string
- container: ''
  name: engineVersion
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: configurations
  type: string
- container: ''
  name: auditLogGroup
  type: string
- container: ''
  name: generalLogGroup
  type: string
- container: ''
  name: pending
  type: string
- container: ''
  name: users
  type: string
- container: ''
  name: brokerEngineTypes
  type: string
- container: ''
  name: revisions
  type: string
- container: ''
  name: autoMinorVersionUpgrade
  type: string
- container: ''
  name: configuration
  type: string
- container: ''
  name: creatorRequestId
  type: string
- container: ''
  name: encryptionOptions
  type: string
- container: ''
  name: ldapServerMetadata
  type: string
- container: ''
  name: logs
  type: string
- container: ''
  name: maintenanceWindowStartTime
  type: string
- container: ''
  name: publiclyAccessible
  type: string
- container: ''
  name: securityGroups
  type: string
- container: ''
  name: storageType
  type: string
- container: ''
  name: subnetIds
  type: string
- container: ''
  name: username
  type: string
- container: ''
  name: availabilityZones
  type: string
- container: ''
  name: supportedDeploymentModes
  type: string
- container: ''
  name: supportedEngineVersions
  type: string
- container: ''
  name: pendingChange
  type: string
- container: ''
  name: actionsRequired
  type: string
- container: ''
  name: brokerInstances
  type: string
- container: ''
  name: pendingAuthenticationStrategy
  type: string
- container: ''
  name: pendingEngineVersion
  type: string
- container: ''
  name: pendingHostInstanceType
  type: string
- container: ''
  name: pendingLdapServerMetadata
  type: string
- container: ''
  name: pendingSecurityGroups
  type: string
- container: ''
  name: brokerSummaries
  type: string
- container: ''
  name: revision
  type: string
- container: ''
  name: hosts
  type: string
- container: ''
  name: roleBase
  type: string
- container: ''
  name: roleName
  type: string
- container: ''
  name: roleSearchMatching
  type: string
- container: ''
  name: roleSearchSubtree
  type: string
- container: ''
  name: serviceAccountUsername
  type: string
- container: ''
  name: userBase
  type: string
- container: ''
  name: userRoleName
  type: string
- container: ''
  name: userSearchMatching
  type: string
- container: ''
  name: userSearchSubtree
  type: string
- container: ''
  name: dayOfWeek
  type: string
- container: ''
  name: timeOfDay
  type: string
- container: ''
  name: timeZone
  type: string
- container: ''
  name: serviceAccountPassword
  type: string
- container: ''
  name: current
  type: string
- container: ''
  name: history
  type: string
- container: ''
  name: actionRequiredCode
  type: string
- container: ''
  name: actionRequiredInfo
  type: string
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: useAwsOwnedKey
  type: string
- container: ''
  name: attributeName
  type: string
- container: ''
  name: elementName
  type: string
- container: ''
  name: reason
  type: string
property_count: 84
provider_name: Amazon MQ
provider_slug: amazon-mq
slug: amazon-mq-mq-api-context
tags:
- AWS
- Broadcasting
- Media Processing
- Media
- JSON-LD
- Linked Data
- Semantic Web
---

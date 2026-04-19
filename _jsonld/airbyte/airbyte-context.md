---
class_count: 108
classes:
- EncryptionMapperAESConfiguration
- NotificationConfig
- ResourceRequirements
- RowFilteringOperation
- ApplicationCreate
- StreamConfigurations
- GroupMemberResponse
- CreateDeclarativeSourceDefinitionRequest
- TagResponse
- DataplaneCreateRequest
- PermissionResponseRead
- DeclarativeSourceDefinitionsResponse
- EmbeddedWidgetRequest
- RowFilteringMapperConfiguration
- EmbeddedWidgetResponse
- RegionsResponse
- InitiateOauthRequest
- TagPatchRequest
- RowFilteringOperationNot
- SourcePutRequest
- WebhookNotificationConfig
- DefinitionsResponse
- ConnectionResponse
- SourceConfiguration
- SourceResponse
- DataplaneResponse
- UserResponse
- OAuthCredentialsConfiguration
- GroupPermissionsResponse
- EmailNotificationConfig
- ConnectionsResponse
- TagsResponse
- JobTypeResourceLimit
- RegionPatchRequest
- FieldRenamingMapperConfiguration
- EmbeddedOrganizationListItem
- StreamConfiguration
- WorkspaceResponse
- EmbeddedOrganizationsList
- DefinitionResponse
- ConnectorDefinitionsResponse
- RegionCreateRequest
- DestinationPatchRequest
- SourceDefinitionSpecification
- EmbeddedScopedTokenRequest
- WorkspaceOAuthCredentialsRequest
- GroupPermissionResponse
- PermissionResponse
- EncryptionMapperConfiguration
- StreamProperties
- NotificationsConfig
- WorkspaceCreateRequest
- SelectedFieldInfo
- ApplicationTokenRequestWithGrant
- RedirectUrlResponse
- DeclarativeManifest
- WorkspacesResponse
- OrganizationOAuthCredentialsRequest
- GroupCreateRequest
- CreateDefinitionRequest
- UpdateDeclarativeSourceDefinitionRequest
- DestinationResponse
- DataplanesResponse
- DeclarativeSourceDefinitionResponse
- JobsResponse
- GroupMemberAddRequest
- UsersResponse
- DestinationConfiguration
- SourcesResponse
- GroupsResponse
- PermissionCreateRequest
- UpdateDefinitionRequest
- ScopedResourceRequirements
- ConfiguredStreamMapper
- SourceCreateRequest
- ConnectionCreateRequest
- TagCreateRequest
- ApplicationReadList
- DestinationPutRequest
- AirbyteApiConnectionSchedule
- FieldFilteringMapperConfiguration
- EncryptionMapperRSAConfiguration
- JobResponse
- WorkspaceUpdateRequest
- Tag
- ConnectionScheduleResponse
- GroupUpdateRequest
- ConnectorDefinitionResponse
- OrganizationResponse
- MapperConfiguration
- RowFilteringOperationEqual
- DataplanePatchRequest
- GroupPermissionCreateRequest
- DestinationsResponse
- ApplicationRead
- DestinationCreateRequest
- GroupMembersResponse
- OrganizationsResponse
- PublicAccessTokenResponse
- RegionResponse
- HashingMapperConfiguration
- EmbeddedScopedTokenResponse
- PermissionUpdateRequest
- ConnectionPatchRequest
- GroupResponse
- SourcePatchRequest
- PermissionsResponse
- JobCreateRequest
context_file: json-ld/airbyte-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/json-ld/airbyte-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Airbyte from Airbyte.
layout: jsonld
name: Airbyte Context
namespaces:
- prefix: airbyte
  uri: https://airbyte.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: algorithm
  type: ''
- container: ''
  name: fieldNameSuffix
  type: ''
- container: ''
  name: key
  type: ''
- container: ''
  name: mode
  type: ''
- container: ''
  name: padding
  type: ''
- container: ''
  name: targetField
  type: ''
- container: ''
  name: email
  type: ''
- container: ''
  name: webhook
  type: ''
- container: ''
  name: cpuRequest
  type: ''
- container: ''
  name: cpuLimit
  type: ''
- container: ''
  name: memoryRequest
  type: ''
- container: ''
  name: memoryLimit
  type: ''
- container: ''
  name: ephemeralStorageRequest
  type: ''
- container: ''
  name: ephemeralStorageLimit
  type: ''
- container: ''
  name: name
  type: ''
- container: set
  name: streams
  type: string
- container: ''
  name: memberId
  type: ''
- container: ''
  name: groupId
  type: ''
- container: ''
  name: userId
  type: ''
- container: ''
  name: userEmail
  type: ''
- container: ''
  name: userName
  type: ''
- container: ''
  name: manifest
  type: ''
- container: ''
  name: tagId
  type: ''
- container: ''
  name: color
  type: ''
- container: ''
  name: workspaceId
  type: ''
- container: ''
  name: regionId
  type: ''
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: permissionId
  type: ''
- container: ''
  name: permissionType
  type: ''
- container: ''
  name: scopeId
  type: ''
- container: ''
  name: scope
  type: ''
- container: ''
  name: previous
  type: ''
- container: ''
  name: next
  type: ''
- container: set
  name: data
  type: string
- container: ''
  name: allowedOrigin
  type: ''
- container: ''
  name: externalUserId
  type: ''
- container: ''
  name: organizationId
  type: ''
- container: ''
  name: conditions
  type: ''
- container: ''
  name: token
  type: ''
- container: ''
  name: sourceType
  type: ''
- container: ''
  name: redirectUrl
  type: ''
- container: ''
  name: oAuthInputConfiguration
  type: ''
- container: set
  name: requestedScopes
  type: string
- container: set
  name: requestedOptionalScopes
  type: string
- container: ''
  name: type
  type: ''
- container: ''
  name: configuration
  type: ''
- container: ''
  name: resourceAllocation
  type: ''
- container: ''
  name: url
  type: ''
- container: ''
  name: connectionId
  type: ''
- container: ''
  name: sourceId
  type: ''
- container: ''
  name: destinationId
  type: ''
- container: ''
  name: status
  type: ''
- container: ''
  name: schedule
  type: ''
- container: ''
  name: nonBreakingSchemaUpdatesBehavior
  type: ''
- container: ''
  name: namespaceDefinition
  type: ''
- container: ''
  name: namespaceFormat
  type: ''
- container: ''
  name: prefix
  type: ''
- container: ''
  name: configurations
  type: ''
- container: ''
  name: createdAt
  type: ''
- container: set
  name: tags
  type: string
- container: ''
  name: statusReason
  type: ''
- container: ''
  name: definitionId
  type: ''
- container: ''
  name: dataplaneId
  type: ''
- container: ''
  name: updatedAt
  type: ''
- container: ''
  name: id
  type: ''
- container: ''
  name: jobType
  type: ''
- container: ''
  name: resourceRequirements
  type: ''
- container: ''
  name: newFieldName
  type: ''
- container: ''
  name: originalFieldName
  type: ''
- container: ''
  name: organizationName
  type: ''
- container: ''
  name: permission
  type: ''
- container: ''
  name: namespace
  type: ''
- container: ''
  name: syncMode
  type: ''
- container: set
  name: cursorField
  type: string
- container: set
  name: primaryKey
  type: string
- container: ''
  name: includeFiles
  type: boolean
- container: ''
  name: destinationObjectName
  type: ''
- container: ''
  name: selectedFields
  type: ''
- container: set
  name: mappers
  type: string
- container: ''
  name: dataResidency
  type: ''
- container: ''
  name: notifications
  type: ''
- container: set
  name: organizations
  type: string
- container: ''
  name: dockerRepository
  type: ''
- container: ''
  name: dockerImageTag
  type: ''
- container: ''
  name: documentationUrl
  type: ''
- container: ''
  name: actorType
  type: ''
- container: ''
  name: streamName
  type: ''
- container: set
  name: syncModes
  type: string
- container: ''
  name: streamnamespace
  type: ''
- container: set
  name: defaultCursorField
  type: string
- container: ''
  name: sourceDefinedCursorField
  type: boolean
- container: set
  name: sourceDefinedPrimaryKey
  type: string
- container: set
  name: propertyFields
  type: string
- container: ''
  name: failure
  type: ''
- container: ''
  name: success
  type: ''
- container: ''
  name: connectionUpdate
  type: ''
- container: ''
  name: connectionUpdateActionRequired
  type: ''
- container: ''
  name: syncDisabled
  type: ''
- container: ''
  name: syncDisabledWarning
  type: ''
- container: set
  name: fieldPath
  type: string
- container: ''
  name: clientId
  type: ''
- container: ''
  name: clientSecret
  type: ''
- container: ''
  name: grant-type
  type: ''
- container: ''
  name: description
  type: ''
- container: ''
  name: destinationType
  type: ''
- container: ''
  name: version
  type: ''
- container: ''
  name: default
  type: ''
- container: set
  name: jobSpecific
  type: string
- container: ''
  name: mapperConfiguration
  type: ''
- container: ''
  name: secretId
  type: ''
- container: set
  name: applications
  type: string
- container: ''
  name: scheduleType
  type: ''
- container: ''
  name: cronExpression
  type: ''
- container: ''
  name: publicKey
  type: ''
- container: ''
  name: jobId
  type: ''
- container: ''
  name: startTime
  type: ''
- container: ''
  name: lastUpdatedAt
  type: ''
- container: ''
  name: duration
  type: ''
- container: ''
  name: bytesSynced
  type: ''
- container: ''
  name: rowsSynced
  type: ''
- container: ''
  name: basicTiming
  type: ''
- container: ''
  name: connectorDefinitionType
  type: ''
- container: ''
  name: comparisonValue
  type: ''
- container: ''
  name: fieldName
  type: ''
- container: ''
  name: accessToken
  type: ''
- container: ''
  name: tokenType
  type: ''
- container: ''
  name: expiresIn
  type: ''
- container: ''
  name: method
  type: ''
- container: ''
  name: memberCount
  type: ''
property_count: 129
provider_name: Airbyte
provider_slug: airbyte
slug: airbyte-context
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 49
classes:
- AssociationLabels
- Oauth2AuthorizationCode
- PatchApiKeyRequest
- Project
- name
- HydratedRevision
- Destination
- FieldDefinition
- description
- UpsertMetadataRequest
- NotificationEventTopicRoute
- BillingAccount
- BuilderInfo
- WebhookHeaders
- ProviderAppMetadata
- JWTKeyResponse
- Oauth2AuthorizationCodeTokensOnly
- StringFieldOptions
- Org
- UpsertMetadataResponse
- UpdateConnectionRequest
- Topic
- ProviderMetadataInfo
- BackfillProgress
- ConnectionRequest
- ApiKeyRequest
- PatchJWTKeyRequest
- ApiKey
- SignedUrl
- url
- ProviderMetadata
- DestinationWithSecrets
- Integration
- Config
- AssociationDefinition
- Installation
- TopicDestinationRoute
- Revision
- FieldUpsertResult
- NumericFieldOptions
- JSONPatchOperation
- ClaimedDomainResponse
- PaginationInfo
- Builder
- CreateJWTKeyRequest
- ProviderApp
- Invite
- ObjectMetadata
- JWTKey
context_file: json-ld/ampersand-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/ampersand/refs/heads/main/json-ld/ampersand-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Ampersand Api from Ampersand.
layout: jsonld
name: Ampersand Api Context
namespaces:
- prefix: amp
  uri: https://withampersand.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: singular
  type: string
- container: ''
  name: plural
  type: string
- container: ''
  name: accessToken
  type: reference
- container: ''
  name: refreshToken
  type: reference
- container: set
  name: scopes
  type: string
- container: set
  name: updateMask
  type: string
- container: ''
  name: apiKey
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: appName
  type: string
- container: ''
  name: orgId
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: updateTime
  type: dateTime
- container: ''
  name: entitlements
  type: reference
- container: ''
  name: specVersion
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: fieldName
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: valueType
  type: string
- container: ''
  name: required
  type: boolean
- container: ''
  name: unique
  type: boolean
- container: ''
  name: indexed
  type: boolean
- container: ''
  name: stringOptions
  type: string
- container: ''
  name: numericOptions
  type: string
- container: ''
  name: association
  type: string
- container: ''
  name: groupRef
  type: string
- container: ''
  name: fields
  type: reference
- container: ''
  name: eventType
  type: string
- container: ''
  name: topicId
  type: string
- container: ''
  name: projectId
  type: string
- container: ''
  name: billingProvider
  type: string
- container: ''
  name: billingProviderRef
  type: string
- container: ''
  name: builder
  type: string
- container: ''
  name: projectRoles
  type: reference
- container: ''
  name: orgRole
  type: reference
- container: ''
  name: authQueryParams
  type: reference
- container: ''
  name: providerParams
  type: reference
- container: ''
  name: kid
  type: string
- container: ''
  name: length
  type: integer
- container: ''
  name: pattern
  type: string
- container: set
  name: values
  type: string
- container: ''
  name: valuesRestricted
  type: boolean
- container: ''
  name: defaultValue
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: defaultTeamId
  type: string
- container: ''
  name: success
  type: boolean
- container: ''
  name: connection
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: installationId
  type: string
- container: ''
  name: objectName
  type: string
- container: ''
  name: operationId
  type: string
- container: ''
  name: recordsProcessed
  type: integer
- container: ''
  name: recordsEstimatedTotal
  type: integer
- container: ''
  name: providerWorkspaceRef
  type: string
- container: ''
  name: providerMetadata
  type: string
- container: ''
  name: groupName
  type: string
- container: ''
  name: consumerName
  type: string
- container: ''
  name: consumerRef
  type: string
- container: ''
  name: provider
  type: string
- container: ''
  name: customAuth
  type: reference
- container: ''
  name: basicAuth
  type: reference
- container: ''
  name: oauth2ClientCredentials
  type: reference
- container: ''
  name: oauth2PasswordCredentials
  type: reference
- container: ''
  name: oauth2AuthorizationCode
  type: string
- container: ''
  name: jwtKey
  type: reference
- container: ''
  name: key
  type: string
- container: ''
  name: active
  type: boolean
- container: ''
  name: bucket
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: secrets
  type: reference
- container: ''
  name: latestRevision
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: createdBy
  type: string
- container: ''
  name: associationType
  type: string
- container: ''
  name: targetObject
  type: string
- container: ''
  name: targetField
  type: string
- container: ''
  name: cardinality
  type: string
- container: ''
  name: onDelete
  type: string
- container: ''
  name: reverseLookupFieldName
  type: string
- container: ''
  name: labels
  type: string
- container: ''
  name: integrationId
  type: string
- container: ''
  name: group
  type: string
- container: ''
  name: healthStatus
  type: string
- container: ''
  name: lastOperationStatus
  type: string
- container: ''
  name: config
  type: string
- container: ''
  name: destinationId
  type: string
- container: ''
  name: action
  type: string
- container: set
  name: warnings
  type: string
- container: ''
  name: precision
  type: integer
- container: ''
  name: scale
  type: integer
- container: ''
  name: min
  type: decimal
- container: ''
  name: max
  type: decimal
- container: ''
  name: op
  type: string
- container: ''
  name: parentType
  type: string
- container: ''
  name: parentId
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: done
  type: boolean
- container: ''
  name: nextPageToken
  type: string
- container: ''
  name: idpProvider
  type: string
- container: ''
  name: idpRef
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: fullName
  type: string
- container: ''
  name: primaryEmail
  type: string
- container: ''
  name: algorithm
  type: string
- container: ''
  name: publicKeyPem
  type: string
- container: ''
  name: externalRef
  type: string
- container: ''
  name: clientId
  type: string
- container: ''
  name: invitedEmail
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: mappedObjectName
  type: string
property_count: 113
provider_name: Ampersand
provider_slug: ampersand
slug: ampersand-api-context
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
- JSON-LD
- Linked Data
- Semantic Web
---

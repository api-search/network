---
class_count: 92
classes:
- CreateAccessTokenResponse
- CreateDevEnvironmentResponse
- RepositoryInput
- IdeConfiguration
- CreateProjectResponse
- CreateSourceRepositoryResponse
- CreateSourceRepositoryBranchResponse
- DeleteAccessTokenResponse
- DeleteDevEnvironmentResponse
- DeleteProjectResponse
- DeleteSourceRepositoryResponse
- DeleteSpaceResponse
- GetDevEnvironmentResponse
- GetProjectResponse
- GetSourceRepositoryResponse
- GetSourceRepositoryCloneUrlsResponse
- GetSpaceResponse
- GetSubscriptionResponse
- GetUserDetailsResponse
- ListAccessTokensResponse
- ListDevEnvironmentSessionsResponse
- ListDevEnvironmentsResponse
- Filter
- ListEventLogsResponse
- ListProjectsResponse
- ProjectListFilter
- ListSourceRepositoriesResponse
- ListSourceRepositoryBranchesResponse
- ListSpacesResponse
- StartDevEnvironmentResponse
- StartDevEnvironmentSessionResponse
- ExecuteCommandSessionConfiguration
- StopDevEnvironmentResponse
- StopDevEnvironmentSessionResponse
- UpdateDevEnvironmentResponse
- UpdateProjectResponse
- UpdateSpaceResponse
- VerifySessionResponse
- AccessTokenSummary
- CreateAccessTokenRequest
- PersistentStorageConfiguration
- CreateDevEnvironmentRequest
- CreateProjectRequest
- CreateSourceRepositoryBranchRequest
- CreateSourceRepositoryRequest
- DeleteAccessTokenRequest
- DeleteDevEnvironmentRequest
- DeleteProjectRequest
- DeleteSourceRepositoryRequest
- DeleteSpaceRequest
- DevEnvironmentAccessDetails
- DevEnvironmentRepositorySummary
- DevEnvironmentSessionConfiguration
- DevEnvironmentSessionSummary
- PersistentStorage
- DevEnvironmentSummary
- EmailAddress
- EventLogEntry
- UserIdentity
- ProjectInformation
- EventPayload
- GetDevEnvironmentRequest
- GetProjectRequest
- GetSourceRepositoryCloneUrlsRequest
- GetSourceRepositoryRequest
- GetSpaceRequest
- GetSubscriptionRequest
- GetUserDetailsRequest
- Ide
- ListAccessTokensRequest
- ListDevEnvironmentSessionsRequest
- ListDevEnvironmentsRequest
- ListEventLogsRequest
- ListProjectsRequest
- ListSourceRepositoriesItem
- ListSourceRepositoriesRequest
- ListSourceRepositoryBranchesItem
- ListSourceRepositoryBranchesRequest
- ListSpacesRequest
- ProjectSummary
- SpaceSummary
- StartDevEnvironmentRequest
- StartDevEnvironmentSessionRequest
- StopDevEnvironmentRequest
- StopDevEnvironmentSessionRequest
- UpdateDevEnvironmentRequest
- UpdateProjectRequest
- UpdateSpaceRequest
- name
- description
- version
- email
context_file: json-ld/amazon-codecatalyst-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codecatalyst/refs/heads/main/json-ld/amazon-codecatalyst-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codecatalyst from Amazon CodeCatalyst.
layout: jsonld
name: Amazon Codecatalyst Context
namespaces:
- prefix: amazon-code-catalyst
  uri: https://amazon-code-catalyst.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: secret
  type: string
- container: ''
  name: expiresTime
  type: string
- container: ''
  name: accessTokenId
  type: string
- container: ''
  name: spaceName
  type: string
- container: ''
  name: projectName
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: repositoryName
  type: string
- container: ''
  name: branchName
  type: string
- container: ''
  name: runtime
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: ref
  type: string
- container: ''
  name: lastUpdatedTime
  type: string
- container: ''
  name: headCommitId
  type: string
- container: ''
  name: creatorId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: string
- container: ''
  name: repositories
  type: string
- container: ''
  name: alias
  type: string
- container: ''
  name: ides
  type: string
- container: ''
  name: instanceType
  type: string
- container: ''
  name: inactivityTimeoutMinutes
  type: string
- container: ''
  name: persistentStorage
  type: string
- container: ''
  name: createdTime
  type: string
- container: ''
  name: https
  type: string
- container: ''
  name: regionName
  type: string
- container: ''
  name: subscriptionType
  type: string
- container: ''
  name: awsAccountName
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: userName
  type: string
- container: ''
  name: primaryEmail
  type: string
- container: ''
  name: items
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: values
  type: string
- container: ''
  name: comparisonOperator
  type: string
- container: ''
  name: accessDetails
  type: string
- container: ''
  name: sessionId
  type: string
- container: ''
  name: command
  type: string
- container: ''
  name: arguments
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: identity
  type: string
- container: ''
  name: sizeInGiB
  type: string
- container: ''
  name: streamUrl
  type: string
- container: ''
  name: tokenValue
  type: string
- container: ''
  name: sessionType
  type: string
- container: ''
  name: executeCommandSessionConfiguration
  type: string
- container: ''
  name: devEnvironmentId
  type: string
- container: ''
  name: startedTime
  type: string
- container: ''
  name: verified
  type: string
- container: ''
  name: eventName
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: eventCategory
  type: string
- container: ''
  name: eventSource
  type: string
- container: ''
  name: eventTime
  type: string
- container: ''
  name: operationType
  type: string
- container: ''
  name: userIdentity
  type: string
- container: ''
  name: projectInformation
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: requestPayload
  type: string
- container: ''
  name: responsePayload
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: sourceIpAddress
  type: string
- container: ''
  name: userAgent
  type: string
- container: ''
  name: userType
  type: string
- container: ''
  name: principalId
  type: string
- container: ''
  name: awsAccountId
  type: string
- container: ''
  name: projectId
  type: string
- container: ''
  name: contentType
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: filters
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: sessionConfiguration
  type: string
property_count: 74
provider_name: Amazon CodeCatalyst
provider_slug: amazon-codecatalyst
slug: amazon-codecatalyst-context
tags:
- Amazon
- AWS
- Developer Tools
- CI/CD
- Collaboration
- DevOps
- Source Control
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 19
classes:
- Collaboration
- name
- description
- Membership
- ProtectedQuery
- ConfiguredTable
- ListCollaborationsResponse
- CreateCollaborationRequest
- CreateCollaborationResponse
- GetCollaborationResponse
- ListMembershipsResponse
- CreateMembershipRequest
- CreateMembershipResponse
- ListProtectedQueriesResponse
- StartProtectedQueryRequest
- StartProtectedQueryResponse
- ListConfiguredTablesResponse
- CreateConfiguredTableRequest
- CreateConfiguredTableResponse
context_file: json-ld/amazon-clean-rooms-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-clean-rooms/refs/heads/main/json-ld/amazon-clean-rooms-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Clean Rooms from Amazon Clean Rooms.
layout: jsonld
name: Amazon Clean Rooms Context
namespaces:
- prefix: cleanrooms
  uri: https://aws.amazon.com/clean-rooms/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: creatorAccountId
  type: string
- container: ''
  name: creatorDisplayName
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: updateTime
  type: dateTime
- container: ''
  name: queryLogStatus
  type: string
- container: ''
  name: collaborationArn
  type: string
- container: ''
  name: collaborationId
  type: string
- container: ''
  name: collaborationCreatorAccountId
  type: string
- container: ''
  name: collaborationName
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: membershipId
  type: string
- container: ''
  name: membershipArn
  type: string
- container: ''
  name: analysisMethod
  type: string
- container: ''
  name: nextToken
  type: string
- container: set
  name: collaborationList
  type: string
- container: set
  name: members
  type: string
- container: set
  name: creatorMemberAbilities
  type: string
- container: ''
  name: collaboration
  type: string
- container: set
  name: membershipList
  type: string
- container: ''
  name: collaborationIdentifier
  type: string
- container: ''
  name: membership
  type: string
- container: set
  name: protectedQueries
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: sqlParameters
  type: string
- container: ''
  name: resultConfiguration
  type: string
- container: ''
  name: protectedQuery
  type: string
- container: set
  name: configuredTableList
  type: string
- container: ''
  name: tableReference
  type: string
- container: set
  name: allowedColumns
  type: string
- container: ''
  name: configuredTable
  type: string
property_count: 32
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
slug: amazon-clean-rooms-context
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
- JSON-LD
- Linked Data
- Semantic Web
---

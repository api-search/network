---
class_count: 9
classes:
- Team
- Channel
- ChatMessage
- ConversationMember
- OnlineMeeting
- Call
- name
- description
- email
context_file: json-ld/microsoft-teams-graph-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/microsoft-teams/refs/heads/main/json-ld/microsoft-teams-graph-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Microsoft Teams Graph Api from Microsoft Teams.
layout: jsonld
name: Microsoft Teams Graph Api Context
namespaces:
- prefix: ms
  uri: https://graph.microsoft.com/schema/
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
  name: displayName
  type: string
- container: ''
  name: visibility
  type: string
- container: ''
  name: isArchived
  type: boolean
- container: ''
  name: createdDateTime
  type: dateTime
- container: ''
  name: lastModifiedDateTime
  type: dateTime
- container: ''
  name: webUrl
  type: reference
- container: ''
  name: membershipType
  type: string
- container: ''
  name: messageType
  type: string
- container: ''
  name: importance
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: body
  type: reference
- container: ''
  name: from
  type: reference
- container: set
  name: roles
  type: ''
- container: ''
  name: userId
  type: string
- container: ''
  name: startDateTime
  type: dateTime
- container: ''
  name: endDateTime
  type: dateTime
- container: ''
  name: joinWebUrl
  type: reference
- container: ''
  name: state
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: callbackUri
  type: reference
- container: set
  name: requestedModalities
  type: ''
property_count: 22
provider_name: Microsoft Teams
provider_slug: microsoft-teams
slug: microsoft-teams-graph-api-context
tags:
- Chat
- Collaboration
- Communication
- Microsoft 365
- Productivity
- Video Conferencing
- JSON-LD
- Linked Data
- Semantic Web
---

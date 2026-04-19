---
class_count: 25
classes:
- User
- UpdateUserRequest
- UpdateFolderRequest
- ConnectionList
- Piece
- CreateProjectRequest
- QueueMetrics
- Connection
- FlowRunList
- FolderList
- UpsertConnectionRequest
- Folder
- UserList
- Template
- FlowRun
- UpdateProjectRequest
- CreateTemplateRequest
- TemplateList
- ProjectList
- Flow
- Project
- CreateFlowRequest
- CreateFolderRequest
- FlowList
- UpdateFlowRequest
context_file: json-ld/activepieces-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/json-ld/activepieces-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Activepieces from Activepieces.
layout: jsonld
name: Activepieces Context
namespaces:
- prefix: activepieces
  uri: https://www.activepieces.com/schema/
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
  name: created
  type: dateTime
- container: ''
  name: updated
  type: dateTime
- container: ''
  name: email
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: platformRole
  type: string
- container: ''
  name: displayName
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: next
  type: string
- container: ''
  name: previous
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: iconUrl
  type: reference
- container: set
  name: categories
  type: string
- container: set
  name: queues
  type: string
- container: ''
  name: pieceName
  type: string
- container: ''
  name: projectId
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: flowId
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: finishTime
  type: dateTime
- container: ''
  name: duration
  type: integer
- container: ''
  name: notifyStatus
  type: string
- container: ''
  name: externalId
  type: string
- container: ''
  name: folderId
  type: string
- container: ''
  name: publishedVersionId
  type: string
- container: ''
  name: ownerId
  type: string
- container: ''
  name: platformId
  type: string
- container: ''
  name: templateId
  type: string
- container: ''
  name: metadata
  type: string
property_count: 35
provider_name: Activepieces
provider_slug: activepieces
slug: activepieces-context
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
- JSON-LD
- Linked Data
- Semantic Web
---

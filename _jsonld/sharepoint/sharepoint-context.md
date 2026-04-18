---
class_count: 11
classes:
- File
- FileCollection
- List
- ListCollection
- ListCreateRequest
- ListItem
- ListItemCollection
- ListItemCreateRequest
- SearchResult
- UserProfile
- Web
context_file: json-ld/sharepoint-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/sharepoint/refs/heads/main/json-ld/sharepoint-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Sharepoint from Microsoft SharePoint.
layout: jsonld
name: Sharepoint Context
namespaces:
- prefix: sp
  uri: https://learn.microsoft.com/en-us/sharepoint/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: AccountName
  type: string
- container: ''
  name: AllowContentTypes
  type: boolean
- container: ''
  name: AuthorId
  type: integer
- container: ''
  name: BaseTemplate
  type: integer
- container: ''
  name: CheckOutType
  type: integer
- container: ''
  name: ContentTypesEnabled
  type: boolean
- container: ''
  name: Created
  type: dateTime
- container: ''
  name: Department
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: DisplayName
  type: string
- container: ''
  name: EditorId
  type: integer
- container: ''
  name: Email
  type: string
- container: ''
  name: EnableVersioning
  type: boolean
- container: ''
  name: Hidden
  type: boolean
- container: ''
  name: Id
  type: string
- container: ''
  name: ItemCount
  type: integer
- container: ''
  name: Language
  type: integer
- container: ''
  name: LastItemModifiedDate
  type: dateTime
- container: ''
  name: Length
  type: integer
- container: ''
  name: MajorVersion
  type: integer
- container: ''
  name: MinorVersion
  type: integer
- container: ''
  name: Modified
  type: dateTime
- container: ''
  name: Name
  type: string
- container: ''
  name: PersonalUrl
  type: string
- container: ''
  name: PictureUrl
  type: string
- container: ''
  name: PrimaryQueryResult
  type: reference
- container: ''
  name: ServerRelativeUrl
  type: string
- container: ''
  name: TimeCreated
  type: dateTime
- container: ''
  name: TimeLastModified
  type: dateTime
- container: ''
  name: Title
  type: string
- container: ''
  name: UniqueId
  type: string
- container: ''
  name: Url
  type: string
- container: ''
  name: WebTemplate
  type: string
- container: ''
  name: __metadata
  type: reference
- container: set
  name: value
  type: string
property_count: 35
provider_name: Microsoft SharePoint
provider_slug: sharepoint
slug: sharepoint-context
tags:
- Collaboration
- Document Management
- Enterprise Content Management
- Intranet
- Microsoft
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 10
classes:
- EnvironmentCollection
- Environment
- GroupCollection
- GroupCreateRequest
- Group
- PermissionCollection
- Permission
- UserCollection
- UserCreateRequest
- User
context_file: json-ld/dynatrace-account-management-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/json-ld/dynatrace-account-management-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Dynatrace Account Management Api from Dynatrace.
layout: jsonld
name: Dynatrace Account Management Api Context
namespaces:
- prefix: dt
  uri: https://dt.dynatrace.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: nextPageKey
  type: string
- container: ''
  name: totalCount
  type: integer
- container: set
  name: environments
  type: ''
- container: ''
  name: id
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: trial
  type: boolean
- container: set
  name: items
  type: ''
- container: ''
  name: description
  type: string
- container: ''
  name: groupId
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: set
  name: permissions
  type: ''
- container: ''
  name: permissionName
  type: string
- container: ''
  name: scope
  type: string
- container: ''
  name: scopeType
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: set
  name: groups
  type: ''
- container: ''
  name: uid
  type: string
- container: ''
  name: userStatus
  type: string
property_count: 23
provider_name: Dynatrace
provider_slug: dynatrace
slug: dynatrace-account-management-api-context
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 18
classes:
- Activity
- Contact
- Task
- Tenant
- SearchResults
- User
- OfferingItem
- HardwareNode
- Agent
- Quota
- Report
- Client
- TokenResponse
- UsageItem
- AgentUpdateSettings
- AgentOS
- email
- name
context_file: json-ld/acronis-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/json-ld/acronis-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Acronis from Acronis.
layout: jsonld
name: Acronis Context
namespaces:
- prefix: acronis
  uri: https://developer.acronis.com/schema/
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
  name: type
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: result_code
  type: string
- container: ''
  name: parent_activity_id
  type: string
- container: ''
  name: task_id
  type: string
- container: ''
  name: sustainable
  type: boolean
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: firstname
  type: string
- container: ''
  name: lastname
  type: string
- container: ''
  name: phone
  type: string
- container: ''
  name: address1
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: uuid
  type: reference
- container: ''
  name: priority
  type: string
- container: ''
  name: policy_id
  type: reference
- container: ''
  name: resource_id
  type: reference
- container: ''
  name: executor_id
  type: string
- container: ''
  name: enqueuedAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: tenant_id
  type: reference
- container: ''
  name: kind
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: parent_id
  type: reference
- container: ''
  name: customer_type
  type: string
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: version
  type: integer
- container: ''
  name: contact
  type: string
- container: set
  name: items
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: login
  type: string
- container: ''
  name: application_id
  type: reference
- container: ''
  name: status
  type: integer
- container: ''
  name: quota
  type: string
- container: ''
  name: edition
  type: string
- container: ''
  name: hostname
  type: string
- container: ''
  name: os
  type: string
- container: ''
  name: last_seen
  type: dateTime
- container: ''
  name: registration_time
  type: dateTime
- container: ''
  name: value
  type: decimal
- container: ''
  name: overage
  type: decimal
- container: ''
  name: schedule
  type: string
- container: ''
  name: parameters
  type: string
- container: ''
  name: client_id
  type: string
- container: ''
  name: client_secret
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: access_token
  type: string
- container: ''
  name: token_type
  type: string
- container: ''
  name: expires_in
  type: integer
- container: ''
  name: refresh_token
  type: string
- container: ''
  name: scope
  type: string
- container: ''
  name: offering_item
  type: string
- container: ''
  name: update_channel
  type: string
- container: ''
  name: automatic
  type: boolean
- container: ''
  name: maintenance_window
  type: string
- container: ''
  name: family
  type: string
- container: ''
  name: arch
  type: string
property_count: 61
provider_name: Acronis
provider_slug: acronis
slug: acronis-context
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
- JSON-LD
- Linked Data
- Semantic Web
---

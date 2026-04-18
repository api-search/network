---
class_count: 67
classes:
- id
- type
- Company
- Property
- Rule
- RuleComponent
- DataElement
- Extension
- ExtensionPackage
- Library
- Build
- Environment
- Host
- Callback
- Secret
- AuditEvent
- attributes
- relationships
- links
- meta
- name
- description
- version
- enabled
- published
- dirty
- privacy
- ssl_enabled
- development
- rule_component_sequencing_enabled
- undefined_vars_return_empty
- delegate_descriptor_id
- settings
- default_value
- storage_duration
- force_lower_case
- clean_text
- order
- rule_order
- timeout
- delay_next
- negate
- display_name
- author
- availability
- discontinued
- state
- build_required
- status
- token
- error_message
- stage
- archive
- path
- library_name
- library_path
- type_of
- server
- port
- username
- encrypted_private_key
- skip_symlinks
- credentials
- revision_number
- org_id
- cjm_enabled
- edge_enabled
context_file: json-ld/context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/json-ld/context.jsonld
description: JSON-LD context defining the semantic vocabulary for context from Adobe Launch.
layout: jsonld
name: context Context
namespaces:
- prefix: adobe
  uri: https://ns.adobe.com/experience-platform/tags/
- prefix: jsonapi
  uri: https://jsonapi.org/format/#document-
- prefix: xdm
  uri: https://ns.adobe.com/xdm/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
properties:
- container: ''
  name: url
  type: reference
- container: ''
  name: platform
  type: string
- container: list
  name: domains
  type: ''
- container: ''
  name: exchange_url
  type: reference
- container: list
  name: subscriptions
  type: ''
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: deleted_at
  type: dateTime
- container: ''
  name: published_at
  type: dateTime
- container: ''
  name: property
  type: reference
- container: ''
  name: company
  type: reference
- container: ''
  name: extension
  type: reference
- container: ''
  name: extension_package
  type: reference
- container: set
  name: rule_components
  type: reference
- container: set
  name: data_elements
  type: reference
- container: set
  name: extensions
  type: reference
- container: set
  name: rules
  type: reference
- container: set
  name: libraries
  type: reference
- container: set
  name: builds
  type: reference
- container: set
  name: environments
  type: reference
- container: set
  name: hosts
  type: reference
- container: set
  name: callbacks
  type: reference
- container: set
  name: secrets
  type: reference
- container: set
  name: revisions
  type: reference
- container: ''
  name: origin
  type: reference
- container: ''
  name: environment
  type: reference
- container: ''
  name: host
  type: reference
- container: ''
  name: library
  type: reference
- container: ''
  name: self
  type: reference
- container: ''
  name: related
  type: reference
property_count: 30
provider_name: Adobe Launch
provider_slug: adobe-launch
slug: context
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
- JSON-LD
- Linked Data
- Semantic Web
---

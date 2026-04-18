---
class_count: 7
classes:
- sys_id
- sys_created_by
- sys_updated_by
- sys_mod_count
- sys_class_name
- sys_domain
- active
context_file: json-ld/servicenow-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/servicenow/refs/heads/main/json-ld/servicenow-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Servicenow from ServiceNow.
layout: jsonld
name: Servicenow Context
namespaces:
- prefix: snow
  uri: https://www.servicenow.com/ns/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: itsm
  uri: https://www.servicenow.com/ns/itsm/
properties:
- container: ''
  name: Incident
  type: ''
- container: ''
  name: ChangeRequest
  type: ''
- container: ''
  name: ConfigurationItem
  type: ''
- container: ''
  name: User
  type: ''
- container: ''
  name: CatalogRequest
  type: ''
- container: ''
  name: KnowledgeArticle
  type: ''
- container: ''
  name: sys_created_on
  type: dateTime
- container: ''
  name: sys_updated_on
  type: dateTime
property_count: 8
provider_name: ServiceNow
provider_slug: servicenow
slug: servicenow-context
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
- JSON-LD
- Linked Data
- Semantic Web
---

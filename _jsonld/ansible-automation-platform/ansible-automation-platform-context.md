---
class_count: 3
classes:
- JobTemplate
- Job
- Inventory
context_file: json-ld/ansible-automation-platform-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/ansible-automation-platform/refs/heads/main/json-ld/ansible-automation-platform-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Ansible Automation Platform from Ansible Automation Platform.
layout: jsonld
name: Ansible Automation Platform Context
namespaces:
- prefix: ansible
  uri: https://ansible.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: jobType
  type: string
- container: ''
  name: playbook
  type: string
- container: ''
  name: hostCount
  type: integer
- container: ''
  name: scmType
  type: string
- container: ''
  name: scmUrl
  type: reference
property_count: 9
provider_name: Ansible Automation Platform
provider_slug: ansible-automation-platform
slug: ansible-automation-platform-context
tags:
- Automation
- Configuration Management
- DevOps
- Infrastructure as Code
- Orchestration
- JSON-LD
- Linked Data
- Semantic Web
---

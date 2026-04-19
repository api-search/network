---
description: A conditional statement with which to compare a value, after a timestamp, before a timestamp, or equal to a string or integer. If multiple conditions are specified, the conditionals become an <code>AND</code>ed statement. If multiple values are specified for a conditional, the values are <code>OR</code>d.
layout: schema
name: Condition
properties_list:
- description: ''
  name: after
  type: object
- description: ''
  name: before
  type: object
- description: ''
  name: equals
  type: object
provider_name: Amazon Incident Manager
provider_slug: amazon-incident-manager
schema_file: json-schema/incident-manager-condition-schema.json
slug: incident-manager-condition
tags:
- Automation
- AWS
- DevOps
- Incident Management
- Operations
title: Condition
---

---
description: An employer group record.
layout: schema
name: Group
properties_list:
- description: Unique employer group identifier.
  name: group_id
  type: string
- description: Employer group name.
  name: name
  type: string
- description: Legal employer name.
  name: employer_name
  type: string
- description: Group status.
  name: status
  type: string
- description: Number of enrolled employees.
  name: employee_count
  type: integer
- description: Group effective date.
  name: effective_date
  type: string
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-group-schema.json
slug: enterprise-connect-group
tags: []
title: Group
---

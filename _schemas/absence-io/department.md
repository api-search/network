---
description: An organizational department.
layout: schema
name: Department
properties_list:
- description: Unique identifier of the department.
  name: _id
  type: string
- description: Name of the department.
  name: name
  type: string
- description: ID of the department manager.
  name: managerId
  type: string
- description: ID of the parent department if hierarchical.
  name: parentId
  type: string
provider_name: Absence.io
provider_slug: absence-io
schema_file: json-schema/department-schema.json
slug: department
tags:
- Absences
- Employees
- Leave Management
- HR
title: Department
---

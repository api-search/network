---
description: Paginated list of enrollment records.
layout: schema
name: EnrollmentList
properties_list:
- description: Array of enrollment records.
  name: items
  type: array
- description: Total number of matching enrollments.
  name: total
  type: integer
- description: Maximum number of results returned.
  name: limit
  type: integer
- description: Number of results skipped.
  name: offset
  type: integer
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-enrollment-list-schema.json
slug: enterprise-connect-enrollment-list
tags: []
title: EnrollmentList
---

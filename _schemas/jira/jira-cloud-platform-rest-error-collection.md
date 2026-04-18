---
description: Error details returned by the API.
layout: schema
name: ErrorCollection
properties_list:
- description: The list of error messages.
  name: errorMessages
  type: array
- description: Field-specific errors.
  name: errors
  type: object
- description: The HTTP status code.
  name: status
  type: integer
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-error-collection-schema.json
slug: jira-cloud-platform-rest-error-collection
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: ErrorCollection
---

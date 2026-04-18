---
description: Details of a single constraint violation in a request.
layout: schema
name: ConstraintViolation
properties_list:
- description: The JSON path to the field that caused the violation.
  name: path
  type: string
- description: A description of the constraint violation.
  name: message
  type: string
- description: The location of the violating parameter (QUERY, PATH, BODY).
  name: parameterLocation
  type: string
- description: The location detail for the violation.
  name: location
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/entities-api-v2-constraint-violation-schema.json
slug: entities-api-v2-constraint-violation
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
title: ConstraintViolation
---

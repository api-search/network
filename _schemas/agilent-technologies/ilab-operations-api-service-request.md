---
description: A service request submitted to a core facility.
layout: schema
name: Service Request
properties_list:
- description: Unique identifier for the service request.
  name: id
  type: integer
- description: Identifier of the service being requested.
  name: service_id
  type: integer
- description: Identifier of the research project to bill.
  name: project_id
  type: integer
- description: Current status of the service request.
  name: status
  type: string
- description: Number of units requested.
  name: quantity
  type: integer
- description: Additional notes or instructions for the core.
  name: notes
  type: string
- description: Timestamp when the request was submitted.
  name: submitted_at
  type: string
- description: Name of the principal investigator.
  name: principal_investigator
  type: string
provider_name: agilent-technologies
provider_slug: agilent-technologies
schema_file: json-schema/ilab-operations-api-service-request-schema.json
slug: ilab-operations-api-service-request
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
title: Service Request
---

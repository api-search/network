---
description: Request body for creating a new service request.
layout: schema
name: Service Request Create Request
properties_list:
- description: Identifier of the service to request.
  name: service_id
  type: integer
- description: Identifier of the research project to bill.
  name: project_id
  type: integer
- description: Number of units to request.
  name: quantity
  type: integer
- description: Additional notes for the core facility.
  name: notes
  type: string
provider_name: agilent-technologies
provider_slug: agilent-technologies
schema_file: json-schema/ilab-operations-api-service-request-create-request-schema.json
slug: ilab-operations-api-service-request-create-request
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
title: Service Request Create Request
---

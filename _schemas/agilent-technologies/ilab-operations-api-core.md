---
description: A core facility within an institution.
layout: schema
name: Core
properties_list:
- description: Unique identifier for the core facility.
  name: id
  type: integer
- description: Display name of the core facility.
  name: name
  type: string
- description: Name of the institution operating the core.
  name: institution
  type: string
- description: Description of the core facility's capabilities.
  name: description
  type: string
- description: Operational status of the core.
  name: status
  type: string
- description: Contact email for the core facility.
  name: contact_email
  type: string
- description: API URL for this core resource.
  name: url
  type: string
provider_name: agilent-technologies
provider_slug: agilent-technologies
schema_file: json-schema/ilab-operations-api-core-schema.json
slug: ilab-operations-api-core
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
title: Core
---

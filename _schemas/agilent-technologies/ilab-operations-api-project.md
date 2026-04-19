---
description: A research project or cost account.
layout: schema
name: Project
properties_list:
- description: Unique identifier for the project.
  name: id
  type: integer
- description: Name of the research project.
  name: name
  type: string
- description: Name of the principal investigator.
  name: pi_name
  type: string
- description: Financial account number for billing.
  name: account_number
  type: string
- description: Project status.
  name: status
  type: string
provider_name: agilent-technologies
provider_slug: agilent-technologies
schema_file: json-schema/ilab-operations-api-project-schema.json
slug: ilab-operations-api-project
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
title: Project
---

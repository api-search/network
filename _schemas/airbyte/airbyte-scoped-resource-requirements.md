---
description: actor or actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level.
layout: schema
name: ScopedResourceRequirements
properties_list:
- description: ''
  name: default
  type: object
- description: ''
  name: jobSpecific
  type: array
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-scoped-resource-requirements-schema.json
slug: airbyte-scoped-resource-requirements
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: ScopedResourceRequirements
---

---
description: HashingMapperConfiguration schema from Airbyte API
layout: schema
name: HashingMapperConfiguration
properties_list:
- description: The suffix to append to the field name after hashing.
  name: fieldNameSuffix
  type: string
- description: The hashing algorithm to use.
  name: method
  type: string
- description: The name of the field to be hashed.
  name: targetField
  type: string
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-hashing-mapper-configuration-schema.json
slug: airbyte-hashing-mapper-configuration
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: HashingMapperConfiguration
---

---
description: Specification for creating or updating an asset
layout: schema
name: AssetDefinition
properties_list:
- description: Display name of the asset
  name: name
  type: string
- description: Description of the asset
  name: description
  type: string
- description: Customer-defined unique key
  name: customerKey
  type: string
- description: ''
  name: category
  type: object
- description: Primary content of the asset
  name: content
  type: string
- description: Channel-specific content views
  name: views
  type: object
- description: Asset-type-specific data
  name: data
  type: object
- description: ''
  name: tags
  type: array
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-asset-definition-schema.json
slug: salesforce-marketing-cloud-asset-definition
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: AssetDefinition
---

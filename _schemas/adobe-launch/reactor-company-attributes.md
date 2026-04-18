---
description: ''
layout: schema
name: CompanyAttributes
properties_list:
- description: The name of the company.
  name: name
  type: string
- description: The Adobe organization ID.
  name: org_id
  type: string
- description: A unique token for the company.
  name: token
  type: string
- description: When the company was created.
  name: created_at
  type: string
- description: When the company was last updated.
  name: updated_at
  type: string
- description: Whether Customer Journey Management is enabled.
  name: cjm_enabled
  type: boolean
- description: Whether Edge capabilities are enabled.
  name: edge_enabled
  type: boolean
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/reactor-company-attributes-schema.json
slug: reactor-company-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: CompanyAttributes
---

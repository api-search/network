---
description: Export job details
layout: schema
name: ExportDetail
properties_list:
- description: Unique export identifier
  name: export_id
  type: string
- description: Export processing status
  name: status
  type: string
- description: Export file format
  name: format
  type: string
- description: Export creation timestamp
  name: created_at
  type: string
- description: Export completion timestamp
  name: completed_at
  type: string
- description: URL to download the exported file
  name: download_url
  type: string
- description: Size of the exported file in bytes
  name: file_size_bytes
  type: integer
provider_name: Circana
provider_slug: circana
schema_file: json-schema/liquid-data-export-detail-schema.json
slug: liquid-data-export-detail
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
title: ExportDetail
---

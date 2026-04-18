---
description: Request body for licensing a stock asset
layout: schema
name: LicenseRequest
properties_list:
- description: Adobe Stock content ID of the asset to license
  name: content_id
  type: integer
- description: License type to apply
  name: license
  type: string
- description: BCP 47 locale for localized response data
  name: locale
  type: string
- description: Optional purchase parameters and reference metadata
  name: purchase_params
  type: object
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-stock-license-request-schema.json
slug: adobe-creative-suite-stock-license-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: LicenseRequest
---

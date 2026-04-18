---
description: Response returned after successfully licensing a stock asset
layout: schema
name: LicenseResponse
properties_list:
- description: Content ID of the licensed asset
  name: content_id
  type: integer
- description: Details of the license purchase transaction
  name: purchase_details
  type: object
- description: URL to download the licensed full-resolution file
  name: download_url
  type: string
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-stock-license-response-schema.json
slug: adobe-creative-suite-stock-license-response
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: LicenseResponse
---

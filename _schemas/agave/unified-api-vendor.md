---
description: A vendor or subcontractor record.
layout: schema
name: Vendor
properties_list:
- description: Vendor identifier.
  name: id
  type: string
- description: Vendor name.
  name: name
  type: string
- description: Primary vendor contact email.
  name: email
  type: string
- description: Vendor phone number.
  name: phone
  type: string
- description: Vendor address.
  name: address
  type: string
- description: Vendor tax identification number.
  name: tax_id
  type: string
- description: Vendor status.
  name: status
  type: string
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-vendor-schema.json
slug: unified-api-vendor
tags:
- Accounting
- Construction
- Integration
title: Vendor
---

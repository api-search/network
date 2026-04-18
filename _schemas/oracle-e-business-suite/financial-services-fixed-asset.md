---
description: ''
layout: schema
name: FixedAsset
properties_list:
- description: Asset identifier
  name: assetId
  type: integer
- description: Asset number
  name: assetNumber
  type: string
- description: Asset description
  name: assetDescription
  type: string
- description: Asset category identifier
  name: assetCategoryId
  type: integer
- description: Asset type
  name: assetType
  type: string
- description: Serial number
  name: serialNumber
  type: string
- description: Tag number
  name: tagNumber
  type: string
- description: ''
  name: dateEffective
  type: string
- description: Date placed in service
  name: dateInService
  type: string
- description: Asset cost
  name: cost
  type: number
- description: Salvage value
  name: salvageValue
  type: number
- description: Depreciation method
  name: depreciationMethod
  type: string
- description: Useful life in months
  name: lifeInMonths
  type: integer
- description: Book type code (corporate or tax)
  name: bookTypeCode
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/financial-services-fixed-asset-schema.json
slug: financial-services-fixed-asset
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: FixedAsset
---

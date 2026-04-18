---
description: ''
layout: schema
name: Delivery
properties_list:
- description: Delivery identifier
  name: deliveryId
  type: integer
- description: Delivery name/number
  name: name
  type: string
- description: Delivery status code
  name: statusCode
  type: string
- description: Initial pickup date
  name: initialPickupDate
  type: string
- description: Ultimate dropoff date
  name: ultimateDropoffDate
  type: string
- description: Customer identifier
  name: customerId
  type: integer
- description: Ship-to location identifier
  name: shipToLocationId
  type: integer
- description: Carrier identifier
  name: carrierId
  type: integer
- description: Ship method code
  name: shipMethodCode
  type: string
- description: Waybill/tracking number
  name: waybill
  type: string
- description: Gross weight
  name: grossWeight
  type: number
- description: Weight unit of measure
  name: weightUomCode
  type: string
- description: Volume
  name: volume
  type: number
- description: Volume unit of measure
  name: volumeUomCode
  type: string
- description: ''
  name: organizationId
  type: integer
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-delivery-schema.json
slug: supply-chain-delivery
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Delivery
---

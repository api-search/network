---
description: Request body for creating a self-service price estimate session
layout: schema
name: PriceEstimateSelfServiceRequest
properties_list:
- description: Type of insurance product for the estimate
  name: product_type
  type: string
- description: ''
  name: vehicle
  type: object
- description: Age of the primary driver for car insurance
  name: driver_age
  type: integer
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-price-estimate-self-service-request-schema.json
slug: api-connect-price-estimate-self-service-request
tags:
- Financial Services
- Insurance
- Asset Management
title: PriceEstimateSelfServiceRequest
---

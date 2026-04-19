---
description: An AWS Data Exchange data set containing a collection of data available for subscription.
layout: schema
name: Data Set
properties_list:
- description: The unique identifier of the data set
  name: Id
  type: string
- description: The ARN of the data set
  name: Arn
  type: string
- description: The name of the data set
  name: Name
  type: string
- description: The description of the data set
  name: Description
  type: string
- description: ''
  name: AssetType
  type: string
- description: ''
  name: Origin
  type: string
- description: ''
  name: Tags
  type: object
- description: ''
  name: CreatedAt
  type: string
- description: ''
  name: UpdatedAt
  type: string
provider_name: Amazon Data Exchange
provider_slug: amazon-data-exchange
schema_file: json-schema/data-set-schema.json
slug: data-set
tags:
- AWS
- Data Exchange
- Data Marketplace
- Third-Party Data
- Analytics
- Subscriptions
title: Data Set
---

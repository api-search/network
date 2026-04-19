---
description: Represents a B2B Data Interchange partnership — a connection between a customer profile and a trading partner with associated EDI capabilities.
layout: schema
name: Partnership
properties_list:
- description: Unique identifier for the partnership
  name: partnershipId
  type: string
- description: Amazon Resource Name (ARN) for the partnership
  name: partnershipArn
  type: string
- description: Identifier of the profile associated with this partnership
  name: profileId
  type: string
- description: Name of the partnership
  name: name
  type: string
- description: Email address of the trading partner contact
  name: email
  type: string
- description: Phone number of the trading partner contact
  name: phone
  type: string
- description: List of capability IDs associated with this partnership
  name: capabilities
  type: array
- description: Identifier assigned to the trading partner
  name: tradingPartnerId
  type: string
- description: Timestamp when the partnership was created
  name: createdAt
  type: string
- description: Timestamp when the partnership was last modified
  name: modifiedAt
  type: string
provider_name: Amazon B2B Data Interchange
provider_slug: amazon-b2b-data-interchange
schema_file: json-schema/partnership.json
slug: partnership
tags:
- EDI
- B2B
- Data Interchange
- Supply Chain
- Healthcare
- Financial Services
- Amazon Web Services
- AWS
title: Partnership
---

---
description: SOAP fault response indicating an error during operation processing.
layout: schema
name: SOAPFault
properties_list:
- description: Fault code identifying the error category.
  name: faultcode
  type: string
- description: Human-readable description of the error.
  name: faultstring
  type: string
- description: Additional error details.
  name: detail
  type: string
provider_name: Adobe Campaign
provider_slug: adobe-campaign
schema_file: json-schema/adobe-campaign-classic-soap-fault-schema.json
slug: adobe-campaign-classic-soap-fault
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
title: SOAPFault
---

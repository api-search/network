---
description: Request to bind a quoted policy
layout: schema
name: BindRequest
properties_list:
- description: Agent electronic signature confirming bind intent
  name: agent_signature
  type: string
- description: Payment method for premium
  name: payment_method
  type: string
- description: Optional notes for the policy
  name: additional_notes
  type: string
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
schema_file: json-schema/amtrust-financial-services-bind-request-schema.json
slug: amtrust-financial-services-bind-request
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
title: BindRequest
---

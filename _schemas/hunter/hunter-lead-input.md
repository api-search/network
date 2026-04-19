---
description: ''
layout: schema
name: LeadInput
properties_list:
- description: Email address of the lead.
  name: email
  type: string
- description: First name of the lead.
  name: first_name
  type: string
- description: Last name of the lead.
  name: last_name
  type: string
- description: Job position or title.
  name: position
  type: string
- description: Company name.
  name: company
  type: string
- description: Industry of the company.
  name: company_industry
  type: string
- description: Size range of the company.
  name: company_size
  type: string
- description: Confidence score for the lead email.
  name: confidence_score
  type: integer
- description: Website URL associated with the lead.
  name: website
  type: string
- description: ISO 3166-1 alpha-2 country code.
  name: country_code
  type: string
- description: LinkedIn profile URL.
  name: linkedin_url
  type: string
- description: Phone number.
  name: phone_number
  type: string
- description: Twitter handle.
  name: twitter
  type: string
- description: Free-text notes about the lead.
  name: notes
  type: string
- description: Identifier of the leads list to add the lead to.
  name: leads_list_id
  type: integer
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-lead-input-schema.json
slug: hunter-lead-input
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: LeadInput
---

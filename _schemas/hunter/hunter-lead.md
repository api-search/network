---
description: ''
layout: schema
name: Lead
properties_list:
- description: Unique identifier for the lead.
  name: id
  type: integer
- description: Email address of the lead.
  name: email
  type: string
- description: First name of the lead.
  name: first_name
  type: '[''string'', ''null'']'
- description: Last name of the lead.
  name: last_name
  type: '[''string'', ''null'']'
- description: Job position or title.
  name: position
  type: '[''string'', ''null'']'
- description: Company name.
  name: company
  type: '[''string'', ''null'']'
- description: Industry of the company.
  name: company_industry
  type: '[''string'', ''null'']'
- description: Size range of the company.
  name: company_size
  type: '[''string'', ''null'']'
- description: Confidence score for the lead email.
  name: confidence_score
  type: '[''integer'', ''null'']'
- description: Website URL associated with the lead.
  name: website
  type: '[''string'', ''null'']'
- description: ISO 3166-1 alpha-2 country code.
  name: country_code
  type: '[''string'', ''null'']'
- description: LinkedIn profile URL.
  name: linkedin_url
  type: '[''string'', ''null'']'
- description: Phone number.
  name: phone_number
  type: '[''string'', ''null'']'
- description: Twitter handle.
  name: twitter
  type: '[''string'', ''null'']'
- description: Free-text notes about the lead.
  name: notes
  type: '[''string'', ''null'']'
- description: Identifier of the leads list the lead belongs to.
  name: leads_list_id
  type: '[''integer'', ''null'']'
- description: CRM synchronization status.
  name: sync_status
  type: '[''string'', ''null'']'
- description: Email sending status.
  name: sending_status
  type: '[''string'', ''null'']'
- description: Timestamp of the last activity for this lead.
  name: last_activity_at
  type: '[''string'', ''null'']'
- description: Timestamp of the last contact with this lead.
  name: last_contacted_at
  type: '[''string'', ''null'']'
- description: Timestamp when the lead was created.
  name: created_at
  type: string
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-lead-schema.json
slug: hunter-lead
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: Lead
---

---
description: ''
layout: schema
name: PersonEnrichment
properties_list:
- description: Unique identifier for the person record.
  name: id
  type: string
- description: ''
  name: name
  type: object
- description: Email address.
  name: email
  type: string
- description: Location description.
  name: location
  type: '[''string'', ''null'']'
- description: Time zone name.
  name: timeZone
  type: '[''string'', ''null'']'
- description: UTC offset in hours.
  name: utcOffset
  type: '[''number'', ''null'']'
- description: Short biography.
  name: bio
  type: '[''string'', ''null'']'
- description: Personal website URL.
  name: site
  type: '[''string'', ''null'']'
- description: Avatar image URL.
  name: avatar
  type: '[''string'', ''null'']'
- description: ''
  name: employment
  type: object
- description: ''
  name: facebook
  type: object
- description: ''
  name: github
  type: object
- description: ''
  name: twitter
  type: object
- description: ''
  name: linkedin
  type: object
- description: Whether the match was fuzzy.
  name: fuzzy
  type: boolean
- description: Email service provider.
  name: emailProvider
  type: '[''string'', ''null'']'
- description: Date when the record was last indexed.
  name: indexedAt
  type: '[''string'', ''null'']'
- description: Phone number.
  name: phone
  type: '[''string'', ''null'']'
- description: Date when the person was last active.
  name: activeAt
  type: '[''string'', ''null'']'
- description: Date when the person became inactive.
  name: inactiveAt
  type: '[''string'', ''null'']'
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-person-enrichment-schema.json
slug: hunter-person-enrichment
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: PersonEnrichment
---

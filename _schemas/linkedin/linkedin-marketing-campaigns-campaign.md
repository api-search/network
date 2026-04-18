---
description: Campaign from LinkedIn API
layout: schema
name: Campaign
properties_list:
- description: Unique identifier
  name: id
  type: integer
- description: Campaign name
  name: name
  type: string
- description: Parent account URN
  name: account
  type: string
- description: Parent campaign group URN
  name: campaignGroup
  type: string
- description: Campaign status
  name: status
  type: string
- description: Campaign type
  name: type
  type: string
- description: Campaign objective
  name: objectiveType
  type: string
- description: ''
  name: runSchedule
  type: object
- description: ''
  name: dailyBudget
  type: object
- description: ''
  name: totalBudget
  type: object
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-marketing-campaigns-campaign-schema.json
slug: linkedin-marketing-campaigns-campaign
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: Campaign
---

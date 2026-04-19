---
description: Paginated collection of journeys
layout: schema
name: JourneyCollection
properties_list:
- description: Total number of journeys matching the query
  name: count
  type: integer
- description: Current page number
  name: page
  type: integer
- description: Number of items per page
  name: pageSize
  type: integer
- description: ''
  name: items
  type: array
provider_name: Salesforce Marketing Cloud
provider_slug: salesforce-marketing-cloud
schema_file: json-schema/salesforce-marketing-cloud-journey-collection-schema.json
slug: salesforce-marketing-cloud-journey-collection
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
title: JourneyCollection
---

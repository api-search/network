---
description: A marketing campaign entity representing a coordinated marketing effort across channels such as email, SMS, push, and in-app, used in both Adobe Campaign and Journey Optimizer for audience targeting and message delivery.
layout: schema
name: Adobe Experience Cloud Campaign
properties_list:
- description: The unique identifier for the campaign.
  name: campaignId
  type: string
- description: The human-readable name of the campaign.
  name: name
  type: string
- description: A description of the campaign purpose and goals.
  name: description
  type: string
- description: The primary delivery channel.
  name: channel
  type: string
- description: The current status of the campaign.
  name: status
  type: string
- description: The target audience for the campaign.
  name: audience
  type: object
- description: The message content configuration.
  name: content
  type: object
- description: The campaign delivery schedule.
  name: schedule
  type: object
- description: Campaign performance metrics.
  name: metrics
  type: object
- description: When the campaign was created.
  name: created
  type: string
- description: When the campaign was last modified.
  name: lastModified
  type: string
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
schema_file: json-schema/adobe-experience-cloud-campaign.json
slug: adobe-experience-cloud-campaign
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
title: Adobe Experience Cloud Campaign
---

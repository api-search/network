---
description: A personalized offer used in Adobe Journey Optimizer and Target for delivering tailored content to customers based on eligibility rules, priority, and placement configuration.
layout: schema
name: Adobe Experience Cloud Offer
properties_list:
- description: The unique identifier for the offer.
  name: offerId
  type: string
- description: The human-readable name of the offer.
  name: name
  type: string
- description: A description of the offer content and purpose.
  name: description
  type: string
- description: The lifecycle status of the offer.
  name: status
  type: string
- description: Whether this is a personalized or fallback offer.
  name: offerType
  type: string
- description: The content representations for different channels and placements.
  name: representations
  type: array
- description: The eligibility rule defining which profiles can receive this offer.
  name: eligibilityRule
  type: object
- description: The priority ranking when multiple offers are eligible.
  name: priority
  type: integer
- description: Frequency capping constraints.
  name: cappingConstraint
  type: object
- description: When the offer becomes eligible for delivery.
  name: startDate
  type: string
- description: When the offer is no longer eligible for delivery.
  name: endDate
  type: string
- description: Tags for categorizing offers into collections.
  name: tags
  type: array
- description: When the offer was created.
  name: created
  type: string
- description: When the offer was last modified.
  name: lastModified
  type: string
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
schema_file: json-schema/adobe-experience-cloud-offer.json
slug: adobe-experience-cloud-offer
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
title: Adobe Experience Cloud Offer
---

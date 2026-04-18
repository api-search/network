---
description: SOAP envelope containing the service name and recipient DOM element for subscribe/unsubscribe operations.
layout: schema
name: SubscriptionRequest
properties_list:
- description: Internal name of the information service.
  name: serviceName
  type: string
- description: Recipient DOM element identifying the subscriber.
  name: recipient
  type: object
- description: Whether to create the recipient if not found (subscribe only).
  name: create
  type: boolean
provider_name: Adobe Campaign
provider_slug: adobe-campaign
schema_file: json-schema/adobe-campaign-classic-subscription-request-schema.json
slug: adobe-campaign-classic-subscription-request
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
title: SubscriptionRequest
---

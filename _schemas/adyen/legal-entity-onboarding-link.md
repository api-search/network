---
description: OnboardingLink schema from Adyen API
layout: schema
name: OnboardingLink
properties_list:
- description: The URL of the hosted onboarding page where you need to redirect your user. This URL expires after 4 minutes and can only be used once. If the link expires, you need to create a new link.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-onboarding-link-schema.json
slug: legal-entity-onboarding-link
tags:
- Payments
- Financial Services
- Fintech
title: OnboardingLink
---

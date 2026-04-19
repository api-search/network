---
description: Ad blocking configuration for a campaign.
layout: schema
name: AdBlockingConfiguration
properties_list:
- description: Whether this campaign has enabled ad blocking. When true, ad blocking is enabled for the campaign and a default ad can be served for blocked ads.
  name: enabled
  type: boolean
- description: Override click-through URL for blocked ads.
  name: overrideClickThroughUrl
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-ad-blocking-configuration-schema.json
slug: google-campaign-manager-ad-blocking-configuration
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: AdBlockingConfiguration
---

---
description: A link between a GA4 property and a Google Ads account.
layout: schema
name: GoogleAdsLink
properties_list:
- description: Enable personalized advertising features with this integration. Automatically publish my Google Analytics audience lists and Google Analytics remarketing events/parameters to the linked Google Ads acc
  name: adsPersonalizationEnabled
  type: boolean
- description: Output only. If true, this link is for a Google Ads manager account.
  name: canManageClients
  type: boolean
- description: Output only. Time when this link was originally created.
  name: createTime
  type: string
- description: Output only. Email address of the user that created the link. An empty string will be returned if the email address can't be retrieved.
  name: creatorEmailAddress
  type: string
- description: Immutable. Google Ads customer ID.
  name: customerId
  type: string
- description: 'Output only. Format: properties/{propertyId}/googleAdsLinks/{googleAdsLinkId} Note: googleAdsLinkId is not the Google Ads customer ID.'
  name: name
  type: string
- description: Output only. Time when this link was last updated.
  name: updateTime
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-google-ads-link-schema.json
slug: admin-api-google-ads-link
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: GoogleAdsLink
---

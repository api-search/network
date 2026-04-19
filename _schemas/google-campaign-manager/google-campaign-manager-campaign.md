---
description: A Campaign Manager 360 campaign. Campaigns are the top-level organizational unit for advertising activities, grouping ads, placements, and creatives under a single advertiser with shared configuration, date ranges, and targeting.
layout: schema
name: Campaign
properties_list:
- description: Campaign ID. This is a read-only, auto-generated field.
  name: id
  type: string
- description: Account ID of this campaign.
  name: accountId
  type: string
- description: Subaccount ID of this campaign.
  name: subaccountId
  type: string
- description: Advertiser ID of this campaign. Required on insert.
  name: advertiserId
  type: string
- description: Advertiser group ID of the associated advertiser.
  name: advertiserGroupId
  type: string
- description: Name of this campaign. Must be fewer than 512 characters and unique among campaigns of the same advertiser.
  name: name
  type: string
- description: Whether this campaign has been archived.
  name: archived
  type: boolean
- description: Start date of this campaign. The date format is YYYY-MM-DD.
  name: startDate
  type: string
- description: End date of this campaign. Must be on or after the start date. The date format is YYYY-MM-DD.
  name: endDate
  type: string
- description: Arbitrary comments about this campaign. Must be fewer than 256 characters.
  name: comment
  type: string
- description: Billing invoice code included in the invoices.
  name: billingInvoiceCode
  type: string
- description: Default landing page ID for this campaign.
  name: defaultLandingPageId
  type: string
- description: External ID for this campaign.
  name: externalId
  type: string
- description: Audience segment groups assigned to this campaign. Maximum of 300 segment groups.
  name: audienceSegmentGroups
  type: array
- description: Event tag overrides for this campaign.
  name: eventTagOverrides
  type: array
- description: List of creative group IDs assigned to this campaign.
  name: creativeGroupIds
  type: array
- description: Additional creative optimization configurations.
  name: additionalCreativeOptimizationConfigurations
  type: array
- description: EU political advertising declaration for this campaign.
  name: euPoliticalAdsDeclaration
  type: string
- description: Identifies what kind of resource this is. Value is always dfareporting#campaign.
  name: kind
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-campaign-schema.json
slug: google-campaign-manager-campaign
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: Campaign
---

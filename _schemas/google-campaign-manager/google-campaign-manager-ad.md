---
description: A Campaign Manager 360 ad. Ads define the creative content, delivery schedules, targeting rules, and placement assignments that control how advertising is served.
layout: schema
name: Ad
properties_list:
- description: Ad ID. Read-only, auto-generated field.
  name: id
  type: string
- description: Account ID of this ad.
  name: accountId
  type: string
- description: Subaccount ID of this ad.
  name: subaccountId
  type: string
- description: Campaign ID of this ad. Required on insert.
  name: campaignId
  type: string
- description: Advertiser ID of this ad. Required on insert.
  name: advertiserId
  type: string
- description: Name of this ad. Must be fewer than 256 characters.
  name: name
  type: string
- description: Whether this ad is active. Cannot be true when archived is true.
  name: active
  type: boolean
- description: Whether this ad is archived. Cannot be true when active is true.
  name: archived
  type: boolean
- description: Comments for this ad.
  name: comments
  type: string
- description: Date and time that this ad should start serving. Must be in the future for new ads.
  name: startTime
  type: string
- description: Date and time that this ad should stop serving. Must be after startTime.
  name: endTime
  type: string
- description: Type of ad. Required on insert.
  name: type
  type: string
- description: Whether this ad is a dynamic click tracker. Read-only after insert.
  name: dynamicClickTracker
  type: boolean
- description: Placement assignments for this ad.
  name: placementAssignments
  type: array
- description: Event tag overrides for this ad.
  name: eventTagOverrides
  type: array
- description: Identifies what kind of resource this is. Value is always dfareporting#ad.
  name: kind
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-ad-schema.json
slug: google-campaign-manager-ad
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: Ad
---

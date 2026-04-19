---
description: Delivery schedule configuration for an ad, controlling pacing and priority.
layout: schema
name: DeliverySchedule
properties_list:
- description: Impression ratio for this ad. Used to calculate the relative weight of this ad vs other ads with the same priority.
  name: impressionRatio
  type: string
- description: Serving priority of this delivery schedule.
  name: priority
  type: string
- description: Whether or not hard cutoff is enabled. If true, the ad will not serve after the end time.
  name: hardCutoff
  type: boolean
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-delivery-schedule-schema.json
slug: google-campaign-manager-delivery-schedule
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: DeliverySchedule
---

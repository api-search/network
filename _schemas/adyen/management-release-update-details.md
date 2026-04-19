---
description: ReleaseUpdateDetails schema from Adyen API
layout: schema
name: ReleaseUpdateDetails
properties_list:
- description: 'Type of terminal action: Update Release.'
  name: type
  type: string
- description: Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will update on its configured reboot time.
  name: updateAtFirstMaintenanceCall
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-release-update-details-schema.json
slug: management-release-update-details
tags:
- Payments
- Financial Services
- Fintech
title: ReleaseUpdateDetails
---

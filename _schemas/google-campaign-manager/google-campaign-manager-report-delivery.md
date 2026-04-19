---
description: Report email delivery settings.
layout: schema
name: ReportDelivery
properties_list:
- description: Whether the report should be emailed to the report owner.
  name: emailOwner
  type: boolean
- description: The type of delivery for the owner email.
  name: emailOwnerDeliveryType
  type: string
- description: The message to include in the email.
  name: message
  type: string
- description: The list of recipients to send the report to.
  name: recipients
  type: array
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-report-delivery-schema.json
slug: google-campaign-manager-report-delivery
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: ReportDelivery
---

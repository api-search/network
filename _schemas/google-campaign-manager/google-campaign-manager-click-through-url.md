---
description: Click-through URL configuration.
layout: schema
name: ClickThroughUrl
properties_list:
- description: Whether the campaign default landing page is used.
  name: defaultLandingPage
  type: boolean
- description: ID of the landing page for the click-through URL.
  name: landingPageId
  type: string
- description: Custom click-through URL.
  name: customClickThroughUrl
  type: string
- description: Read-only computed click-through URL. Set when either defaultLandingPage or landingPageId is set.
  name: computedClickThroughUrl
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-click-through-url-schema.json
slug: google-campaign-manager-click-through-url
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: ClickThroughUrl
---

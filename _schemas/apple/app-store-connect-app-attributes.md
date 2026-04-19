---
description: ''
layout: schema
name: AppAttributes
properties_list:
- description: The name of the app
  name: name
  type: string
- description: The bundle ID of the app
  name: bundleId
  type: string
- description: The SKU of the app
  name: sku
  type: string
- description: The primary locale for the app (e.g., en-US)
  name: primaryLocale
  type: string
- description: Whether the app is or was made for kids
  name: isOrEverWasMadeForKids
  type: boolean
- description: Declaration of whether the app uses third-party content
  name: contentRightsDeclaration
  type: string
- description: Whether streamlined purchasing is enabled
  name: streamlinedPurchasingEnabled
  type: boolean
- description: URL for subscription status notifications
  name: subscriptionStatusUrl
  type: '[''string'', ''null'']'
- description: URL for sandbox subscription status notifications
  name: subscriptionStatusUrlForSandbox
  type: '[''string'', ''null'']'
- description: Version of the subscription status URL
  name: subscriptionStatusUrlVersion
  type: '[''string'', ''null'']'
- description: Version of the sandbox subscription status URL
  name: subscriptionStatusUrlVersionForSandbox
  type: '[''string'', ''null'']'
provider_name: Apple
provider_slug: apple
schema_file: json-schema/app-store-connect-app-attributes-schema.json
slug: app-store-connect-app-attributes
tags:
- Developer
- iOS
- macOS
- Mobile
- Technology
title: AppAttributes
---

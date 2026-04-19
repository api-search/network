---
description: ''
layout: schema
name: BuildAttributes
properties_list:
- description: The build version string (CFBundleVersion)
  name: version
  type: string
- description: The date and time the build was uploaded
  name: uploadedDate
  type: string
- description: The date and time the build expires
  name: expirationDate
  type: string
- description: Whether the build has expired
  name: expired
  type: boolean
- description: The minimum OS version required
  name: minOsVersion
  type: string
- description: The minimum macOS system version
  name: lsMinimumSystemVersion
  type: string
- description: The computed minimum macOS version
  name: computedMinMacOsVersion
  type: string
- description: Token for the build's icon asset
  name: iconAssetToken
  type: object
- description: The processing state of the build
  name: processingState
  type: string
- description: The audience type for the build
  name: buildAudienceType
  type: string
- description: Whether the build uses non-exempt encryption
  name: usesNonExemptEncryption
  type: '[''boolean'', ''null'']'
provider_name: Apple
provider_slug: apple
schema_file: json-schema/app-store-connect-build-attributes-schema.json
slug: app-store-connect-build-attributes
tags:
- Developer
- iOS
- macOS
- Mobile
- Technology
title: BuildAttributes
---

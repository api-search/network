---
description: Metadata about the device used to write a review.
layout: schema
name: DeviceMetadata
properties_list:
- description: Device manufacturer (e.g., Samsung, Google).
  name: manufacturer
  type: string
- description: Device class (e.g., phone, tablet).
  name: deviceClass
  type: string
- description: Screen width in pixels.
  name: screenWidthPx
  type: integer
- description: Screen height in pixels.
  name: screenHeightPx
  type: integer
- description: Comma-separated list of native platforms (e.g., armeabi-v7a, arm64-v8a).
  name: nativePlatform
  type: string
- description: Device product name.
  name: productName
  type: string
- description: Screen density in DPI.
  name: screenDensityDpi
  type: integer
- description: OpenGL ES version.
  name: glEsVersion
  type: integer
- description: CPU model identifier.
  name: cpuModel
  type: string
- description: CPU manufacturer.
  name: cpuMake
  type: string
- description: Device RAM in megabytes.
  name: ramMb
  type: integer
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-device-metadata-schema.json
slug: google-play-developer-device-metadata
tags:
- AI
- Android
- Automotive
- Google
- Machine Learning
- Mobile Development
- SDK
- TV
- Wearables
title: DeviceMetadata
---

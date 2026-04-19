---
description: Schema representing an Android application and its metadata, including manifest information, Google Play Store listing details, distribution configuration, and associated API integrations. Based on the Android application model as documented at developer.android.com.
layout: schema
name: Android Application
properties_list:
- description: The unique application ID that identifies the app on the device and in the Google Play Store. Follows Java package naming conventions (e.g., com.example.myapp). Defined in the app's build.gradle as ap
  name: packageName
  type: string
- description: The user-visible name of the application as it appears on the device and in the Google Play Store.
  name: appName
  type: string
- description: An internal version number used to determine whether one version is more recent than another. Higher values indicate more recent versions. This is the versionCode specified in build.gradle.
  name: versionCode
  type: integer
- description: The version name shown to users, following semantic versioning conventions (e.g., 1.0.0). This is the versionName specified in build.gradle.
  name: versionName
  type: string
- description: The minimum Android API level required to run the application. Devices running a lower API level cannot install the app. See https://developer.android.com/guide/topics/manifest/uses-sdk-element.
  name: minSdkVersion
  type: integer
- description: The API level that the application targets. This informs the system how the app expects to behave and enables or disables compatibility behaviors. Apps on Google Play must target a recent API level.
  name: targetSdkVersion
  type: integer
- description: The API level the application is compiled against. Determines which Android framework APIs are available at compile time.
  name: compileSdkVersion
  type: integer
- description: Key attributes from the AndroidManifest.xml file that define the application's components, permissions, and requirements. See https://developer.android.com/guide/topics/manifest/manifest-intro.
  name: manifest
  type: object
- description: Build configuration details from the app's build.gradle file.
  name: buildConfiguration
  type: object
- description: Google Play Store listing metadata as managed through the Google Play Console.
  name: playStoreListing
  type: object
- description: Distribution and release configuration for the application.
  name: distribution
  type: object
- description: In-app products (managed products) available for purchase within the application.
  name: inAppProducts
  type: array
- description: Subscription products available in the application, following the Google Play Billing Library model.
  name: subscriptions
  type: array
- description: Data safety declaration for Google Play, describing what data the app collects, shares, and how it is handled. See https://developer.android.com/guide/topics/data/collect-share.
  name: dataSafety
  type: object
- description: External APIs and services integrated into the application.
  name: apiIntegrations
  type: array
provider_name: Android
provider_slug: android
schema_file: json-schema/android-app-schema.json
slug: android-app
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
title: Android Application
---

---
description: AndroidApp schema from Adyen API
layout: schema
name: AndroidApp
properties_list:
- description: The description that was provided when uploading the app. The description is not shown on the terminal.
  name: description
  type: string
- description: The error code of the app. It exists if the status is error or invalid.
  name: errorCode
  type: string
- description: The unique identifier of the app.
  name: id
  type: string
- description: The app name that is shown on the terminal.
  name: label
  type: string
- description: The package name that uniquely identifies the Android app.
  name: packageName
  type: string
- description: 'The status of the app. Possible values: * `processing`: the app is being signed and converted to a format that the terminal can handle. * `error`: something went wrong. Check that the app matches the '
  name: status
  type: string
- description: The version number of the app.
  name: versionCode
  type: integer
- description: The app version number that is shown on the terminal.
  name: versionName
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-android-app-schema.json
slug: management-android-app
tags:
- Payments
- Financial Services
- Fintech
title: AndroidApp
---

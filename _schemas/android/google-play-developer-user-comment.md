---
description: A comment from a user reviewing the app.
layout: schema
name: UserComment
properties_list:
- description: The text content of the review.
  name: text
  type: string
- description: The star rating (1-5) given by the user.
  name: starRating
  type: integer
- description: BCP-47 language tag of the reviewer's language.
  name: reviewerLanguage
  type: string
- description: Information about the device used to write the review.
  name: device
  type: string
- description: The Android OS version of the user's device.
  name: androidOsVersion
  type: integer
- description: The version code of the app installed when the review was written.
  name: appVersionCode
  type: integer
- description: The version name of the app installed when the review was written.
  name: appVersionName
  type: string
- description: Number of users who found this review helpful.
  name: thumbsUpCount
  type: integer
- description: Number of users who found this review unhelpful.
  name: thumbsDownCount
  type: integer
- description: The untranslated text of the review, if a translation was requested.
  name: originalText
  type: string
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-user-comment-schema.json
slug: google-play-developer-user-comment
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
title: UserComment
---

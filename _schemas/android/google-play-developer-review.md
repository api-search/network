---
description: An individual review of an app on Google Play, containing the user comment and optional developer reply.
layout: schema
name: Review
properties_list:
- description: Unique identifier for the review.
  name: reviewId
  type: string
- description: The name of the user who wrote the review.
  name: authorName
  type: string
- description: A list of comments for this review. Contains the user comment and optionally the developer reply.
  name: comments
  type: array
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-review-schema.json
slug: google-play-developer-review
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
title: Review
---

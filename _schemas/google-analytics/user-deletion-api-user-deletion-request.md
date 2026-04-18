---
description: UserDeletionRequest schema from Google Analytics API
layout: schema
name: UserDeletionRequest
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: ''
  name: id
  type: object
- description: The Web Property ID for a Universal Analytics property. Required for Universal Analytics properties.
  name: webPropertyId
  type: string
- description: The Firebase Project ID. Required for app streams using APP_INSTANCE_ID.
  name: firebaseProjectId
  type: string
- description: The GA4 property ID.
  name: propertyId
  type: string
- description: The time when the deletion request was submitted. Set by the server.
  name: deletionRequestTime
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/user-deletion-api-user-deletion-request-schema.json
slug: user-deletion-api-user-deletion-request
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: UserDeletionRequest
---

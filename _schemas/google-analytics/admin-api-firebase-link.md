---
description: A link between a GA4 property and a Firebase project.
layout: schema
name: FirebaseLink
properties_list:
- description: Output only. Time when this FirebaseLink was originally created.
  name: createTime
  type: string
- description: 'Output only. Example format: properties/1234/firebaseLinks/5678'
  name: name
  type: string
- description: Immutable. Firebase project resource name. When creating a FirebaseLink, you may provide this resource name using either a project number or project ID. Once this resource has been created, returned F
  name: project
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-firebase-link-schema.json
slug: admin-api-firebase-link
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: FirebaseLink
---

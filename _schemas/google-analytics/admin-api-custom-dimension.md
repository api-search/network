---
description: A definition for a CustomDimension.
layout: schema
name: CustomDimension
properties_list:
- description: Optional. Description for this custom dimension. Max length of 150 characters.
  name: description
  type: string
- description: Optional. If set to true, sets this dimension as NPA and excludes it from ads personalization. This is currently only supported by user-scoped custom dimensions.
  name: disallowAdsPersonalization
  type: boolean
- description: Required. Display name for this custom dimension as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated displ
  name: displayName
  type: string
- description: 'Output only. Resource name for this CustomDimension resource. Format: properties/{property}/customDimensions/{customDimension}'
  name: name
  type: string
- description: Required. Immutable. Tagging parameter name for this custom dimension. If this is a user-scoped dimension, then this is the user property name. If this is an event-scoped dimension, then this is the e
  name: parameterName
  type: string
- description: Required. Immutable. The scope of this dimension.
  name: scope
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-custom-dimension-schema.json
slug: admin-api-custom-dimension
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: CustomDimension
---

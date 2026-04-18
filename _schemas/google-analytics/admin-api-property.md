---
description: A resource message representing a Google Analytics GA4 property.
layout: schema
name: Property
properties_list:
- description: 'Immutable. The resource name of the parent account Format: accounts/{account_id} Example: "accounts/123"'
  name: account
  type: string
- description: Output only. Time when the entity was originally created.
  name: createTime
  type: string
- description: 'The currency type used in reports involving monetary values. Format: https://en.wikipedia.org/wiki/ISO_4217 Examples: "USD", "EUR", "JPY"'
  name: currencyCode
  type: string
- description: Output only. If set, the time at which this property was trashed. If not set, then this property is not currently in the trash can.
  name: deleteTime
  type: string
- description: Required. Human-readable display name for this property. The max allowed display name length is 100 UTF-16 code units.
  name: displayName
  type: string
- description: Output only. If set, the time at which this trashed property will be permanently deleted. If not set, then this property is not currently in the trash can and is not slated to be deleted.
  name: expireTime
  type: string
- description: 'Industry associated with this property Example: AUTOMOTIVE, FOOD_AND_DRINK'
  name: industryCategory
  type: string
- description: 'Output only. Resource name of this property. Format: properties/{property_id} Example: "properties/1000"'
  name: name
  type: string
- description: 'Immutable. Resource name of this property''s logical parent. Note: The Property-Moving UI can be used to change the parent. Format: accounts/{account}, properties/{property} Example: "accounts/100", "p'
  name: parent
  type: string
- description: Immutable. The property type for this Property resource. When creating a property, if the type is "PROPERTY_TYPE_UNSPECIFIED", then "ORDINARY_PROPERTY" will be implied.
  name: propertyType
  type: string
- description: Output only. The Google Analytics service level that applies to this property.
  name: serviceLevel
  type: string
- description: 'Required. Reporting Time Zone, used as the day boundary for reports, regardless of where the data originates. If the time zone honors DST, Analytics will automatically adjust for the changes. NOTE: Ch'
  name: timeZone
  type: string
- description: Output only. Time when entity payload fields were last updated.
  name: updateTime
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-property-schema.json
slug: admin-api-property
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: Property
---

---
class_count: 10
classes:
- Account
- ChangeHistoryEvent
- ConversionEvent
- CustomDimension
- CustomMetric
- DataStream
- FirebaseLink
- GoogleAdsLink
- MeasurementProtocolSecret
- Property
context_file: json-ld/google-analytics-admin-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/json-ld/google-analytics-admin-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Google Analytics Admin Api from Google Analytics.
layout: jsonld
name: Google Analytics Admin Api Context
namespaces:
- prefix: ga
  uri: https://developers.google.com/analytics/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: account
  type: string
- container: ''
  name: actorType
  type: string
- container: ''
  name: adsPersonalizationEnabled
  type: boolean
- container: ''
  name: androidAppStreamData
  type: reference
- container: ''
  name: bundleId
  type: string
- container: ''
  name: canManageClients
  type: boolean
- container: ''
  name: changeTime
  type: dateTime
- container: set
  name: changes
  type: reference
- container: ''
  name: changesFiltered
  type: boolean
- container: ''
  name: countingMethod
  type: string
- container: ''
  name: createTime
  type: dateTime
- container: ''
  name: creatorEmailAddress
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: custom
  type: boolean
- container: ''
  name: customerId
  type: string
- container: ''
  name: defaultConversionValue
  type: reference
- container: ''
  name: defaultUri
  type: string
- container: ''
  name: deletable
  type: boolean
- container: ''
  name: deleteTime
  type: dateTime
- container: ''
  name: deleted
  type: boolean
- container: ''
  name: description
  type: string
- container: ''
  name: disallowAdsPersonalization
  type: boolean
- container: ''
  name: displayName
  type: string
- container: ''
  name: eventName
  type: string
- container: ''
  name: expireTime
  type: dateTime
- container: ''
  name: firebaseAppId
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: industryCategory
  type: string
- container: ''
  name: iosAppStreamData
  type: reference
- container: ''
  name: measurementId
  type: string
- container: ''
  name: measurementUnit
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: packageName
  type: string
- container: ''
  name: parameterName
  type: string
- container: ''
  name: parent
  type: string
- container: ''
  name: project
  type: string
- container: ''
  name: propertyType
  type: string
- container: ''
  name: regionCode
  type: string
- container: set
  name: restrictedMetricType
  type: string
- container: ''
  name: scope
  type: string
- container: ''
  name: secretValue
  type: string
- container: ''
  name: serviceLevel
  type: string
- container: ''
  name: timeZone
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: updateTime
  type: dateTime
- container: ''
  name: userActorEmail
  type: string
- container: ''
  name: value
  type: double
- container: ''
  name: webStreamData
  type: reference
property_count: 48
provider_name: Google Analytics
provider_slug: google-analytics
slug: google-analytics-admin-api-context
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
- JSON-LD
- Linked Data
- Semantic Web
---

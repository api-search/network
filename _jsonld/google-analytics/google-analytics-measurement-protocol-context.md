---
class_count: 7
classes:
- Consent
- Device
- Event
- MeasurementPayload
- UserLocation
- ValidationMessage
- ValidationResponse
context_file: json-ld/google-analytics-measurement-protocol-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/json-ld/google-analytics-measurement-protocol-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Google Analytics Measurement Protocol from Google Analytics.
layout: jsonld
name: Google Analytics Measurement Protocol Context
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
  name: adPersonalization
  type: string
- container: ''
  name: adUserData
  type: string
- container: ''
  name: appInstanceId
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: browser
  type: string
- container: ''
  name: browserVersion
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: clientId
  type: string
- container: ''
  name: consent
  type: reference
- container: ''
  name: continentId
  type: string
- container: ''
  name: countryId
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: device
  type: reference
- container: ''
  name: engagementTimeMsec
  type: integer
- container: set
  name: events
  type: reference
- container: ''
  name: fieldPath
  type: string
- container: ''
  name: ipOverride
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: nonPersonalizedAds
  type: boolean
- container: ''
  name: operatingSystem
  type: string
- container: ''
  name: operatingSystemVersion
  type: string
- container: ''
  name: params
  type: reference
- container: ''
  name: regionId
  type: string
- container: ''
  name: screenResolution
  type: string
- container: ''
  name: sessionId
  type: string
- container: ''
  name: subcontinentId
  type: string
- container: ''
  name: timestampMicros
  type: integer
- container: ''
  name: userData
  type: reference
- container: ''
  name: userId
  type: string
- container: ''
  name: userLocation
  type: reference
- container: ''
  name: userProperties
  type: reference
- container: ''
  name: validationCode
  type: string
- container: set
  name: validationMessages
  type: reference
- container: ''
  name: validationBehavior
  type: string
property_count: 37
provider_name: Google Analytics
provider_slug: google-analytics
slug: google-analytics-measurement-protocol-context
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

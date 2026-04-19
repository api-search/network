---
class_count: 10
classes:
- Adobe Experience Cloud Event
- Adobe Experience Cloud Campaign
- Adobe Experience Cloud Offer
- Adobe Experience Cloud Journey
- Adobe Experience Cloud Segment
- Adobe Experience Cloud Profile
- name
- version
- description
- email
context_file: json-ld/adobe-experience-cloud-io-events-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/json-ld/adobe-experience-cloud-io-events-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Experience Cloud Io Events from Adobe Experience Cloud.
layout: jsonld
name: Adobe Experience Cloud Io Events Context
namespaces:
- prefix: aec
  uri: https://developer.adobe.com/schema/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: schema
  type: reference
- container: ''
  name: eventId
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: identityMap
  type: reference
- container: ''
  name: web
  type: reference
- container: ''
  name: webPageDetails
  type: reference
- container: ''
  name: URL
  type: reference
- container: ''
  name: siteSection
  type: string
- container: ''
  name: isHomePage
  type: boolean
- container: ''
  name: webInteraction
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: webReferrer
  type: reference
- container: ''
  name: commerce
  type: reference
- container: ''
  name: purchases
  type: reference
- container: ''
  name: value
  type: decimal
- container: ''
  name: order
  type: reference
- container: ''
  name: purchaseID
  type: string
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: priceTotal
  type: decimal
- container: set
  name: payments
  type: string
- container: ''
  name: paymentType
  type: string
- container: ''
  name: paymentAmount
  type: decimal
- container: set
  name: productListItems
  type: string
- container: ''
  name: SKU
  type: string
- container: ''
  name: quantity
  type: integer
- container: ''
  name: device
  type: reference
- container: ''
  name: manufacturer
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: screenHeight
  type: integer
- container: ''
  name: screenWidth
  type: integer
- container: ''
  name: environment
  type: reference
- container: ''
  name: browserDetails
  type: reference
- container: ''
  name: userAgent
  type: string
- container: ''
  name: operatingSystem
  type: string
- container: ''
  name: operatingSystemVersion
  type: string
- container: ''
  name: ipV4
  type: string
- container: ''
  name: source
  type: reference
- container: ''
  name: datasetId
  type: string
- container: ''
  name: campaignId
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: audience
  type: reference
- container: ''
  name: segmentId
  type: string
- container: ''
  name: estimatedSize
  type: integer
- container: ''
  name: content
  type: reference
- container: ''
  name: subject
  type: string
- container: ''
  name: body
  type: string
- container: ''
  name: templateId
  type: string
- container: ''
  name: sender
  type: reference
- container: ''
  name: schedule
  type: reference
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: endDate
  type: dateTime
- container: ''
  name: timezone
  type: string
- container: ''
  name: recurring
  type: boolean
- container: ''
  name: metrics
  type: reference
- container: ''
  name: sent
  type: integer
- container: ''
  name: delivered
  type: integer
- container: ''
  name: opened
  type: integer
- container: ''
  name: clicked
  type: integer
- container: ''
  name: bounced
  type: integer
- container: ''
  name: unsubscribed
  type: integer
- container: ''
  name: created
  type: dateTime
- container: ''
  name: lastModified
  type: dateTime
- container: ''
  name: offerId
  type: string
- container: ''
  name: offerType
  type: string
- container: set
  name: representations
  type: string
- container: ''
  name: placementId
  type: string
- container: ''
  name: contentType
  type: string
- container: ''
  name: eligibilityRule
  type: reference
- container: ''
  name: ruleId
  type: string
- container: ''
  name: priority
  type: integer
- container: ''
  name: cappingConstraint
  type: reference
- container: ''
  name: maxImpressions
  type: integer
- container: ''
  name: scope
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: journeyId
  type: string
- container: ''
  name: entryCondition
  type: reference
- container: ''
  name: frequency
  type: string
- container: set
  name: activities
  type: string
- container: ''
  name: activityId
  type: string
- container: ''
  name: configuration
  type: reference
- container: ''
  name: nextActivityId
  type: string
- container: ''
  name: totalEntered
  type: integer
- container: ''
  name: currentlyInJourney
  type: integer
- container: ''
  name: totalExited
  type: integer
- container: ''
  name: totalErrored
  type: integer
- container: ''
  name: publishedAt
  type: dateTime
- container: ''
  name: expression
  type: reference
- container: ''
  name: format
  type: string
- container: ''
  name: evaluationType
  type: string
- container: ''
  name: mergePolicyId
  type: string
- container: ''
  name: profileCount
  type: integer
- container: ''
  name: owner
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: lastEvaluated
  type: dateTime
- container: ''
  name: profileId
  type: string
- container: ''
  name: person
  type: reference
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: fullName
  type: string
- container: ''
  name: birthDate
  type: date
- container: ''
  name: gender
  type: string
- container: ''
  name: personalEmail
  type: reference
- container: ''
  name: address
  type: string
- container: ''
  name: primary
  type: boolean
- container: ''
  name: mobilePhone
  type: reference
- container: ''
  name: number
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: homeAddress
  type: reference
- container: ''
  name: street1
  type: string
- container: ''
  name: street2
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: stateProvince
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: segmentMembership
  type: reference
- container: ''
  name: consents
  type: reference
- container: ''
  name: marketing
  type: reference
- container: ''
  name: val
  type: string
- container: ''
  name: push
  type: reference
- container: ''
  name: sms
  type: reference
property_count: 122
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
slug: adobe-experience-cloud-io-events-context
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
- JSON-LD
- Linked Data
- Semantic Web
---

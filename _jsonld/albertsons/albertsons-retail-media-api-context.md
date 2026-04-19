---
class_count: 13
classes:
- Audience List Response
- Audience
- Campaign List Response
- Campaign
- Create Campaign Request
- Error Response
- Performance Metric
- Performance Metrics Response
- Report Request
- Report Response
- createdAt
- description
- name
context_file: json-ld/albertsons-retail-media-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/albertsons/refs/heads/main/json-ld/albertsons-retail-media-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Albertsons Retail Media Api from albertsons.
layout: jsonld
name: Albertsons Retail Media Api Context
namespaces:
- prefix: alb
  uri: https://albertsons.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: audienceId
  type: string
- container: set
  name: audiences
  type: string
- container: ''
  name: budget
  type: double
- container: ''
  name: campaignId
  type: string
- container: set
  name: campaignIds
  type: string
- container: set
  name: campaigns
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: clickThroughRate
  type: double
- container: ''
  name: clicks
  type: integer
- container: ''
  name: conversions
  type: integer
- container: ''
  name: date
  type: date
- container: set
  name: dimensions
  type: string
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: endDate
  type: date
- container: ''
  name: error
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: impressions
  type: integer
- container: ''
  name: limit
  type: integer
- container: ''
  name: message
  type: string
- container: set
  name: metrics
  type: string
- container: ''
  name: offset
  type: integer
- container: ''
  name: reportId
  type: string
- container: ''
  name: roas
  type: double
- container: ''
  name: size
  type: integer
- container: ''
  name: spend
  type: double
- container: ''
  name: startDate
  type: date
- container: ''
  name: status
  type: string
- container: ''
  name: statusCode
  type: integer
- container: set
  name: targetAudienceIds
  type: string
- container: ''
  name: total
  type: integer
property_count: 30
provider_name: albertsons
provider_slug: albertsons
slug: albertsons-retail-media-api-context
tags:
- Grocery
- Retail
- Retail Media
- Advertising
- Campaigns
- Analytics
- Consumer Goods
- Food
- Pharmacy
- JSON-LD
- Linked Data
- Semantic Web
---

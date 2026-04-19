---
class_count: 9
classes:
- Report
- Office
- name
- Reports List Response
- Report Data Response
- Report Data
- Error Response
- Offices List Response
- Pagination Stats
context_file: json-ld/agricultural-marketing-service-mars-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agricultural-marketing-service/refs/heads/main/json-ld/agricultural-marketing-service-mars-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agricultural Marketing Service Mars Api from Agricultural Marketing Service.
layout: jsonld
name: Agricultural Marketing Service Mars Api Context
namespaces:
- prefix: ams
  uri: https://ams.usda.gov/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: slugId
  type: string
- container: ''
  name: slugName
  type: string
- container: ''
  name: reportDate
  type: date
- container: ''
  name: publishedDate
  type: dateTime
- container: ''
  name: commodity
  type: string
- container: ''
  name: marketType
  type: string
- container: ''
  name: office
  type: string
- container: ''
  name: sectionName
  type: string
- container: ''
  name: officeId
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: set
  name: commodities
  type: string
- container: set
  name: results
  type: string
- container: ''
  name: stats
  type: string
- container: ''
  name: class
  type: string
- container: ''
  name: grade
  type: string
- container: ''
  name: headCount
  type: integer
- container: ''
  name: pricePerCwt
  type: double
- container: ''
  name: priceUnit
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: status
  type: integer
- container: ''
  name: count
  type: integer
- container: ''
  name: total
  type: integer
property_count: 25
provider_name: Agricultural Marketing Service
provider_slug: agricultural-marketing-service
slug: agricultural-marketing-service-mars-api-context
tags:
- Agriculture
- Federal Government
- Market News
- Livestock
- Dairy
- Fruits And Vegetables
- Cotton
- Tobacco
- JSON-LD
- Linked Data
- Semantic Web
---

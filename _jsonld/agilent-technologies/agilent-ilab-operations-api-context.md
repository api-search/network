---
class_count: 23
classes:
- Price Update Request
- Service Requests List Response
- Service Request Create Request
- Core
- name
- description
- url
- Invoices List Response
- Cores List Response
- Member
- email
- Price
- Prices List Response
- Invoice
- Service Request
- Project
- Members List Response
- Service
- Projects List Response
- Reservations List Response
- Error Response
- Services List Response
- Reservation
context_file: json-ld/agilent-ilab-operations-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agilent-technologies/refs/heads/main/json-ld/agilent-ilab-operations-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agilent Ilab Operations Api from agilent-technologies.
layout: jsonld
name: Agilent Ilab Operations Api Context
namespaces:
- prefix: agilent
  uri: https://agilent.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: amount
  type: double
- container: ''
  name: currency
  type: string
- container: set
  name: serviceRequests
  type: string
- container: ''
  name: serviceId
  type: integer
- container: ''
  name: projectId
  type: integer
- container: ''
  name: quantity
  type: integer
- container: ''
  name: notes
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: institution
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: contactEmail
  type: string
- container: set
  name: invoices
  type: string
- container: set
  name: cores
  type: string
- container: ''
  name: total
  type: integer
- container: ''
  name: page
  type: integer
- container: ''
  name: perPage
  type: integer
- container: ''
  name: role
  type: string
- container: ''
  name: memberType
  type: string
- container: ''
  name: unit
  type: string
- container: set
  name: prices
  type: string
- container: ''
  name: period
  type: string
- container: ''
  name: totalAmount
  type: double
- container: ''
  name: issuedAt
  type: dateTime
- container: ''
  name: submittedAt
  type: dateTime
- container: ''
  name: principalInvestigator
  type: string
- container: ''
  name: piName
  type: string
- container: ''
  name: accountNumber
  type: string
- container: set
  name: members
  type: string
- container: set
  name: projects
  type: string
- container: set
  name: reservations
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: message
  type: string
- container: set
  name: services
  type: string
- container: ''
  name: equipmentName
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: user
  type: string
property_count: 37
provider_name: agilent-technologies
provider_slug: agilent-technologies
slug: agilent-ilab-operations-api-context
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 5
classes:
- Incident
- IncidentCollection
- date
- description
- name
context_file: json-ld/2020-police-brutality-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/json-ld/2020-police-brutality-context.jsonld
description: JSON-LD context defining the semantic vocabulary for 2020 Police Brutality from 2020 Police Brutality.
layout: jsonld
name: 2020 Police Brutality Context
namespaces:
- prefix: pb2020
  uri: https://2020pb.github.io/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: city
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: dateText
  type: string
- container: ''
  name: editAt
  type: reference
- container: ''
  name: geolocation
  type: string
- container: ''
  name: help
  type: reference
- container: ''
  name: id
  type: string
- container: set
  name: links
  type: string
- container: ''
  name: state
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: updatedAt
  type: dateTime
property_count: 11
provider_name: 2020 Police Brutality
provider_slug: 2020-police-brutality
slug: 2020-police-brutality-context
tags:
- Brutality
- Civil Rights
- Policing
- Public Data
- JSON-LD
- Linked Data
- Semantic Web
---

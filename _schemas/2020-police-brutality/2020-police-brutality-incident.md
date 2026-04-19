---
description: A documented police brutality incident from the 2020 George Floyd protests
layout: schema
name: Incident
properties_list:
- description: 'Unique identifier for the incident (format: state-city-number)'
  name: id
  type: string
- description: Brief title or summary of the incident
  name: name
  type: string
- description: Detailed description of what occurred during the incident
  name: description
  type: string
- description: Date the incident occurred (ISO 8601 format)
  name: date
  type: string
- description: Human-readable date description
  name: date_text
  type: string
- description: US state abbreviation where the incident occurred
  name: state
  type: string
- description: City where the incident occurred
  name: city
  type: string
- description: Latitude and longitude coordinates of the incident location
  name: geolocation
  type: string
- description: Categorical tags describing the type of incident or force used
  name: tags
  type: array
- description: Source URLs documenting or referencing the incident
  name: links
  type: array
- description: Direct link to edit this incident record on GitHub
  name: edit_at
  type: string
provider_name: 2020 Police Brutality
provider_slug: 2020-police-brutality
schema_file: json-schema/2020-police-brutality-incident-schema.json
slug: 2020-police-brutality-incident
tags:
- Brutality
- Civil Rights
- Policing
- Public Data
title: Incident
---

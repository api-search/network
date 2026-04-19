---
description: Single media resource data
layout: schema
name: ResourceContract
properties_list:
- description: URL of the resource
  name: url
  type: string
- description: URL of web-page containing the resource
  name: webUrl
  type: string
- description: Author name of the resource
  name: author
  type: string
- description: Title of the resource
  name: title
  type: string
- description: Description of the resource
  name: description
  type: string
- description: ''
  name: license
  type: object
- description: Attributions maintaining copyright, ownership and other legal information adjusted for displaying as HTML. Each element represent one line.
  name: htmlAttributions
  type: array
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-resource-contract-schema.json
slug: aerodatabox-resource-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: ResourceContract
---

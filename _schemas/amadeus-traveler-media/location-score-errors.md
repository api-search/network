---
description: errors schema
layout: schema
name: errors
properties_list:
- description: The [HTTP status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) of this response. This is present only in terminal errors which cause an unsuccessful response. In th
  name: status
  type: integer
- description: A machine-readable error code from the Amadeus Canned Messages table, that will enable the API Consumers code to handle this type of error
  name: code
  type: integer
- description: An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized
  name: title
  type: string
- description: An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be
  name: detail
  type: string
- description: ''
  name: source
  type: object
provider_name: Amadeus Traveler Media
provider_slug: amadeus-traveler-media
schema_file: json-schema/location-score-errors-schema.json
slug: location-score-errors
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
title: errors
---

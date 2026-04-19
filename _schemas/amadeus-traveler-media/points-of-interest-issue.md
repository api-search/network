---
description: Issue schema
layout: schema
name: Issue
properties_list:
- description: the HTTP status code applicable to this error
  name: status
  type: integer
- description: an application-specific error code
  name: code
  type: integer
- description: a short summary of the error
  name: title
  type: string
- description: explanation of the error
  name: detail
  type: string
- description: an object containing references to the source of the error
  name: source
  type: object
provider_name: Amadeus Traveler Media
provider_slug: amadeus-traveler-media
schema_file: json-schema/points-of-interest-issue-schema.json
slug: points-of-interest-issue
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
title: Issue
---

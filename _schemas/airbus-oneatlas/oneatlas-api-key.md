---
description: ''
layout: schema
name: ApiKey
properties_list:
- description: API key creation date in ISO 8601 format
  name: date
  type: string
- description: A free-text human readable description of this API key
  name: description
  type: string
- description: API key expiration date in ISO 8601 format
  name: expirationDate
  type: string
- description: API Key identifier
  name: id
  type: string
- description: The API Key secret to be used to retrieve acces tokens. This field is only provided once, then the client should store this information in a secure place.
  name: secret
  type: string
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-api-key-schema.json
slug: oneatlas-api-key
tags:
- Imagery
- Satellites
title: ApiKey
---

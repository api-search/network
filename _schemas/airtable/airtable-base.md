---
description: An Airtable base is a database that contains one or more tables. Bases are the top-level containers for organizing related data in Airtable.
layout: schema
name: Airtable Base
properties_list:
- description: The unique identifier for the base. Base IDs always start with the 'app' prefix.
  name: id
  type: string
- description: The display name of the base.
  name: name
  type: string
- description: The permission level the authenticated user has on this base.
  name: permissionLevel
  type: string
- description: The tables contained within this base. Only included when retrieving the full base schema.
  name: tables
  type: array
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-base-schema.json
slug: airtable-base
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Base
---

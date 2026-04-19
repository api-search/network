---
description: A comment attached to an Airtable record. Comments support user mentions using the @[usrXXXXXXXX] syntax and are used for collaboration and discussion within records.
layout: schema
name: Airtable Comment
properties_list:
- description: The unique identifier for the comment.
  name: id
  type: string
- description: The text content of the comment. May include user mentions in the format @[usrXXXXXXXX].
  name: text
  type: string
- description: The user who created the comment.
  name: author
  type: object
- description: The time when the comment was created in ISO 8601 format.
  name: createdTime
  type: string
- description: The time when the comment was last updated. Null if the comment has not been edited.
  name: lastUpdatedTime
  type:
  - string
  - 'null'
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-comment-schema.json
slug: airtable-comment
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Comment
---

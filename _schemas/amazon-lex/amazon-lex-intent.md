---
description: An Amazon Lex intent representing an action a user can perform.
layout: schema
name: Intent
properties_list:
- description: The unique identifier assigned to the intent.
  name: intentId
  type: string
- description: The name of the intent.
  name: intentName
  type: string
- description: The description of the intent.
  name: description
  type: string
- description: The identifier of the bot associated with this intent.
  name: botId
  type: string
- description: The version of the bot associated with this intent.
  name: botVersion
  type: string
- description: The language and locale of the intent.
  name: localeId
  type: string
- description: A timestamp of the date and time the intent was created.
  name: creationDateTime
  type: string
provider_name: Amazon Lex
provider_slug: amazon-lex
schema_file: json-schema/amazon-lex-intent-schema.json
slug: amazon-lex-intent
tags: []
title: Intent
---

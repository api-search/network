---
description: An Amazon Lex V2 bot for building conversational interfaces.
layout: schema
name: Bot
properties_list:
- description: The unique identifier assigned to the bot.
  name: botId
  type: string
- description: The name specified for the bot.
  name: botName
  type: string
- description: The current status of the bot.
  name: botStatus
  type: string
- description: The description of the bot.
  name: description
  type: string
- description: The Amazon Resource Name (ARN) of the role assumed by the bot.
  name: roleArn
  type: string
- description: A timestamp of the date and time the bot was created.
  name: creationDateTime
  type: string
- description: A timestamp of the date and time the bot was last updated.
  name: lastUpdatedDateTime
  type: string
provider_name: Amazon Lex
provider_slug: amazon-lex
schema_file: json-schema/amazon-lex-bot-schema.json
slug: amazon-lex-bot
tags: []
title: Bot
---

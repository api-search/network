---
description: A Slack message object representing a single message in a conversation. Messages can contain text, blocks, attachments, files, and reactions.
layout: schema
name: Message
properties_list:
- description: Always "message" for messages.
  name: type
  type: string
- description: Optional subtype indicating a specialized message type such as bot_message, channel_join, channel_leave, etc.
  name: subtype
  type: string
- description: The channel ID where the message was posted.
  name: channel
  type: string
- description: The user ID of the message author.
  name: user
  type: string
- description: The text content of the message.
  name: text
  type: string
- description: Unique timestamp identifier for the message, also serves as the message ID. Format is Unix epoch with microseconds (e.g., "1503435956.000247").
  name: ts
  type: string
- description: The timestamp of the parent message in a thread. Present only for threaded replies.
  name: thread_ts
  type: string
- description: Number of replies in the thread.
  name: reply_count
  type: integer
- description: Number of unique users who have replied in the thread.
  name: reply_users_count
  type: integer
- description: Timestamp of the most recent reply in the thread.
  name: latest_reply
  type: string
- description: Array of user IDs who have replied in the thread.
  name: reply_users
  type: array
- description: An array of Block Kit layout blocks used for rich message formatting.
  name: blocks
  type: array
- description: An array of message attachments.
  name: attachments
  type: array
- description: An array of file objects attached to the message.
  name: files
  type: array
- description: An array of emoji reactions on this message.
  name: reactions
  type: array
- description: Edit information if the message was edited.
  name: edited
  type: object
- description: Bot ID if the message was posted by a bot.
  name: bot_id
  type: string
- description: Bot profile information if posted by a bot.
  name: bot_profile
  type: object
- description: Custom metadata attached to the message by an application.
  name: metadata
  type: object
- description: Permalink URL for the message.
  name: permalink
  type: string
provider_name: Slack
provider_slug: slack
schema_file: json-schema/slack-web-message-schema.json
slug: slack-web-message
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
title: Message
---

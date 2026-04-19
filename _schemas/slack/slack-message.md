---
description: A Slack message object representing a single message in a conversation. Messages can contain plain text, Block Kit layouts, attachments, files, reactions, and metadata. Each message is uniquely identified by its channel and timestamp (ts) combination. Messages support threading via thread_ts, and can have subtypes indicating specialized message types such as bot_message, channel_join, file_share, etc.
layout: schema
name: Slack Message
properties_list:
- description: The object type. Always 'message' for message objects.
  name: type
  type: string
- description: 'An optional subtype indicating a specialized message type. Common subtypes include: bot_message, channel_join, channel_leave, channel_topic, channel_purpose, channel_name, channel_archive, channel_una'
  name: subtype
  type: string
- description: The channel ID where the message was posted. Channel IDs begin with C for public channels, G for private channels and multi-person DMs, and D for direct messages.
  name: channel
  type: string
- description: The user ID of the message author. User IDs begin with U or W.
  name: user
  type: string
- description: The text content of the message. Supports Slack mrkdwn formatting including *bold*, _italic_, ~strikethrough~, `code`, ```code blocks```, > blockquotes, and <URL|label> links. Also supports user menti
  name: text
  type: string
- description: The unique timestamp identifier for the message, which also serves as the message ID within its channel. Format is Unix epoch seconds with microsecond precision separated by a dot (e.g., '1503435956.0
  name: ts
  type: string
- description: The timestamp of the parent message when this message is a threaded reply. If present and equal to ts, this message is the parent of a thread. If present and different from ts, this message is a reply
  name: thread_ts
  type: string
- description: The total number of replies in the thread. Only present on the parent message of a thread.
  name: reply_count
  type: integer
- description: The number of unique users who have replied in the thread. Only present on the parent message.
  name: reply_users_count
  type: integer
- description: The timestamp of the most recent reply in the thread. Only present on the parent message.
  name: latest_reply
  type: string
- description: An array of user IDs for users who have replied in the thread. Only present on the parent message. Limited to the most recent 5 reply users by default.
  name: reply_users
  type: array
- description: Whether the thread is locked, preventing new replies.
  name: is_locked
  type: boolean
- description: Whether the authenticated user is subscribed to this thread.
  name: subscribed
  type: boolean
- description: An array of Block Kit layout blocks used for rich message formatting. Blocks can include sections, dividers, images, context, actions, header, input, and other interactive elements. See https://docs.s
  name: blocks
  type: array
- description: An array of secondary message attachments. While Block Kit is the preferred way to build rich messages, attachments are still supported for legacy compatibility and for displaying content below the bl
  name: attachments
  type: array
- description: An array of file objects attached to or shared in the message.
  name: files
  type: array
- description: An array of emoji reactions applied to this message. Only present when reactions exist.
  name: reactions
  type: array
- description: Metadata about when and by whom the message was last edited. Only present on edited messages.
  name: edited
  type: object
- description: The bot ID if this message was posted by a bot. Bot IDs begin with B.
  name: bot_id
  type: string
- description: Information about the bot that posted this message.
  name: bot_profile
  type: object
- description: The app ID if this message was posted by an app.
  name: app_id
  type: string
- description: Custom metadata attached to the message by an application. Metadata allows apps to attach structured data to messages for use in workflows and automations without affecting the visible message content
  name: metadata
  type: object
- description: A permanent URL pointing to this specific message within Slack.
  name: permalink
  type: string
- description: A unique identifier assigned by the client when the message was sent. Used for deduplication.
  name: client_msg_id
  type: string
- description: The team (workspace) ID where this message was posted.
  name: team
  type: string
- description: The user ID of the parent message author, if this is a threaded reply.
  name: parent_user_id
  type: string
- description: Whether the authenticated user has starred this message.
  name: is_starred
  type: boolean
- description: An array of channel IDs where this message is pinned.
  name: pinned_to
  type: array
- description: Whether the message is a file upload notification.
  name: upload
  type: boolean
- description: Whether the message should be displayed as if from a bot.
  name: display_as_bot
  type: boolean
provider_name: Slack
provider_slug: slack
schema_file: json-schema/slack-message-schema.json
slug: slack-message
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
title: Slack Message
---

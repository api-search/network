---
description: A Slack conversation object representing a channel, direct message, multi-person DM, or group conversation.
layout: schema
name: Channel
properties_list:
- description: The unique identifier for this conversation.
  name: id
  type: string
- description: 'The name of the channel (without the leading # sign).'
  name: name
  type: string
- description: Normalized version of the channel name.
  name: name_normalized
  type: string
- description: Whether this is a public channel.
  name: is_channel
  type: boolean
- description: Whether this is a private channel (formerly a group).
  name: is_group
  type: boolean
- description: Whether this is a direct message.
  name: is_im
  type: boolean
- description: Whether this is a multi-person direct message.
  name: is_mpim
  type: boolean
- description: Whether this is a private conversation.
  name: is_private
  type: boolean
- description: Whether the channel is archived.
  name: is_archived
  type: boolean
- description: Whether this is the
  name: is_general
  type: boolean
- description: Whether the channel is shared with another workspace.
  name: is_shared
  type: boolean
- description: Whether the channel is shared with an external organization via Slack Connect.
  name: is_ext_shared
  type: boolean
- description: Whether the channel is shared across an Enterprise Grid org.
  name: is_org_shared
  type: boolean
- description: Whether there is a pending external share invitation.
  name: is_pending_ext_shared
  type: boolean
- description: Whether the calling user is a member of this conversation.
  name: is_member
  type: boolean
- description: Whether the DM is open.
  name: is_open
  type: boolean
- description: Whether the channel is frozen.
  name: is_frozen
  type: boolean
- description: Unix timestamp of when the conversation was created.
  name: created
  type: integer
- description: User ID of the member who created this channel.
  name: creator
  type: string
- description: Unix timestamp of the last update to the conversation.
  name: updated
  type: integer
- description: Number of times the channel has been unlinked.
  name: unlinked
  type: integer
- description: The channel topic.
  name: topic
  type: object
- description: The channel purpose.
  name: purpose
  type: object
- description: A list of previous names the channel had.
  name: previous_names
  type: array
- description: The number of members in the channel. Only included when specifically requested.
  name: num_members
  type: integer
- description: IETF language code for the channel locale. Only included when specifically requested.
  name: locale
  type: string
- description: For direct messages, the user ID of the other participant.
  name: user
  type: string
- description: Array of team IDs that share this channel (for shared channels).
  name: shared_team_ids
  type: array
- description: Parent conversation ID for thread-only channels.
  name: parent_conversation
  type: string
- description: The workspace team ID.
  name: context_team_id
  type: string
- description: Additional channel properties.
  name: properties
  type: object
provider_name: Slack
provider_slug: slack
schema_file: json-schema/slack-web-channel-schema.json
slug: slack-web-channel
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
title: Channel
---

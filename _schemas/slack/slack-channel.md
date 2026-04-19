---
description: A Slack conversation object representing a channel, direct message, multi-person direct message, or group conversation. This is the unified model returned by the conversations.* family of Web API methods, which consolidated the legacy channels.*, groups.*, im.*, and mpim.* endpoints. The type of conversation is identified by boolean flags (is_channel, is_group, is_im, is_mpim) and the is_private flag. Channels are uniquely identified by their id field, with public channels starting with C, private channels and multi-person DMs starting with G, and direct messages starting with D.
layout: schema
name: Slack Channel
properties_list:
- description: The unique identifier for this conversation. Public channels begin with C, private channels and multi-person DMs begin with G, and direct messages begin with D.
  name: id
  type: string
- description: 'The name of the channel without the leading # sign. Channel names can contain lowercase letters, numbers, hyphens, and underscores, with a maximum length of 80 characters. Not present for direct messa'
  name: name
  type: string
- description: A normalized, lowercase version of the channel name. Useful for case-insensitive comparisons and sorting.
  name: name_normalized
  type: string
- description: Whether this conversation is a public channel. Public channels are visible to all members of the workspace and can be joined by anyone.
  name: is_channel
  type: boolean
- description: Whether this conversation is a private channel. Private channels are invite-only and not visible in the channel browser.
  name: is_group
  type: boolean
- description: Whether this conversation is a direct message between two people.
  name: is_im
  type: boolean
- description: Whether this conversation is a multi-person direct message. MPIMs are group DMs between 3 or more people.
  name: is_mpim
  type: boolean
- description: Whether this conversation is private. True for private channels, DMs, and MPIMs. False for public channels.
  name: is_private
  type: boolean
- description: Whether the channel is archived. Archived channels are read-only and do not accept new messages. They can be unarchived by workspace admins.
  name: is_archived
  type: boolean
- description: 'Whether this is the workspace''s #general channel. Every workspace has exactly one general channel that all members are automatically added to.'
  name: is_general
  type: boolean
- description: Whether the channel is shared with another workspace using Slack Connect.
  name: is_shared
  type: boolean
- description: Whether the channel is shared with an external organization via Slack Connect. External shared channels allow cross-organization collaboration.
  name: is_ext_shared
  type: boolean
- description: Whether the channel is shared across the entire Enterprise Grid organization. Org-wide channels are available to all workspaces in the grid.
  name: is_org_shared
  type: boolean
- description: Whether there is a pending Slack Connect invitation for this channel that has not yet been accepted.
  name: is_pending_ext_shared
  type: boolean
- description: Whether the authenticated user or bot is a member of this conversation. Users must be members to read history or post messages in private channels.
  name: is_member
  type: boolean
- description: Whether the direct message or MPIM is currently open in the user's sidebar. Only relevant for DMs and MPIMs.
  name: is_open
  type: boolean
- description: Whether the channel is frozen. Frozen channels do not accept new messages.
  name: is_frozen
  type: boolean
- description: Whether the channel is read-only. In read-only channels, only admins and approved users can post.
  name: is_read_only
  type: boolean
- description: Whether the channel only allows threaded replies. Top-level posts are not permitted.
  name: is_thread_only
  type: boolean
- description: Whether threading is disabled in this channel.
  name: is_non_threadable
  type: boolean
- description: Unix timestamp (in seconds) of when the conversation was created.
  name: created
  type: integer
- description: The user ID of the member who created this channel. Not present for DMs.
  name: creator
  type: string
- description: Unix timestamp of the last update to the conversation metadata (not the last message).
  name: updated
  type: integer
- description: The number of times this shared channel has been unlinked from a partner workspace.
  name: unlinked
  type: integer
- description: The channel's topic. Topics appear below the channel name in the Slack client and help describe what the channel is currently being used for.
  name: topic
  type: object
- description: The channel's purpose. Purposes describe the intended use of the channel and help users decide whether to join.
  name: purpose
  type: object
- description: A list of all previous names this channel has had. Useful for tracking channel history and identifying channels that have been renamed.
  name: previous_names
  type: array
- description: The approximate number of members in the channel. Only included in responses when explicitly requested via the include_num_members parameter. May not be perfectly accurate for large channels.
  name: num_members
  type: integer
- description: The IETF language code for the channel's locale. Only included in responses when explicitly requested via the include_locale parameter.
  name: locale
  type: string
- description: For direct messages, the user ID of the other participant. Not present for channels, groups, or MPIMs.
  name: user
  type: string
- description: An array of team (workspace) IDs that share this channel. Present for shared and Slack Connect channels.
  name: shared_team_ids
  type: array
- description: An array of team IDs for pending shared channel invitations.
  name: pending_shared
  type: array
- description: An array of team IDs for pending Slack Connect invitations.
  name: pending_connected_team_ids
  type: array
- description: The parent conversation ID if this is a sub-conversation or thread-only channel. Null for top-level conversations.
  name: parent_conversation
  type:
  - string
  - 'null'
- description: The team (workspace) ID providing context for this conversation. Useful in Enterprise Grid environments where channels may be shared across workspaces.
  name: context_team_id
  type: string
- description: Additional channel properties including canvas and tab configurations.
  name: properties
  type: object
- description: The timestamp of the last message read by the authenticated user in this channel.
  name: last_read
  type: string
- description: The most recent message in the channel. Only included in some API responses.
  name: latest
  type: object
- description: The number of unread messages the authenticated user has in this channel.
  name: unread_count
  type: integer
- description: The number of unread messages to display (may differ from unread_count based on notification settings).
  name: unread_count_display
  type: integer
- description: A priority value used for sorting channels in the sidebar.
  name: priority
  type: number
provider_name: Slack
provider_slug: slack
schema_file: json-schema/slack-channel-schema.json
slug: slack-channel
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
title: Slack Channel
---

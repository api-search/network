---
description: A Slack file object representing an uploaded file with its metadata and sharing information.
layout: schema
name: File
properties_list:
- description: Unique file identifier.
  name: id
  type: string
- description: Unix timestamp of when the file was created.
  name: created
  type: integer
- description: Unix timestamp.
  name: timestamp
  type: integer
- description: The file name.
  name: name
  type: string
- description: Title of the file.
  name: title
  type: string
- description: MIME type of the file.
  name: mimetype
  type: string
- description: Slack file type identifier (e.g., "png", "pdf", "snippet").
  name: filetype
  type: string
- description: Human-readable file type.
  name: pretty_type
  type: string
- description: User ID of the user who uploaded the file.
  name: user
  type: string
- description: Team ID of the user who uploaded the file.
  name: user_team
  type: string
- description: Whether the file content is editable.
  name: editable
  type: boolean
- description: File size in bytes.
  name: size
  type: integer
- description: File mode (e.g., "hosted", "external", "snippet", "post").
  name: mode
  type: string
- description: Whether the file is externally hosted.
  name: is_external
  type: boolean
- description: Type of external file.
  name: external_type
  type: string
- description: Whether the file is public.
  name: is_public
  type: boolean
- description: ''
  name: public_url_shared
  type: boolean
- description: ''
  name: display_as_bot
  type: boolean
- description: ''
  name: username
  type: string
- description: URL to access the file. Requires authentication.
  name: url_private
  type: string
- description: URL to download the file. Requires authentication.
  name: url_private_download
  type: string
- description: Permalink URL for the file.
  name: permalink
  type: string
- description: Public permalink URL for the file (if shared publicly).
  name: permalink_public
  type: string
- description: Array of channel IDs where the file is shared.
  name: channels
  type: array
- description: Array of private channel IDs where the file is shared.
  name: groups
  type: array
- description: Array of DM IDs where the file is shared.
  name: ims
  type: array
- description: Sharing information broken down by type.
  name: shares
  type: object
- description: Number of comments on the file.
  name: comments_count
  type: integer
provider_name: Slack
provider_slug: slack
schema_file: json-schema/slack-web-file-schema.json
slug: slack-web-file
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
title: File
---

---
description: A mail folder in a user's mailbox, such as Inbox and Drafts.
layout: schema
name: MailFolder
properties_list:
- description: The unique identifier for the mail folder.
  name: id
  type: string
- description: The mail folder's display name.
  name: displayName
  type: string
- description: The unique identifier for the mail folder's parent.
  name: parentFolderId
  type: string
- description: The number of immediate child folders in the current folder.
  name: childFolderCount
  type: integer
- description: The number of items in the mail folder.
  name: totalItemCount
  type: integer
- description: The number of unread items in the folder.
  name: unreadItemCount
  type: integer
- description: Indicates whether the mail folder is hidden.
  name: isHidden
  type: boolean
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-mail-folder-schema.json
slug: microsoft-graph-mail-folder
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: MailFolder
---

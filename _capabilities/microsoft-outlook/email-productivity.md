---
consumed_apis:
- graph-mail
description: Unified capability for Microsoft Outlook email productivity combining mail operations, folder management, and attachment handling via Microsoft Graph. Used by productivity teams, IT administrators, and automation engineers.
layout: capability
name: Microsoft Outlook Email Productivity
operations:
- description: List email messages
  method: GET
  name: list-messages
  path: /v1/messages
- description: Create a draft message
  method: POST
  name: create-draft
  path: /v1/messages
- description: Get a specific message
  method: GET
  name: get-message
  path: /v1/messages/{id}
- description: Update a message
  method: PATCH
  name: update-message
  path: /v1/messages/{id}
- description: Delete a message
  method: DELETE
  name: delete-message
  path: /v1/messages/{id}
- description: Send a draft message
  method: POST
  name: send-draft
  path: /v1/messages/{id}/send
- description: Reply to a message
  method: POST
  name: reply
  path: /v1/messages/{id}/reply
- description: Forward a message
  method: POST
  name: forward
  path: /v1/messages/{id}/forward
- description: List attachments
  method: GET
  name: list-attachments
  path: /v1/messages/{id}/attachments
- description: Add an attachment
  method: POST
  name: add-attachment
  path: /v1/messages/{id}/attachments
- description: Send a new email message
  method: POST
  name: send-mail
  path: /v1/send-mail
- description: List mail folders
  method: GET
  name: list-folders
  path: /v1/folders
- description: Create a mail folder
  method: POST
  name: create-folder
  path: /v1/folders
- description: Get a mail folder
  method: GET
  name: get-folder
  path: /v1/folders/{id}
- description: Update a mail folder
  method: PATCH
  name: update-folder
  path: /v1/folders/{id}
- description: Delete a mail folder
  method: DELETE
  name: delete-folder
  path: /v1/folders/{id}
- description: List messages in a folder
  method: GET
  name: list-folder-messages
  path: /v1/folders/{id}/messages
personas: []
provider_name: Microsoft Outlook
provider_slug: microsoft-outlook
search_terms:
- send a new email message directly
- update a message
- create folder
- reply to an email message
- list mail folders
- microsoft
- forward an email message to recipients
- copy a message to a different folder
- reply all to message
- enterprise
- get a specific message
- list mail folders in the mailbox
- mail folders
- messages in a folder
- email
- update a mail folder
- productivity
- delete a mail folder
- reply to message
- move a message to a different folder
- list messages in a folder
- copy message
- create a new mail folder
- delete an attachment from a message
- calendar
- get a specific email message by id
- email messages
- send draft
- list messages
- list folder messages
- send mail
- list folders
- message attachments
- add an attachment
- graph api
- send a draft message
- delete a message
- outlook
- update an email message
- get attachment
- single mail folder
- add an attachment to a message
- update folder
- create a draft email message
- list attachments for a message
- list email messages
- single email message
- add attachment
- reply to a message
- get a specific mail folder
- forward message
- get a specific attachment from a message
- list email messages in the outlook mailbox
- create a mail folder
- delete folder
- create draft
- move message
- list attachments
- forward a message
- delete message
- delete attachment
- send a new email message
- delete an email message
- office 365
- get message
- send an existing draft message
- forward
- get a mail folder
- create a draft message
- get folder
- list messages in a specific mail folder
- update message
- contacts
- reply all to an email message
- reply
- send a new email directly
slug: email-productivity
tags:
- Microsoft
- Outlook
- Email
- Productivity
- Graph API
tools:
- description: List email messages in the Outlook mailbox
  hints:
    openWorld: true
    readOnly: true
  name: list-messages
- description: Get a specific email message by ID
  hints:
    readOnly: true
  name: get-message
- description: Send a new email message directly
  hints:
    readOnly: false
  name: send-mail
- description: Create a draft email message
  hints:
    readOnly: false
  name: create-draft
- description: Send an existing draft message
  hints:
    readOnly: false
  name: send-draft
- description: Update an email message
  hints:
    idempotent: true
    readOnly: false
  name: update-message
- description: Delete an email message
  hints:
    destructive: true
    readOnly: false
  name: delete-message
- description: Reply to an email message
  hints:
    readOnly: false
  name: reply-to-message
- description: Reply all to an email message
  hints:
    readOnly: false
  name: reply-all-to-message
- description: Forward an email message to recipients
  hints:
    readOnly: false
  name: forward-message
- description: Copy a message to a different folder
  hints:
    readOnly: false
  name: copy-message
- description: Move a message to a different folder
  hints:
    readOnly: false
  name: move-message
- description: List mail folders in the mailbox
  hints:
    openWorld: true
    readOnly: true
  name: list-folders
- description: Create a new mail folder
  hints:
    readOnly: false
  name: create-folder
- description: Get a specific mail folder
  hints:
    readOnly: true
  name: get-folder
- description: Delete a mail folder
  hints:
    destructive: true
    readOnly: false
  name: delete-folder
- description: List messages in a specific mail folder
  hints:
    openWorld: true
    readOnly: true
  name: list-folder-messages
- description: List attachments for a message
  hints:
    readOnly: true
  name: list-attachments
- description: Get a specific attachment from a message
  hints:
    readOnly: true
  name: get-attachment
- description: Add an attachment to a message
  hints:
    readOnly: false
  name: add-attachment
- description: Delete an attachment from a message
  hints:
    destructive: true
    readOnly: false
  name: delete-attachment
---

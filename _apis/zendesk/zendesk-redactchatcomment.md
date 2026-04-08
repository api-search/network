---
aid: zendesk:zendesk-redactchatcomment
name: Zendesk Put  Api V2 Chat_redactions Ticket_id
tags:
- Ticket Comments
humanURL: 
properties: []
description: >-
  Permanently removes words or strings from a chat ticket's comment.   Wrap `<redact>` tags around the content in the chat comment you want redacted. Example:   ```json {   "text": "My ID number is <redact>847564</redact>!" } ```  The characters contained in the tag will be replaced by the ▇ symbol.  **Note**: This does not work on active chats. For chat tickets that predate March 2020, consider using [Redact Ticket Comment In Agent Workspace](#redact-ticket-comment-in-agent-workspace).  #### A...

---

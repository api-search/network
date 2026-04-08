---
aid: zendesk:zendesk-redactstringincomment
name: Zendesk Put  Api V2 Tickets Ticket_id Comments Ticket_comment_id Redact
tags:
- Ticket Comments
humanURL: 
properties: []
description: >-
  Permanently removes words or strings from a ticket comment. Specify the string to redact in an object with a `text` property. Example: `'{"text": "987-65-4320"}'`. The characters of the word or string are replaced by the ▇ symbol.  If the comment was made by email, the endpoint also attempts to redact the string from the original email retained by Zendesk for audit purposes.  **Note**: If you use the rich text editor, support for redacting formatted text (bold, italics, hyperlinks) is limited...

---

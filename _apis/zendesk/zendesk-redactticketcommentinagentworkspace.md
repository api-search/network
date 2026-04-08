---
aid: zendesk:zendesk-redactticketcommentinagentworkspace
name: Zendesk Put  Api V2 Comment_redactions Ticket_comment_id
tags:
- Ticket Comments
humanURL: 
properties: []
description: >-
  Redaction allows you to permanently remove words, strings, or attachments from a ticket comment.  In the `html_body` of the comment, wrap the content you want redacted in `<redact>` tags. Example:  ```json {   "html_body": "<div class=\"zd-comment\" dir=\"auto\">My ID number is <redact>847564</redact>!</div>",   "ticket_id":100 } ```  The characters in the redact tag will be replaced by the ▇ symbol.  To redact HTML elements such inline images, anchor tags, and links, add the `redact` tag att...

---

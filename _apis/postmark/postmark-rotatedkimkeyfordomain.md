---
aid: postmark:postmark-rotatedkimkeyfordomain
name: Postmark Rotate DKIM Key
tags:
- Domains API
humanURL: 
properties: []
description: >-
  Creates a new DKIM key to replace your current key. Until the DNS entries are confirmed, the new values will be in the `DKIMPendingHost` and `DKIMPendingTextValue` fields. After the new DKIM value is verified in DNS, the pending values will migrate to `DKIMTextValue` and `DKIMPendingTextValue` and Postmark will begin to sign emails with the new DKIM key.

---

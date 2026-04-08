---
aid: postmark:postmark-requestnewdkimkeyforsendersignature
name: Postmark Request a new DKIM Key
tags:
- Sender Signatures API
humanURL: 
properties: []
description: >-
  Requests a new DKIM key to be created. Until the DNS entries are confirmed, the new values will be in the `DKIMPendingHost` and `DKIMPendingTextValue` fields. After the new DKIM value is verified in DNS, the pending values will migrate to `DKIMTextValue` and `DKIMPendingTextValue` and Postmark will begin to sign emails with the new DKIM key.

---

---
aid: atlassian:atlassian-atlassianupdateawebhookforarepository
name: Update A Webhook For A Repository
tags:
- Repositories - Webhooks
humanURL: 
properties: []
description: >-
  Updates the specified webhook subscription.<br><br>The following properties can be mutated:<br><br>* `description`<br>* `url`<br>* `secret`<br>* `active`<br>* `events`<br><br>The hook's secret is used as a key to generate the HMAC hex digest sent in the<br>`X-Hub-Signature` header at delivery time. This signature is only generated<br>when the hook has a secret.<br><br>Set the hook's secret by passing the new value in the `secret` field. Passing a<br>`null` value in the `secret` field will rem...

---

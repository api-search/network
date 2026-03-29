---
aid: atlassian:atlassian-put-workspaces-workspace-hooks-uid
name: Update a webhook for a workspace
tags:
- - - - Workspaces
      - Webhooks
humanURL: 
properties: []
description: >-
  Updates the specified webhook subscription.  The following properties can be mutated:  * `description` * `url` * `secret` * `active` * `events`  The hook's secret is used as a key to generate the HMAC hex digest sent in the `X-Hub-Signature` header at delivery time. This signature is only generated when the hook has a secret.  Set the hook's secret by passing the new value in the `secret` field. Passing a `null` value in the `secret` field will remove the secret from the hook. The hook's secr...

---

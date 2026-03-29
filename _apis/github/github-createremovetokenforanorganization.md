---
aid: github:github-createremovetokenforanorganization
name: Create Remove Token For An Organization
tags:
- Create
- Remove
- Tokens
- Organizations
humanURL: 
properties: []
description: >-
  Returns a token that you can pass to the `config` script to remove a self-hosted runner from an organization. The token expires after one hour.  For example, you can replace `TOKEN` in the following example with the registration token provided by this endpoint to remove your self-hosted runner from an organization:  ``` ./config.sh remove --token TOKEN ```  Authenticated users must have admin access to the organization to use this endpoint.  OAuth tokens and personal access tokens (classic) n...

---

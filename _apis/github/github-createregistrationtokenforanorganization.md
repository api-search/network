---
aid: github:github-createregistrationtokenforanorganization
name: Create Registration Token For An Organization
tags:
- Create
- Registration
- Tokens
- Organizations
humanURL: 
properties: []
description: >-
  Returns a token that you can pass to the `config` script. The token expires after one hour.  For example, you can replace `TOKEN` in the following example with the registration token provided by this endpoint to configure your self-hosted runner:  ``` ./config.sh --url https://github.com/octo-org --token TOKEN ```  Authenticated users must have admin access to the organization to use this endpoint.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoi...

---

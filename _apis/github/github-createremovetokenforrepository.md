---
aid: github:github-createremovetokenforrepository
name: Create Remove Token For Repository
tags:
- Create
- Remove
- Tokens
- Repositories
humanURL: 
properties: []
description: >-
  Returns a token that you can pass to the `config` script to remove a self-hosted runner from an repository. The token expires after one hour.  For example, you can replace `TOKEN` in the following example with the registration token provided by this endpoint to remove your self-hosted runner from an organization:  ``` ./config.sh remove --token TOKEN ```  Authenticated users must have admin access to the repository to use this endpoint.  OAuth tokens and personal access tokens (classic) need ...

---

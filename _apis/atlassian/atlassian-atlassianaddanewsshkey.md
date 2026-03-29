---
aid: atlassian:atlassian-atlassianaddanewsshkey
name: Add A New Ssh Key
tags:
- Ssh
humanURL: 
properties: []
description: >-
  Adds a new SSH public key to the specified user account and returns the resulting key.<br><br>Example:<br><br>```<br>$ curl -X POST -H "Content-Type: application/json" -d '{"key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY user@myhost"}' https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys<br>```

---

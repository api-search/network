---
aid: atlassian:atlassian-atlassianupdateasshkey
name: Update A Ssh Key
tags:
- Ssh
humanURL: 
properties: []
description: >-
  Updates a specific SSH public key on a user's account<br><br>Note: Only the 'comment' field can be updated using this API. To modify the key or comment values, you must delete and add the key again.<br><br>Example:<br><br>```<br>$ curl -X PUT -H "Content-Type: application/json" -d '{"label": "Work key"}' https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/{b15b6026-9c02-4626-b4ad-b905f99f763a}<br>```

---

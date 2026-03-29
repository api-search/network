---
aid: atlassian:atlassian-atlassianupdatearepositorydeploykey
name: Update A Repository Deploy Key
tags:
- Deployments
humanURL: 
properties: []
description: >-
  Create a new deploy key in a repository.<br><br>The same key needs to be passed in but the comment and label can change.<br><br>Example:<br>```<br>$ curl -X PUT \<br>-H "Authorization " \<br>-H "Content-type: application/json" \<br>https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/1234 -d \<br>'{<br>    "label": "newlabel",<br>    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5u...

---

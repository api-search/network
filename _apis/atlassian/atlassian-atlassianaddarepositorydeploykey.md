---
aid: atlassian:atlassian-atlassianaddarepositorydeploykey
name: Add A Repository Deploy Key
tags:
- Deployments
humanURL: 
properties: []
description: >-
  Create a new deploy key in a repository. Note: If authenticating a deploy key<br>with an OAuth consumer, any changes to the OAuth consumer will subsequently<br>invalidate the deploy key.<br><br><br>Example:<br>```<br>$ curl -X POST \<br>-H "Authorization " \<br>-H "Content-type: application/json" \<br>https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys -d \<br>'{<br>    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJw...

---

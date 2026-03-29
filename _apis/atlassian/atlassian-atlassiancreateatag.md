---
aid: atlassian:atlassian-atlassiancreateatag
name: Create A Tag
tags:
- Refs
humanURL: 
properties: []
description: >-
  Creates a new tag in the specified repository.<br><br>The payload of the POST should consist of a JSON document that<br>contains the name of the tag and the target hash.<br><br>```<br>curl https://api.bitbucket.org/2.0/repositories/jdoe/myrepo/refs/tags \<br>-s -u jdoe -X POST -H "Content-Type: application/json" \<br>-d '{<br>    "name" : "new-tag-name",<br>    "target" : {<br>        "hash" : "a1b2c3d4e5f6",<br>    }<br>}'<br>```<br><br>This endpoint does support using short hash prefixes fo...

---

---
aid: atlassian:atlassian-atlassiancreateabranch
name: Create A Branch
tags:
- Refs
humanURL: 
properties: []
description: >-
  Creates a new branch in the specified repository.<br><br>The payload of the POST should consist of a JSON document that<br>contains the name of the tag and the target hash.<br><br>```<br>curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \<br>-s -u seanfarley -X POST -H "Content-Type: application/json" \<br>-d '{<br>    "name" : "smf/create-feature",<br>    "target" : {<br>        "hash" : "default",<br>    }<br>}'<br>```<br><br>This call requires authentication. Priv...

---

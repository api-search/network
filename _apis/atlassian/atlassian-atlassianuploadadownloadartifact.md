---
aid: atlassian:atlassian-atlassianuploadadownloadartifact
name: Upload A Download Artifact
tags:
- Downloads
humanURL: 
properties: []
description: >-
  Upload new download artifacts.<br><br>To upload files, perform a `multipart/form-data` POST containing one<br>or more `files` fields:<br><br>    $ echo Hello World > hello.txt<br>    $ curl -s -u evzijst -X POST https://api.bitbucket.org/2.0/repositories/evzijst/git-tests/downloads -F files=@hello.txt<br><br>When a file is uploaded with the same name as an existing artifact,<br>then the existing file will be replaced.

---

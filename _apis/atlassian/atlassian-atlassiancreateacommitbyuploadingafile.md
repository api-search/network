---
aid: atlassian:atlassian-atlassiancreateacommitbyuploadingafile
name: Create A Commit By Uploading A File
tags:
- Source - Repositories
humanURL: 
properties: []
description: >-
  This endpoint is used to create new commits in the repository by<br>uploading files.<br><br>To add a new file to a repository:<br><br>```<br>$ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \<br>  -F /repo/path/to/image.png=@image.png<br>```<br><br>This will create a new commit on top of the main branch, inheriting the<br>contents of the main branch, but adding (or overwriting) the<br>`image.png` file to the repository in the `/repo/path/to` directory.<br><br>To create a co...

---

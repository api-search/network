---
aid: atlassian:atlassian-atlassiangettherootdirectoryofthemainbranch
name: Get The Root Directory Of The Main Branch
tags:
- Source - Repositories
humanURL: 
properties: []
description: >-
  This endpoint redirects the client to the directory listing of the<br>root directory on the main branch.<br><br>This is equivalent to directly hitting<br>[/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)<br>without having to know the name or SHA1 of the repo's main branch.<br><br>To create new commits, [POST to this endpoint](#post)

---

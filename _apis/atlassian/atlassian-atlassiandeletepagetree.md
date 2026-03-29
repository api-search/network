---
aid: atlassian:atlassian-atlassiandeletepagetree
name: Delete Page Tree
tags:
- Experimental
humanURL: 
properties: []
description: >-
  Moves a pagetree rooted at a page to the space's trash:<br><br>- If the content's type is `page` and its status is `current`, it will be trashed including<br>all its descendants.<br>- For every other combination of content type and status, this API is not supported.<br><br>This API accepts the pageTree delete request and returns a task ID.<br>The delete process happens asynchronously.<br><br> Response example:<br> <br> {<br>      "id" : "1180606",<br>      "links" : {<br>           "status" :...

---

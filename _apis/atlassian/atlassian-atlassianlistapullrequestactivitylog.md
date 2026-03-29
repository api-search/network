---
aid: atlassian:atlassian-atlassianlistapullrequestactivitylog
name: List A Pull Request Activity Log
tags:
- Pullrequests
humanURL: 
properties: []
description: >-
  Returns a paginated list of the pull request's activity log.<br><br>This handler serves both a v20 and internal endpoint. The v20 endpoint<br>returns reviewer comments, updates, approvals and request changes. The internal<br>endpoint includes those plus tasks and attachments.<br><br>Comments created on a file or a line of code have an inline property.<br><br>Comment example:<br>```<br>{<br>    "pagelen": 20,<br>    "values": [<br>        {<br>            "comment": {<br>                "links...

---

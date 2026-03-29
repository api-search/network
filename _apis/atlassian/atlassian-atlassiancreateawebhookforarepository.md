---
aid: atlassian:atlassian-atlassiancreateawebhookforarepository
name: Create A Webhook For A Repository
tags:
- Repositories - Webhooks
humanURL: 
properties: []
description: >-
  Creates a new webhook on the specified repository.<br><br>Example:<br><br>```<br>$ curl -X POST -u credentials -H 'Content-Type: application/json'<br>  https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo-slug/hooks<br>  -d '<br>    {<br>      "description": "Webhook Description",<br>      "url": "https://example.com/",<br>      "active": true,<br>      "secret": "this is a really bad secret",<br>      "events": [<br>        "repo:push",<br>        "issue:created",<br>        "issu...

---

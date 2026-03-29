---
aid: atlassian:atlassian-atlassiangetcontentrestrictionstatusforuser
name: Get Content Restriction Status For User
tags:
- Content restrictions
humanURL: 
properties: []
description: >-
  Returns whether the specified content restriction applies to a user.<br>For example, if a page with `id=123` has a `read` restriction for a user with an account ID of<br>`384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192`, the following request will return `true`:<br><br>`/wiki/rest/api/content/123/restriction/byOperation/read/user?accountId=384093:32b4d9w0-f6a5-3535-11a3-9c8c88d10192`<br><br>Note that a response of `true` does not guarantee that the user can view the page, as it does not account f...

---

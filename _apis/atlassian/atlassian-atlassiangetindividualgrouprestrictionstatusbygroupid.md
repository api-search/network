---
aid: atlassian:atlassian-atlassiangetindividualgrouprestrictionstatusbygroupid
name: Get Content Restriction Status For Group
tags:
- Content restrictions
humanURL: 
properties: []
description: >-
  Returns whether the specified content restriction applies to a group.<br>For example, if a page with `id=123` has a `read` restriction for the `123456` group id,<br>the following request will return `true`:<br><br>`/wiki/rest/api/content/123/restriction/byOperation/read/byGroupId/123456`<br><br>Note that a response of `true` does not guarantee that the group can view the page, as it does not account for<br>account-inherited restrictions, space permissions, or even product access. For more<br>...

---

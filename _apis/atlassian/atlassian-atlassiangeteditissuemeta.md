---
aid: atlassian:atlassian-atlassiangeteditissuemeta
name: Get Edit Issue Metadata
tags:
- Issues
humanURL: 
properties: []
description: >-
  Returns the edit screen fields for an issue that are visible to and editable by the user. Use the information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put).<br><br>This endpoint will check for these conditions:<br><br>1.  Field is available on a field screen - through screen, screen scheme, issue type screen scheme, and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition.<br>2.  Field is visible in the [field configuration](ht...

---

---
aid: atlassian:atlassian-atlassianstoreavatar
name: Load Avatar
tags:
- Avatars
humanURL: 
properties: []
description: >-
  Loads a custom avatar for a project or issue type.<br><br>Specify the avatar's local file location in the body of the request. Also, include the following headers:<br><br> *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).<br> *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.<br><br>For example:  <br>`curl --request POST `<br><br>`--user email@example.com: `<br><br>`...

---

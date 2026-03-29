---
aid: atlassian:atlassian-atlassiancreateprojectavatar
name: Load Project Avatar
tags:
- Project avatars
humanURL: 
properties: []
description: >-
  Loads an avatar for a project.<br><br>Specify the avatar's local file location in the body of the request. Also, include the following headers:<br><br> *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).<br> *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.<br><br>For example:  <br>`curl --request POST `<br><br>`--user email@example.com: `<br><br>`--header 'X-Atlassia...

---

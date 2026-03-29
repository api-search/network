---
aid: atlassian:atlassian-atlassiancreateissuetypeavatar
name: Load Issue Type Avatar
tags:
- Issue types
humanURL: 
properties: []
description: >-
  Loads an avatar for the issue type.<br><br>Specify the avatar's local file location in the body of the request. Also, include the following headers:<br><br> *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).<br> *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.<br><br>For example:  <br>`curl --request POST \ --user email@example.com: \ --header 'X-Atlassian-Token: no...

---

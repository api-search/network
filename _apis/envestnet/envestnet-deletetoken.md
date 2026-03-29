---
aid: envestnet:envestnet-deletetoken
name: Delete Token
tags:
- Auth
humanURL: 
properties: []
description: >-
  This endpoint revokes the token passed in the Authorization header. This service is applicable for JWT-based (and all API key-based) authentication and also client credential (clientId and secret) based authentication. This service does not return a response body. The HTTP response code is 204 (success with no content). <br>Tokens generally have limited lifetime of up to 30 minutes. You will call this service when you finish working with one user, and you want to delete the valid token rather...

---

---
aid: neo4j:neo4j-getaccesstoken
name: Obtain an OAuth2 access token
tags:
- Authentication
humanURL: 
properties: []
description: >-
  Authenticates using client credentials to obtain a bearer token for API access. The client ID and client secret are provided using HTTP Basic Authentication. Access tokens expire after one hour and a new token must be obtained when the current one expires. A 403 Forbidden response indicates an expired token.

---

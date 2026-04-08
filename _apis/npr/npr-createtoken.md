---
aid: npr:npr-createtoken
name: NPR Create a new OAuth2 access token
tags:
- Authorization
humanURL: 
properties: []
description: >-
  Please be aware that the required parameters are contingent on the `grant_type` that you select.  For the `authorization_code` grant type, you are **required** to pass in the `code` and `redirect_uri` parameters.  For the `client_credentials` grant type, you do not need to pass in any additional parameters beyond the basic requirements. `code` and `redirect_uri` parameters will be ignored.  For the `device_code` grant type, you are **required** to pass in the `code` parameter. If you are a th...

---

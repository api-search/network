---
aid: box:box-post-oauth2-token
name: Request access token
tags:
- - - - Authorization
humanURL: 
properties: []
description: >-
  Request an Access Token using either a client-side obtained OAuth 2.0 authorization code or a server-side JWT assertion.  An Access Token is a string that enables Box to verify that a request belongs to an authorized session. In the normal order of operations you will begin by requesting authentication from the [authorize](#get-authorize) endpoint and Box will send you an authorization code.  You will then send this code to this endpoint to exchange it for an Access Token. The returned Access...

---

---
aid: tesla:tesla-createoauthtoken
name: Tesla Get an Access Token
tags:
- Authentication
humanURL: 
properties: []
description: >-
  Performs the login. Takes in an plain text email and password, matching the owner's login information for [https://my.teslamotors.com/user/login](https://my.teslamotors.com/user/login). Returns a `access_token` which is passed along as a header with all future requests to authenticate the user. You must provide the `Authorization: Bearer {access_token}` header in all other requests. The current client ID and secret are [available here](http://pastebin.com/YiLPDggh)

---

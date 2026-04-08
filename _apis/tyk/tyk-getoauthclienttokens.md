---
aid: tyk:tyk-getoauthclienttokens
name: Tyk List tokens for a provided API ID and OAuth-client ID
tags:
- OAuth
humanURL: 
properties: []
description: >-
  This endpoint allows you to retrieve a list of all current tokens and their expiry date for a provided API ID and OAuth-client ID .If page query parameter is sent the tokens will be paginated. This endpoint will work only for newly created tokens.         <br/>         <br/>         You can control how long you want to store expired tokens in this list using `oauth_token_expired_retain_period` gateway option, which specifies retain period for expired tokens stored in Redis. By default expired...

---

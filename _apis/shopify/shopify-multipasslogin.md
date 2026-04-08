---
aid: shopify:shopify-multipasslogin
name: Shopify Log in a customer using a Multipass token
tags:
- Multipass
humanURL: 
properties: []
description: >-
  Authenticates a customer using a Multipass token. The token is generated server-side by encrypting a JSON customer payload with AES-128-CBC and signing it with HMAC-SHA256 using keys derived from the store Multipass secret. The token is valid for 15 minutes and can only be used once. On success the customer is logged in and redirected to the return_to URL or the store homepage.

---

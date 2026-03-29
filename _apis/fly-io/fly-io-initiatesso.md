---
aid: fly-io:fly-io-initiatesso
name: Initiate SSO for an extension
tags:
- SSO
humanURL: 
properties: []
description: >-
  Called by Fly.io when a user runs a flyctl command to access the provider's dashboard (e.g., flyctl ext redis dashboard). The provider should verify the request signature and redirect the user to the appropriate dashboard page, using information from the Fly.io OAuth token to identify the user.

---

---
aid: vtex:vtex-3returntovtex
name: 3. Return to VTEX
tags:
- OAuth Flow
humanURL: 
properties: []
description: >-
  Through this endpoint, the provider will redirect the store administrator to the VTEX website using the `returnUrl` passed from VTEX to create token.  The `returnUrl` must be filled with your query string **authorizationCode**.  Example:  If you receive the following URL:  `https://store.vtex.com/return?authorizationCode=&otherparams...`  and your **authorizationCode** is `pro2018`. Then, you redirect the store administrator to: `https://store.vtex.com/return?authorizationCode=pro20...

---

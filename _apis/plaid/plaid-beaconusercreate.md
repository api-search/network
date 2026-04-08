---
aid: plaid:plaid-beaconusercreate
name: Plaid Create a Beacon User
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Create and scan a Beacon User against your Beacon Program, according to your program's settings.  When you submit a new user to `/beacon/user/create`, several checks are performed immediately:    - The user's PII (provided within the `user` object) is searched against all other users within the Beacon Program you specified. If a match is found that violates your program's "Duplicate Information Filtering" settings, the user will be returned with a status of `pending_review`.    - The user's P...

---

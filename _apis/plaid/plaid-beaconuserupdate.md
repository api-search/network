---
aid: plaid:plaid-beaconuserupdate
name: Plaid Update the identity data of a Beacon User
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Update the identity data for a Beacon User in your Beacon Program.  Similar to `/beacon/user/create`, several checks are performed immediately when you submit a change to `/beacon/user/update`:    - The user's updated PII is searched against all other users within the Beacon Program you specified. If a match is found that violates your program's "Duplicate Information Filtering" settings, the user will be returned with a status of `pending_review`.    - The user's updated PII is also searched...

---

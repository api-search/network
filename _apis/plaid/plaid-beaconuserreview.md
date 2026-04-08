---
aid: plaid:plaid-beaconuserreview
name: Plaid Review a Beacon User
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Update the status of a Beacon User.  When updating a Beacon User's status via this endpoint, Plaid validates that the status change is consistent with the related state for this Beacon User. Specifically, we will check:  1. Whether there are any associated Beacon Reports connected to the Beacon User, and 2. Whether there are any confirmed Beacon Report Syndications connected to the Beacon User.  When updating a Beacon User's status to "rejected", we enforce that either a Beacon Report has bee...

---

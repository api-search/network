---
aid: okta:okta-deactivateuser
name: Okta Deactivate User
tags:
- User
humanURL: 
properties: []
description: >-
  Deactivates a user. This operation can only be performed on users that do not have a `DEPROVISIONED` status. While the asynchronous operation (triggered by HTTP header `Prefer: respond-async`) is proceeding the user's `transitioningToStatus` property is `DEPROVISIONED`. The user's status is `DEPROVISIONED` when the deactivation process is complete.

---

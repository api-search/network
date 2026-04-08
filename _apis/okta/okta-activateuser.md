---
aid: okta:okta-activateuser
name: Okta Activate User
tags:
- User
humanURL: 
properties: []
description: >-
  Activates a user.  This operation can only be performed on users with a `STAGED` status.  Activation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `ACTIVE` when the activation process is complete.

---

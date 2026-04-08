---
aid: zendesk:zendesk-createorupdateuser
name: Zendesk Post  Api V2 Users Create_or_update
tags:
- Users
humanURL: 
properties: []
description: >-
  Creates a user if the user does not already exist, or updates an existing user identified by e-mail address or external ID.  If you don't specify a role parameter, the new user is assigned the role of end user.  If you need to create users without sending out a verification email, include a `"skip_verify_email": true` property in the body.  #### External ID Case Sensitivity  When providing an external id to identify an existing user to update, the search for the user record is not case sensit...

---

---
aid: zendesk:zendesk-deleteuseridentity
name: Zendesk Delete  Api V2 Users User_id Identities User_identity_id
tags:
- User Identities
humanURL: 
properties: []
description: >-
  Deletes the identity for a given user. In certain cases, a phone number associated with an identity is still visible on the user profile after the identity has been deleted via API. You can remove the phone number from the user profile by updating the `phone` attribute of the user to an empty string. See [Update User via API](/api-reference/ticketing/users/users/#update-user) for details and examples.  Deleting identities with type `messaging` could break messaging functionality. For example,...

---

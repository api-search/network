---
aid: sendgrid:sendgrid-deletecontactidentifier
name: Delete a Contact Identifier
tags:
- Contacts
humanURL: 
properties: []
description: >-
  **This endpoint can be used to delete one identifier from a contact.**  Deletion jobs are processed asynchronously.  Note this is different from deleting a contact. If the contact has only one identifier, the asynchronous request will fail. All contacts are required to have at least one identifier.  The request body field `identifier_type` must have a valid value of "EMAIL", "PHONENUMBERID", "EXTERNALID", or "ANONYMOUSID".

---

---
aid: sendgrid:sendgrid-createverifiedsender
name: Create Verified Sender Request
tags:
- Sender Verification
humanURL: 
properties: []
description: >-
  **This endpoint allows you to create a new Sender Identify**.  Upon successful submission of a `POST` request to this endpoint, an identity will be created, and a verification email will be sent to the address assigned to the `from_email` field. You must complete the verification process using the sent email to fully verify the sender.  If you need to resend the verification email, you can do so with the Resend Verified Sender Request, `/resend/{id}`, endpoint.  If you need to authenticate a ...

---

---
aid: sendgrid:twilio-sendgrid-verified-senders-api
name: Twilio SendGrid Verified Senders API
tags: []
properties:
  - url: openapi/tsg_verified_senders_v3.yaml
    type: OpenAPI
description: >-
  The Twilio SendGrid Verified Senders API allows you to programmatically manage
  the Sender Identities that are authorized to send email for your account. You
  can also manage Sender Identities in the [SendGrid application user
  interface](https://app.sendgrid.com/settings/sender_auth). See [**Single
  Sender
  Verification**](https://sendgrid.com/docs/ui/sending-email/sender-verification/)
  for more information.


  You an use this API to create new Sender Identities, retrieve a list of
  existing Sender Identities, check the status of a Sender Identity, update a
  Sender Identity, and delete a Sender Identity.


  This API offers additional operations to check for domains known to implement
  DMARC and resend verification emails to Sender Identities that have yet to
  complete the verification process.

---
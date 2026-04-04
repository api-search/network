---
aid: sendgrid:twilio-sendgrid-enforced-tls-api
name: Twilio SendGrid Enforced TLS API
tags: []
properties:
  - url: openapi/tsg_enforced_tls_v3.yaml
    type: OpenAPI
description: >-
  The Twilio SendGrid Enforced TLS API allows you to specify whether or not the
  recipient of your mail send is required to support TLS or have a valid
  certificate.


  Twilio SendGrid sends all emails with [Opportunistic
  TLS](https://sendgrid.com/blog/myth-opportunistic-tls-email-privacy/) by
  default, meaning email is sent with TLS, and if the recipient's inbox provider
  does not accept the TLS encryption, we then send the message unencrypted.


  You can optionally choose to enforce TLS encryption, meaning that if the
  recipient's inbox provider does not accept the TLS encryption, Twilio SendGrid
  drops the message and sends a block event with the message, TLS required but
  not supported as the description.

---
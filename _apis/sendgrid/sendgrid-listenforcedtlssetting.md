---
aid: sendgrid:sendgrid-listenforcedtlssetting
name: Retrieve current Enforced TLS settings.
tags:
- Enforced TLS
humanURL: 
properties: []
description: >-
  **This endpoint allows you to retrieve your current Enforced TLS settings.**  The Enforced TLS settings specify whether or not the recipient is required to support TLS or have a valid certificate.  If either `require_tls` or `require_valid_cert` is set to `true`, the recipient must support TLS 1.1 or higher or have a valid certificate. If these conditions are not met, Twilio SendGrid will drop the message and send a block event with “TLS required but not supported” as the description.

---

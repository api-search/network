---
aid: sendgrid:sendgrid-updateenforcedtlssetting
name: Update Enforced TLS settings
tags:
- Enforced TLS
humanURL: 
properties: []
description: >-
  **This endpoint allows you to update your Enforced TLS settings.**  To require TLS from recipients, set `require_tls` to `true`. If either `require_tls` or `require_valid_cert` is set to `true`, the recipient must support TLS 1.1 or higher or have a valid certificate. If these conditions are not met, Twilio SendGrid will drop the message and send a block event with “TLS required but not supported” as the description.

---

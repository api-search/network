---
aid: sendgrid:twilio-sendgrid-domain-authentication-api
name: Twilio SendGrid Domain Authentication API
tags: []
properties:
  - url: openapi/tsg_domain_authentication_v3.yaml
    type: OpenAPI
description: >-
  The Twilio SendGrid Domain Authentication API allows you to manage your
  authenticated domains and their settings.


  Domain Authentication is a required step when setting up your Twilio SendGrid
  account because it's essential to ensuring the deliverability of your email.
  Domain Authentication signals trustworthiness to email inbox providers and
  your recipients by approving SendGrid to send email on behalf of your domain.
  For more information, see [**How to Set Up Domain
  Authentication**](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-domain-authentication/).


  Each user may have a maximum of 3,000 authenticated domains and 3,000 link
  brandings. This limit is at the user level, meaning each Subuser belonging to
  a parent account may have its own 3,000 authenticated domains and 3,000 link
  brandings.

---
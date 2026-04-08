---
aid: sendgrid:sendgrid-listverifiedsenderdomain
name: Domain Warn List
tags:
- Sender Verification
humanURL: 
properties: []
description: >-
  **This endpoint returns a list of domains known to implement DMARC and categorizes them by failure type — hard failure or soft failure**.  Domains listed as hard failures will not deliver mail when used as a [Sender Identity](https://sendgrid.com/docs/for-developers/sending-email/sender-identity/) due to the domain's DMARC policy settings.  For example, using a `yahoo.com` email address as a Sender Identity will likely result in the rejection of your mail. For more information about DMARC, se...

---

---
aid: sendgrid:sendgrid-validatereversedns
name: Validate a reverse DNS record
tags:
- Reverse DNS
humanURL: 
properties: []
description: >-
  **This endpoint allows you to validate a reverse DNS record.**  Always check the `valid` property of the response’s `validation_results.a_record` object. This field will indicate whether it was possible to validate the reverse DNS record. If the `validation_results.a_record.valid` is `false`, this indicates only that Twilio SendGrid could not determine the validity your reverse DNS record — it may still be valid.  If validity couldn’t be determined, you can check the value of `validation_resu...

---

---
aid: stripe:stripe-postidentityverificationsessionssessionredact
name: Stripe Post   Identity Verification Sessions Session Redact
tags:
- Identity
- Post
- Redact
- Sessions
- Verification
humanURL: 
properties: []
description: >-
  <p>Redact a VerificationSession to remove all collected information from Stripe. This will redact the VerificationSession and all objects related to it, including VerificationReports, Events, request logs, etc.</p>  <p>A VerificationSession object can be redacted when it is in <code>requires_input</code> or <code>verified</code> <a href="/docs/identity/how-sessions-work">status</a>. Redacting a VerificationSession in <code>requires_action</code> state will automatically cancel it.</p>  <p>The...

---

---
aid: stripe:stripe-postcreditnotes
name: Stripe Post   Credit Notes
tags:
- Credit
- Notes
- Post
humanURL: 
properties: []
description: >-
  <p>Issue a credit note to adjust the amount of a finalized invoice. For a <code>status=open</code> invoice, a credit note reduces its <code>amount_due</code>. For a <code>status=paid</code> invoice, a credit note does not affect its <code>amount_due</code>. Instead, it can result in any combination of the following:</p>  <ul> <li>Refund: create a new refund (using <code>refund_amount</code>) or link an existing refund (using <code>refund</code>).</li> <li>Customer balance credit: credit the c...

---

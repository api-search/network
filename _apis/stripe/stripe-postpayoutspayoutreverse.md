---
aid: stripe:stripe-postpayoutspayoutreverse
name: Stripe Post   Payouts Reverse
tags:
- Payouts
- Post
- Reverse
humanURL: 
properties: []
description: >-
  <p>Reverses a payout by debiting the destination bank account. At this time, you can only reverse payouts for connected accounts to US bank accounts. If the payout is in the <code>pending</code> status, use <code>/v1/payouts/:id/cancel</code> instead.</p>  <p>By requesting a reversal through <code>/v1/payouts/:id/reverse</code>, you confirm that the authorized signatory of the selected bank account authorizes the debit on the bank account and that no other authorization is required.</p>

---

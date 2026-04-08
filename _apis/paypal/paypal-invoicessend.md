---
aid: paypal:paypal-invoicessend
name: Paypal Send invoice
tags:
- Invoices
humanURL: 
properties: []
description: >-
  Sends or schedules an invoice, by ID, to be sent to a customer. The action depends on the invoice issue date:<ul><li>If the invoice issue date is current or in the past, sends the invoice immediately.</li><li>If the invoice issue date is in the future, schedules the invoice to be sent on that date.</li></ul>To suppress the merchant's email notification, set the `send_to_invoicer` body parameter to `false`. To send the invoice through a share link and not through PayPal, set the <code>send_to_...

---

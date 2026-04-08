---
aid: paypal:paypal-invoicescreate
name: Paypal Create draft invoice
tags:
- Invoices
humanURL: 
properties: []
description: >-
  Creates a draft invoice. To move the invoice from a draft to payable state, you must <a href="#invoices_send">send the invoice</a>.<br/><br/>In the JSON request body, include invoice details including merchant information. The <code>invoice</code> object must include an <code>items</code> array.<blockquote><strong>Note:</strong> The merchant that you specify in an invoice must have a PayPal account in good standing.</blockquote>.

---

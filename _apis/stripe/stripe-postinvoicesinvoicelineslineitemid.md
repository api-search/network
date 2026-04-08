---
aid: stripe:stripe-postinvoicesinvoicelineslineitemid
name: Stripe Post   Invoices Invoice Lines Line Item Id
tags:
- Identifiers
- Invoice
- Invoices
- Item
- Line
- Lines
- Post
humanURL: 
properties: []
description: >-
  <p>Updates an invoice’s line item. Some fields, such as <code>tax_amounts</code>, only live on the invoice line item, so they can only be updated through this endpoint. Other fields, such as <code>amount</code>, live on both the invoice item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well. Updating an invoice’s line item is only possible before the invoice is finalized.</p>

---

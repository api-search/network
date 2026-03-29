---
aid: bigcommerce:bigcommerce-createpaymentaccesstoken
name: Create Payment Access Token
tags:
- Payments
- Access
- Tokens
humanURL: 
properties: []
description: >-
  Use this endpoint to create a payment access token. A payment access token is required to process payments with the BigCommerce API.  You can also generate a payment access token during checkout by using the `completeCheckout` mutation in the [GraphQL Storefront API](/docs/storefront/cart-checkout/guide/graphql-storefront#handling-payments).  After the token is created, use the token to [Process a payment](/docs/rest-payments/processing#process-payment).  **Required Fields** * order_id

---

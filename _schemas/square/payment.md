---
description: Represents a payment processed by the Square API, including credit cards, gift cards, digital wallets, ACH bank transfers, cash, and external payments.
layout: schema
name: Square Payment
properties_list:
- description: A unique ID for the payment.
  name: id
  type: string
- description: The timestamp of when the payment was created, in RFC 3339 format.
  name: created_at
  type: string
- description: The timestamp of when the payment was last updated, in RFC 3339 format.
  name: updated_at
  type: string
- description: The amount processed for this payment, not including tip_money.
  name: amount_money
  type: object
- description: The amount designated as a tip.
  name: tip_money
  type: object
- description: The total amount for the payment, including amount_money and tip_money.
  name: total_money
  type: object
- description: The amount the developer is taking as a fee for facilitating the payment on behalf of the seller.
  name: app_fee_money
  type: object
- description: The amount of money approved for this payment.
  name: approved_money
  type: object
- description: The processing fees and fee adjustments assessed by Square for this payment.
  name: processing_fee
  type: array
- description: The total amount of the payment refunded to date.
  name: refunded_money
  type: object
- description: Indicates whether the payment is APPROVED, PENDING, COMPLETED, CANCELED, or FAILED.
  name: status
  type: string
- description: The duration of time after the payment's creation when Square automatically applies the delay_action to the payment, in RFC 3339 duration format.
  name: delay_duration
  type: string
- description: The action to be applied to the payment when the delay_duration has elapsed. Current values include CANCEL and COMPLETE.
  name: delay_action
  type: string
- description: The read-only timestamp of when the delay_action is automatically applied, in RFC 3339 format.
  name: delayed_until
  type: string
- description: The source type for this payment.
  name: source_type
  type: string
- description: Details about a card payment. Only populated if the source_type is CARD.
  name: card_details
  type: object
- description: Details about a cash payment. Only populated if the source_type is CASH.
  name: cash_details
  type: object
- description: Details about a bank account payment. Only populated if the source_type is BANK_ACCOUNT.
  name: bank_account_details
  type: object
- description: Details about an external payment. Only populated if the source_type is EXTERNAL.
  name: external_details
  type: object
- description: Details about a wallet payment. Only populated if the source_type is WALLET.
  name: wallet_details
  type: object
- description: Details about a Buy Now Pay Later payment. Only populated if the source_type is BUY_NOW_PAY_LATER.
  name: buy_now_pay_later_details
  type: object
- description: Details about a Square Account payment. Only populated if the source_type is SQUARE_ACCOUNT.
  name: square_account_details
  type: object
- description: The ID of the location associated with the payment.
  name: location_id
  type: string
- description: The ID of the order associated with the payment.
  name: order_id
  type: string
- description: An optional ID that associates the payment with an entity in another system.
  name: reference_id
  type: string
- description: The ID of the customer associated with the payment.
  name: customer_id
  type: string
- description: An optional ID of the employee associated with taking the payment.
  name: employee_id
  type: string
- description: An optional ID of the TeamMember associated with taking the payment.
  name: team_member_id
  type: string
- description: A list of refund IDs associated with the payment.
  name: refund_ids
  type: array
- description: An assessment of the risk associated with the payment.
  name: risk_evaluation
  type: object
- description: The buyer's email address.
  name: buyer_email_address
  type: string
- description: The buyer's billing address.
  name: billing_address
  type: object
- description: The buyer's shipping address.
  name: shipping_address
  type: object
- description: An optional note to include when creating a payment.
  name: note
  type: string
- description: Additional payment information that gets added to the customer's card statement.
  name: statement_description_identifier
  type: string
- description: The payment's receipt number.
  name: receipt_number
  type: string
- description: The URL for the payment's receipt.
  name: receipt_url
  type: string
- description: Used for optimistic concurrency. This opaque token identifies a specific version of the Payment object.
  name: version_token
  type: string
provider_name: Square
provider_slug: square
schema_file: json-schema/payment.json
slug: payment
tags:
- Bookings
- Catalog
- Checkout
- Customers
- Disputes
- Ecommerce
- Financial Technology
- Gift Cards
- Inventory
- Invoicing
- Labor
- Locations
- Loyalty
- Merchants
- Orders
- Payments
- Point of Sale
- Refunds
- Retail
- Subscriptions
- Team
- Terminal
- Webhooks
title: Square Payment
---

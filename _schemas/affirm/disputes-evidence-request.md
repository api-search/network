---
description: Request body for submitting evidence to contest a dispute. May include file references, textual explanations, and shipping/tracking details.
layout: schema
name: EvidenceRequest
properties_list:
- description: Array of file identifiers uploaded via the Files API to attach as documentary evidence.
  name: files
  type: array
- description: Textual explanation of the merchant's position and why the dispute should be decided in the merchant's favor.
  name: explanation
  type: string
- description: Shipment tracking number demonstrating that the order was delivered as expected.
  name: tracking_number
  type: string
- description: Name of the shipping carrier used for the disputed order.
  name: shipping_carrier
  type: string
- description: Description or summary of communications with the customer regarding the disputed order.
  name: customer_communication
  type: string
- description: Description of the merchant's refund policy as shown to the customer at the time of purchase.
  name: refund_policy_disclosure
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/disputes-evidence-request-schema.json
slug: disputes-evidence-request
tags: []
title: EvidenceRequest
---

---
aid: zendesk:zendesk-verifysupportaddressforwarding
name: Zendesk Put  Api V2 Recipient_addresses Support_address_id Verify
tags:
- Support Addresses
humanURL: 
properties: []
description: >-
  Sends a test email to the specified support address to verify that email forwarding for the address works. An external support address won't work in Zendesk Support until it's verified.  **Note**: You don't need to verify Zendesk system support addresses.  The endpoint takes the following body: `{"type": "forwarding"}`. The value of the `type` property defaults to "forwarding" if none is specified, but the values "spf" and "dns" are also accepted.  Use this endpoint after [adding](#create-sup...

---

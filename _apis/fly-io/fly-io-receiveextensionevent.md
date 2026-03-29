---
aid: fly-io:fly-io-receiveextensionevent
name: Receive a machine event webhook from Fly.io
tags:
- Webhooks
humanURL: 
properties: []
description: >-
  Fly.io sends CloudEvents-format webhook payloads to this provider endpoint when Machine or account events occur that are relevant to an extension. Providers should verify the HMAC-SHA256 signature using the webhook signing secret provided by Fly.io and process the event accordingly.

---

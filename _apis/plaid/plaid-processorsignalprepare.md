---
aid: plaid:plaid-processorsignalprepare
name: Plaid Opt-in a processor token to Signal
tags:
- Plaid
humanURL: 
properties: []
description: >-
  When a processor token is not initialized with Signal, call `/processor/signal/prepare` to opt-in that processor token to the Signal data collection process, which will improve the accuracy of the Signal score.  If this endpoint is called with a processor token that is already initialized with Signal, it will return a 200 response and will not modify the processor token.

---

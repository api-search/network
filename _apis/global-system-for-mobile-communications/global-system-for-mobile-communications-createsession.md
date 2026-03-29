---
aid: global-system-for-mobile-communications:global-system-for-mobile-communications-createsession
name: Creates a new session
tags:
- QoS Sessions
humanURL: 
properties: []
description: >-
  Create QoS Session to manage latency/throughput priorities  If the qosStatus in the API response is "AVAILABLE" and a notification callback is provided the client will receive in addition to the response a `QOS_STATUS_CHANGED` event notification with `qosStatus` as `AVAILABLE`.  If the `qosStatus` in the API response is `REQUESTED`, the client will receive either - a `QOS_STATUS_CHANGED` event notification with `qosStatus` as `AVAILABLE` after the network notifies that it has created the requ...

---

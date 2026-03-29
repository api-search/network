---
aid: global-system-for-mobile-communications:global-system-for-mobile-communications-deletesession
name: Delete a QoS session
tags:
- QoS Sessions
humanURL: 
properties: []
description: >-
  Release resources related to QoS session  If the notification callback is provided and the `qosStatus` of the session was `AVAILABLE` the client will receive in addition to the response a `QOS_STATUS_CHANGED` event with - `qosStatus` as `UNAVAILABLE` and - `statusInfo` as `DELETE_REQUESTED` There will be no notification event if the `qosStatus` was already `UNAVAILABLE`.  **NOTES:** - The access token may be either 2-legged or 3-legged. - If a 3-legged access token is used, the end user (and ...

---

---
aid: microsoft-graph:microsoft-graph-communicationscallscallkeepalive
name: Microsoft Graph Invoke action keepAlive
tags:
- Communications.call
humanURL: 
properties: []
description: >-
  Make a request to this API every 15 to 45 minutes to ensure that an ongoing call remains active. A call that does not receive this request within 45 minutes is considered inactive and will subsequently end. At least one successful request must be made within 45 minutes of the previous request, or the start of the call. We recommend that you send a request in shorter time intervals (every 15 minutes). Make sure that these requests are successful to prevent the call from timing out and ending. ...

---

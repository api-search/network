---
aid: box:box-options-events
name: Get events long poll endpoint
tags:
- - - - Events
humanURL: 
properties: []
description: >-
  Returns a list of real-time servers that can be used for long-polling updates to the [event stream](#get-events).  Long polling is the concept where a HTTP request is kept open until the server sends a response, then repeating the process over and over to receive updated responses.  Long polling the event stream can only be used for user events, not for enterprise events.  To use long polling, first use this endpoint to retrieve a list of long poll URLs. Next, make a long poll request to any ...

---

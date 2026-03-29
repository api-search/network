---
aid: fluentd:fluentd-postevent
name: Post a log event
tags:
- Events
humanURL: 
properties: []
description: >-
  Posts a single log event to Fluentd with the specified tag. The tag determines which Fluentd match rules route the event downstream. The request body can be JSON, MessagePack, or form-encoded. When sending JSON, the Content-Type must be application/json. The time field can be supplied in the body or omitted to use the server receive time.

---

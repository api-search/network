---
aid: symphony:symphony-get-v4-stream-sid-message
name: Symphony Get messages from an existing stream.
tags:
- Stream
humanURL: 
properties: []
description: >-
  A caller can fetch all unseen messages by passing the timestamp of the last message seen as the since parameter and the number of messages with the same timestamp value already seen as the skip parameter. This means that every message will be seen exactly once even in the case that an additional message is processed with the same timestamp as the last message returned by the previous call, and the case where there are more than maxMessages with the same timestamp value.  This method is intend...

---

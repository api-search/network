---
aid: symphony:symphony-get-v1-message-search
name: Symphony Search messages
tags:
- Message
humanURL: 
properties: []
description: >-
  Search messages according to the specified criteria. The "query" parameter takes a search query defined as "field:value" pairs combined by the operator "AND" (e.g. "text:foo AND autor:bar"). Supported fields are  (case-insensitive): "text", "author", "hashtag", "cashtag", "mention", "signal", "fromDate", "toDate",  "streamId", "streamType".  "text" search requires a "streamId" to be specified.  "streamType" accepts one of the following values: "chat" (IMs and MIMs), "im", "mim", "chatroom", "...

---

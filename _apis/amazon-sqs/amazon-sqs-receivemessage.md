---
aid: amazon-sqs:amazon-sqs-receivemessage
name: Receive messages from a queue
tags:
- Messages
humanURL: 
properties: []
description: >-
  Retrieves one or more messages (up to 10) from the specified queue. Using the WaitTimeSeconds parameter enables long-poll support. Short poll is the default behavior where a weighted random set of machines is sampled on a ReceiveMessage call. Long polling reduces the number of empty responses and false empty responses.

---

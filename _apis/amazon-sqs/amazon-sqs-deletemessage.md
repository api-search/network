---
aid: amazon-sqs:amazon-sqs-deletemessage
name: Delete a message from a queue
tags:
- Messages
humanURL: 
properties: []
description: >-
  Deletes the specified message from the specified queue. To select the message to delete, use the ReceiptHandle of the message (not the MessageId which you receive when you send the message). Amazon SQS can delete a message from a queue even if a visibility timeout setting causes the message to be locked by another consumer.

---

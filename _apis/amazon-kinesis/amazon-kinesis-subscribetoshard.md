---
aid: amazon-kinesis:amazon-kinesis-subscribetoshard
name: Subscribe to a shard for enhanced fan-out
tags:
- Consumers
humanURL: 
properties: []
description: >-
  This operation establishes an HTTP/2 connection between the consumer you specify in the ConsumerARN parameter and the shard you specify in the ShardId parameter. After the connection is successfully established, Kinesis Data Streams pushes records from the shard to the consumer over this connection. Before you call this operation, call RegisterStreamConsumer to register the consumer with the data stream. The connection persists for up to 5 minutes.

---

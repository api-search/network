---
aid: amazon-kinesis:amazon-kinesis-putrecord
name: Write a single data record to a stream
tags:
- Records
humanURL: 
properties: []
description: >-
  Writes a single data record into an Amazon Kinesis data stream. You must specify the name or ARN of the stream that captures, stores, and transports the data, a partition key, and the data blob itself. The partition key is used by Kinesis Data Streams to distribute data across shards. Kinesis Data Streams segregates the data records that belong to a stream into multiple shards, using the partition key associated with each data record to determine the shard to which a given data record belongs.

---

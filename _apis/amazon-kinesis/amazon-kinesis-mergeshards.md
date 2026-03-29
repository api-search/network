---
aid: amazon-kinesis:amazon-kinesis-mergeshards
name: Merge two adjacent shards
tags:
- Shards
humanURL: 
properties: []
description: >-
  Merges two adjacent shards in a Kinesis data stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data. Two shards are considered adjacent if the union of the hash key ranges for the two shards form a contiguous set with no gaps.

---

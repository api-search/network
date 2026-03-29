---
aid: amazon-kinesis:amazon-kinesis-getrecords
name: Get data records from a shard
tags:
- Records
humanURL: 
properties: []
description: >-
  Gets data records from a Kinesis data stream's shard. Specify a shard iterator using the ShardIterator parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. Each call to GetRecords can return up to 10 MiB of data and up to 10,000 records. Each shard can support up to 5 transactions per second for reads, up to a maximum total data read rate of 2 MiB per second.

---

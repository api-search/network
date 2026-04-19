---
description: A data record in an Amazon Kinesis data stream.
layout: schema
name: Record
properties_list:
- description: The unique identifier of the record in the shard.
  name: SequenceNumber
  type: string
- description: The approximate time the record was inserted.
  name: ApproximateArrivalTimestamp
  type: string
- description: The data blob (base64-encoded).
  name: Data
  type: string
- description: Identifies which shard the data record belongs to.
  name: PartitionKey
  type: string
provider_name: Amazon Kinesis
provider_slug: amazon-kinesis
schema_file: json-schema/amazon-kinesis-record-schema.json
slug: amazon-kinesis-record
tags:
- Analytics
- Big Data
- Data Processing
- Real-Time
- Streaming
title: Record
---

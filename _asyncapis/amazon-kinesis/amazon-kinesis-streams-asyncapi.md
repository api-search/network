---
channels:
- description: A shard within a Kinesis data stream. Each shard is an append-only, ordered sequence of data records. Producers write records to shards via partition keys, and consumers read records sequentially. Each shard provides 1 MiB/sec write capacity and 2 MiB/sec read capacity (shared among polling consumers), or 2 MiB/sec dedicated throughput per enhanced fan-out consumer.
  name: kinesisStreamShard
- description: A dedicated HTTP/2 push channel between a registered consumer and a specific shard. Established via the SubscribeToShard API, this channel pushes SubscribeToShardEvent messages containing data records at up to 2 MiB/sec per shard per consumer. Each subscription lasts up to 5 minutes before requiring renewal.
  name: enhancedFanOutSubscription
- description: When configured as an AWS Lambda event source, Kinesis Data Streams automatically invokes a Lambda function with batches of records from each shard. The Lambda service manages shard iterator lifecycle, checkpointing, and retry logic. Each shard is processed by one Lambda invocation at a time (unless parallelization is configured).
  name: lambdaEventSource
description: Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. This AsyncAPI specification describes the event-driven consumer patterns for Kinesis Data Streams, including enhanced fan-out via SubscribeToShard (HTTP/2 push), polling via GetRecords, and integration with AWS Lambda as an event source. Kinesis Data Streams captures data from producers and makes it available to consumers in real time. Data records are organized into shards, and consumers read records sequentially from shards using shard iterators or enhanced fan-out subscriptions.
layout: asyncapi
messages:
- description: ''
  name: KinesisRecord
  summary: A single data record in a Kinesis data stream. Each record contains a data blob, partition key, and is assigned a unique sequence number and approximate arrival timestamp by the service.
  title: Kinesis Data Record
- description: ''
  name: SubscribeToShardEvent
  summary: An event pushed to an enhanced fan-out consumer over an HTTP/2 connection. Contains a batch of data records along with a continuation sequence number and lag metrics.
  title: Subscribe to Shard Event
- description: ''
  name: LambdaKinesisEvent
  summary: The event payload delivered to an AWS Lambda function when a Kinesis data stream is configured as an event source. Contains an array of Kinesis event records with metadata including the event source ARN, region, and event name.
  title: Lambda Kinesis Event
name: Amazon Kinesis Data Streams
provider_name: Amazon Kinesis
provider_slug: amazon-kinesis
servers:
- description: Amazon Kinesis Data Streams regional endpoint. Enhanced fan-out uses HTTP/2 server push over this endpoint. Polling consumers use standard HTTPS POST requests.
  name: production
  protocol: https
  url: ''
slug: amazon-kinesis-streams-asyncapi
spec_file: asyncapi/amazon-kinesis-streams-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/amazon-kinesis/refs/heads/main/asyncapi/amazon-kinesis-streams-asyncapi.yml
tags:
- Analytics
- Big Data
- Data Processing
- Real-Time
- Streaming
- AsyncAPI
- Webhooks
- Events
version: '2013-12-02'
---

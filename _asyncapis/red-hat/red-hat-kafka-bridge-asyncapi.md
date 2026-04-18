---
channels:
- description: Channel representing messages produced to and consumed from a specific Kafka topic through the HTTP bridge. Producers send messages via HTTP POST and consumers receive messages by polling the bridge endpoint.
  name: topics.{topic}.messages
  operation: publish
  operation_id: produceMessage
  summary: Produce message to topic
- description: Channel representing offset management for a consumer group. Consumers can commit offsets to track their progress and seek to specific offsets for replay or recovery.
  name: consumers.{group_id}.offsets
  operation: publish
  operation_id: commitOffsets
  summary: Commit consumer offsets
description: The Red Hat Streams for Apache Kafka Bridge provides an HTTP-based interface for producing and consuming messages to and from Apache Kafka topics without requiring a native Kafka client. Deployed on OpenShift as part of Red Hat Streams for Apache Kafka, the bridge enables REST clients to participate in event streaming by sending and receiving messages through standard HTTP requests.
layout: asyncapi
messages:
- description: A message record containing the value to produce to a Kafka topic, with optional key, partition, and headers for controlling message routing and metadata.
  name: ProducerRecord
  summary: A single message to be produced to a Kafka topic.
  title: Producer Record
- description: A batch of message records to produce to a Kafka topic in a single HTTP request for improved throughput.
  name: ProducerRecordBatch
  summary: A batch of messages to be produced to a Kafka topic.
  title: Producer Record Batch
- description: A message record received from a Kafka topic through the bridge consumer, including the topic, partition, offset, and the message key and value.
  name: ConsumerRecord
  summary: A message consumed from a Kafka topic.
  title: Consumer Record
- description: A request to commit offsets for specific topic partitions, marking the consumer's progress in processing messages.
  name: OffsetCommit
  summary: Offset commit request for a consumer group.
  title: Offset Commit
name: Red Hat Streams for Apache Kafka Bridge Events
provider_name: Red Hat
provider_slug: red-hat
servers:
- description: The Kafka Bridge HTTP endpoint deployed on OpenShift. The bridge accepts HTTP requests and translates them to Kafka protocol operations for producing and consuming messages.
  name: kafkaBridge
  protocol: https
  url: '{bridge_url}'
slug: red-hat-kafka-bridge-asyncapi
spec_file: asyncapi/red-hat-kafka-bridge-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/red-hat/refs/heads/main/asyncapi/red-hat-kafka-bridge-asyncapi.yml
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
- AsyncAPI
- Webhooks
- Events
version: '3.1'
---

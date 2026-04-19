---
channels:
- description: A DynamoDB Stream for a specific table. When DynamoDB Streams is enabled on a table, every modification to data items in the table is captured as a stream record. Each stream record is written in near-real time and appears in the stream in the order in which the actual modifications occurred. Stream records are organized into shards, which are containers for stream records.
  name: streamRecord
- description: DynamoDB Streams can be configured as an event source for AWS Lambda. Lambda polls the stream and invokes the function synchronously with a batch of stream records. The event source mapping controls the batch size, starting position, and error handling behavior.
  name: lambdaTrigger
description: 'Amazon DynamoDB Streams captures a time-ordered sequence of item-level modifications in any DynamoDB table and stores this information in a log for up to 24 hours. Applications can access this log and view the data items as they appeared before and after they were modified, in near-real time. DynamoDB Streams writes stream records in near-real time so that you can build applications that consume these streams and take action based on the contents. A stream record contains information about a data modification to a single item in a DynamoDB table. Stream records are organized into groups called shards. Each shard acts as a container for multiple stream records and contains information required for accessing and iterating through these records. Stream records can be configured to capture one of four view types: KEYS_ONLY (only the key attributes of the modified item), NEW_IMAGE (the entire item as it appears after modification), OLD_IMAGE (the entire item as it appeared before
  modification), or NEW_AND_OLD_IMAGES (both the new and old images of the item).'
layout: asyncapi
messages:
- description: 'Contains the new image of the item that was inserted. The exact attributes included depend on the StreamViewType: KEYS_ONLY returns just the key attributes, NEW_IMAGE returns the entire new item, OLD_IMAGE returns nothing for inserts, NEW_AND_OLD_IMAGES returns the new item only (no old image exists'
  name: StreamRecordInsert
  summary: A stream record generated when a new item is inserted
  title: Item Insert Stream Record
- description: Contains the old and/or new image of the item that was modified. The exact attributes included depend on the StreamViewType. With NEW_AND_OLD_IMAGES, both the pre-modification and post-modification item data are included, enabling diff-based processing.
  name: StreamRecordModify
  summary: A stream record generated when an existing item is modified
  title: Item Modify Stream Record
- description: Contains the old image of the item that was deleted. The exact attributes included depend on the StreamViewType. Removal events are generated for explicit deletes (DeleteItem, BatchWriteItem) as well as TTL-expired items. TTL deletions are indicated by a userIdentity field with principalId 'dynamodb
  name: StreamRecordRemove
  summary: A stream record generated when an item is deleted
  title: Item Remove Stream Record
- description: When DynamoDB Streams is configured as a Lambda event source, the Lambda service polls the stream and batches records together before invoking the function. The event contains an array of stream records in the Records field. The batch size is configurable from 1 to 10000 records.
  name: LambdaStreamEvent
  summary: Batch of DynamoDB stream records delivered to a Lambda function
  title: Lambda DynamoDB Stream Event
name: Amazon DynamoDB Streams
provider_name: Amazon DynamoDB
provider_slug: dynamodb
servers:
- description: Amazon DynamoDB Streams regional endpoint. Stream records are accessed via the DynamoDB Streams API using HTTP/JSON protocol with AWS SigV4 authentication.
  name: production
  protocol: https
  url: ''
- description: AWS Lambda integration endpoint. DynamoDB Streams can trigger Lambda functions automatically via event source mapping, providing a serverless stream processing pattern.
  name: lambda-trigger
  protocol: https
  url: ''
slug: dynamodb-streams-asyncapi
spec_file: asyncapi/dynamodb-streams-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/dynamodb/refs/heads/main/asyncapi/dynamodb-streams-asyncapi.yml
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
- AsyncAPI
- Webhooks
- Events
version: '2012-08-10'
---

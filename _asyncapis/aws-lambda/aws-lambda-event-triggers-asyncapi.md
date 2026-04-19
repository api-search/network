---
channels:
- description: Amazon S3 sends event notifications to Lambda when objects are created, modified, or deleted in a bucket. S3 invokes your function asynchronously with an event that contains details about the object. You configure notifications on the S3 bucket to specify which events trigger the function.
  name: s3/event
  operation: subscribe
  operation_id: onS3Event
  summary: Receive S3 object event notifications
- description: Amazon DynamoDB Streams captures a time-ordered sequence of item-level modifications in a DynamoDB table. Lambda polls the stream and invokes your function synchronously with a batch of stream records. You create an event source mapping to connect the stream to your function.
  name: dynamodb/stream
  operation: subscribe
  operation_id: onDynamoDBStreamRecord
  summary: Receive DynamoDB Streams records
- description: Amazon Kinesis Data Streams captures real-time data at scale. Lambda polls the Kinesis stream and invokes your function with a batch of records from one or more shards. You create an event source mapping to connect the stream to your function.
  name: kinesis/stream
  operation: subscribe
  operation_id: onKinesisRecord
  summary: Receive Kinesis Data Streams records
- description: Amazon SQS queues messages for asynchronous processing. Lambda polls the queue and invokes your function with a batch of messages. When the function successfully processes a batch, Lambda deletes the messages from the queue. Supports both standard and FIFO queues.
  name: sqs/message
  operation: subscribe
  operation_id: onSQSMessage
  summary: Receive SQS queue messages
- description: Amazon SNS delivers notifications to Lambda functions subscribed to an SNS topic. When a message is published to the topic, SNS invokes your function asynchronously with the message payload. Supports standard topics for fanout to multiple subscribers.
  name: sns/notification
  operation: subscribe
  operation_id: onSNSNotification
  summary: Receive SNS topic notifications
- description: Amazon API Gateway invokes Lambda functions in response to HTTP API requests. API Gateway passes the request details as an event to the function and returns the function response to the caller. Supports REST APIs (v1 payload format) and HTTP APIs (v2 payload format).
  name: apigateway/request
  operation: subscribe
  operation_id: onAPIGatewayRequest
  summary: Receive API Gateway HTTP requests
- description: Amazon EventBridge delivers events from AWS services, custom applications, and SaaS partners to Lambda functions. EventBridge rules match incoming events and route them to target functions. You create rules that match event patterns and specify the Lambda function as a target.
  name: eventbridge/event
  operation: subscribe
  operation_id: onEventBridgeEvent
  summary: Receive EventBridge events
- description: Amazon EventBridge Scheduler (formerly CloudWatch Events scheduled rules) invokes Lambda functions on a schedule. You define a schedule expression using a rate or cron expression, and EventBridge invokes the function at the specified intervals.
  name: cloudwatch/scheduledevent
  operation: subscribe
  operation_id: onScheduledEvent
  summary: Receive scheduled invocations
- description: Amazon Cognito invokes Lambda functions as triggers during user pool operations such as sign-up, authentication, and token generation. The function can modify the authentication flow, validate data, or add custom claims.
  name: cognito/trigger
  operation: subscribe
  operation_id: onCognitoTrigger
  summary: Receive Cognito user pool trigger events
- description: Amazon CloudWatch can invoke Lambda functions as alarm actions when a metric alarm changes state. The function receives details about the alarm state change.
  name: cloudwatch/alarm
  operation: subscribe
  operation_id: onCloudWatchAlarm
  summary: Receive CloudWatch alarm state changes
- description: Amazon CloudWatch Logs can invoke a Lambda function when a subscription filter matches log events. The log data is delivered as a batch of log events compressed with gzip and base64-encoded.
  name: cloudwatch/logs
  operation: subscribe
  operation_id: onCloudWatchLogsEvent
  summary: Receive CloudWatch Logs subscription filter events
description: AWS Lambda integrates with other AWS services to invoke functions in response to events. Lambda functions can be triggered by event sources including Amazon S3, Amazon DynamoDB Streams, Amazon Kinesis Data Streams, Amazon SQS, Amazon SNS, Amazon API Gateway, Amazon EventBridge, Amazon CloudWatch Events, Amazon Cognito, and many more. Event sources send event data as JSON payloads that Lambda passes to the function handler. Events are processed synchronously (push model), asynchronously (event model), or by Lambda polling a stream or queue (poll model).
layout: asyncapi
messages:
- description: Contains information about S3 bucket events including the bucket name, object key, size, eTag, and the event type that triggered the function. S3 events are delivered asynchronously.
  name: S3Event
  summary: S3 object event notification delivered to Lambda
  title: Amazon S3 Event
- description: Contains a batch of records from a DynamoDB stream. Each record includes the event type (INSERT, MODIFY, REMOVE), the new and old item images (depending on stream view type), and metadata about the change.
  name: DynamoDBStreamEvent
  summary: Batch of DynamoDB Streams records delivered to Lambda
  title: Amazon DynamoDB Stream Event
- description: Contains a batch of records from a Kinesis data stream. Each record includes base64-encoded data, a partition key, and a sequence number.
  name: KinesisEvent
  summary: Batch of Kinesis Data Streams records delivered to Lambda
  title: Amazon Kinesis Event
- description: Contains a batch of messages from an SQS queue. Each message includes the message body, message attributes, and metadata such as the message ID and receipt handle.
  name: SQSEvent
  summary: Batch of SQS messages delivered to Lambda
  title: Amazon SQS Event
- description: Contains one or more SNS notification records. Each record includes the SNS topic ARN, subject, message body, timestamp, and message attributes.
  name: SNSEvent
  summary: SNS notification delivered to Lambda
  title: Amazon SNS Event
- description: Contains the full HTTP request details from API Gateway REST API including method, path, headers, query parameters, path parameters, stage variables, request context, and the request body.
  name: APIGatewayProxyEvent
  summary: HTTP request from API Gateway REST API
  title: API Gateway REST API Proxy Event (v1)
- description: Contains the HTTP request details from API Gateway HTTP API in the v2 payload format, with a simplified structure compared to the v1 format. Includes request context with HTTP method, path, source IP, and user agent.
  name: APIGatewayV2ProxyEvent
  summary: HTTP request from API Gateway HTTP API
  title: API Gateway HTTP API Proxy Event (v2)
- description: Contains an event matched by an EventBridge rule. The event includes the source service, detail type, account, region, and the event detail containing the event-specific data.
  name: EventBridgeEvent
  summary: Event from EventBridge event bus
  title: Amazon EventBridge Event
- description: Represents a scheduled event trigger. Contains the schedule rule ARN, timestamp, and identifying information. The detail-type is Scheduled Event.
  name: ScheduledEvent
  summary: Scheduled invocation from EventBridge Scheduler
  title: Scheduled Event
- description: Contains details about a Cognito user pool trigger including the trigger source, user pool ID, user attributes, and request/response parameters specific to the trigger type.
  name: CognitoEvent
  summary: Cognito user pool trigger event
  title: Amazon Cognito User Pool Trigger Event
- description: Contains information about a CloudWatch alarm state change including the alarm name, state, reason, and metric details.
  name: CloudWatchAlarmEvent
  summary: CloudWatch alarm state change event
  title: Amazon CloudWatch Alarm Event
- description: Contains a base64-encoded, gzip-compressed batch of log events from a CloudWatch Logs subscription filter.
  name: CloudWatchLogsEvent
  summary: CloudWatch Logs subscription filter event
  title: Amazon CloudWatch Logs Event
name: AWS Lambda Event Triggers
provider_name: AWS Lambda
provider_slug: aws-lambda
servers:
- description: AWS Lambda service endpoint. Event sources deliver events to Lambda which invokes the configured function. The function receives the event payload as the first argument to the handler.
  name: lambdaRuntime
  protocol: https
  url: https://lambda.{region}.amazonaws.com
slug: aws-lambda-event-triggers-asyncapi
spec_file: asyncapi/aws-lambda-event-triggers-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/aws-lambda/refs/heads/main/asyncapi/aws-lambda-event-triggers-asyncapi.yml
tags:
- AsyncAPI
- Webhooks
- Events
version: '2015-03-31'
---

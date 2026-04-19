---
channels:
- description: HTTP/HTTPS notification delivery channel. When a message is published to a topic with HTTP/S subscribers, SNS sends an HTTP POST request to each confirmed subscriber endpoint containing the notification in JSON format. The endpoint must return a 2xx status code to acknowledge receipt. SNS includes headers such as x-amz-sns-message-type, x-amz-sns-message-id, and x-amz-sns-topic-arn.
  name: /sns/http-notification
  operation: subscribe
  operation_id: receiveHttpNotification
  summary: Receive SNS notification via HTTP/HTTPS
- description: Amazon SQS notification delivery channel. When a message is published to a topic with SQS subscribers, SNS delivers the notification as an SQS message to the subscribed queue. The SQS message body contains the SNS notification in JSON format unless raw message delivery is enabled, in which case only the published message body is delivered.
  name: /sns/sqs-notification
  operation: subscribe
  operation_id: receiveSqsNotification
  summary: Receive SNS notification via SQS
- description: AWS Lambda notification delivery channel. When a message is published to a topic with Lambda subscribers, SNS invokes the Lambda function asynchronously with an event containing an array of SNS records. Each record includes the notification message, subject, timestamp, message attributes, and topic ARN.
  name: /sns/lambda-notification
  operation: subscribe
  operation_id: receiveLambdaNotification
  summary: Receive SNS notification via Lambda invocation
- description: Email notification delivery channel. When a message is published to a topic with email subscribers, SNS delivers the message as an email. For the email protocol, the message body is sent as the email body with the optional Subject as the email subject line. For the email-json protocol, the full JSON notification object is sent as the email body.
  name: /sns/email-notification
  operation: subscribe
  operation_id: receiveEmailNotification
  summary: Receive SNS notification via email
- description: SMS notification delivery channel. When a message is published to a topic with SMS subscribers or directly to a phone number, SNS delivers the message as a text message. The SMS message contains only the published message text, truncated to fit SMS size limits.
  name: /sns/sms-notification
  operation: subscribe
  operation_id: receiveSmsNotification
  summary: Receive SNS notification via SMS
description: Amazon Simple Notification Service (SNS) delivers notifications to subscribed endpoints when messages are published to topics. This AsyncAPI specification describes the notification messages that SNS delivers to HTTP/HTTPS endpoints, Amazon SQS queues, AWS Lambda functions, email recipients, and SMS recipients. When a message is published to an SNS topic, the service fans out the message to all confirmed subscribers using the delivery format appropriate for each protocol. HTTP/S endpoints receive a JSON-formatted POST request containing the message along with metadata such as the topic ARN, message ID, timestamp, and a signature for verification.
layout: asyncapi
messages:
- description: When a message is published to a topic, SNS wraps it in a JSON notification envelope that includes the message, metadata, topic ARN, and a cryptographic signature for verification. This is the standard delivery format for HTTP/S, SQS, and email-json protocol subscribers.
  name: Notification
  summary: Standard notification message delivered to HTTP/S, SQS, and email-json subscribers
  title: SNS Notification Message
- description: When a new HTTP/S subscription is created, SNS sends a SubscriptionConfirmation message to the endpoint. The endpoint must visit the SubscribeURL to confirm the subscription. Until confirmed, no notification messages are delivered.
  name: SubscriptionConfirmation
  summary: Sent to HTTP/S endpoints when a new subscription is created
  title: Subscription Confirmation Message
- description: When a subscription is deleted, SNS sends an UnsubscribeConfirmation message to the endpoint. The endpoint can visit the SubscribeURL to re-subscribe if the unsubscribe was unintended.
  name: UnsubscribeConfirmation
  summary: Sent to HTTP/S endpoints when a subscription is deleted
  title: Unsubscribe Confirmation Message
- description: When SNS invokes a Lambda function, the event payload contains a Records array. Each record includes an EventSource of aws:sns, the EventVersion, the EventSubscriptionArn, and an Sns object with the full notification details including message, subject, timestamp, message attributes, and signing meta
  name: LambdaEvent
  summary: Event payload delivered to Lambda function subscribers
  title: SNS Lambda Invocation Event
- description: SMS messages contain only the published message text. The message is truncated to fit within SMS size limits (160 characters for GSM encoding, 70 characters for Unicode).
  name: SmsMessage
  summary: Text message delivered to SMS subscribers
  title: SNS SMS Message
name: Amazon SNS Notifications
provider_name: Amazon SNS
provider_slug: amazon-sns
servers:
- description: Amazon SNS regional endpoint. SNS delivers notifications from the region where the topic is created.
  name: snsRegional
  protocol: https
  url: https://sns.{region}.amazonaws.com
slug: amazon-sns-notifications-asyncapi
spec_file: asyncapi/amazon-sns-notifications-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/amazon-sns/refs/heads/main/asyncapi/amazon-sns-notifications-asyncapi.yml
tags:
- AWS
- Email
- Messaging
- Notifications
- Pub/Sub
- Push Notifications
- SMS
- AsyncAPI
- Webhooks
- Events
version: '2010-03-31'
---

---
description: ''
layout: schema
name: SubscriptionMember
properties_list:
- description: The subscription ARN
  name: SubscriptionArn
  type: string
- description: The subscription owner's AWS account ID
  name: Owner
  type: string
- description: The subscription protocol
  name: Protocol
  type: string
- description: The subscription endpoint
  name: Endpoint
  type: string
- description: The topic ARN that this subscription is associated with
  name: TopicArn
  type: string
provider_name: Amazon SNS
provider_slug: amazon-sns
schema_file: json-schema/amazon-sns-subscription-member-schema.json
slug: amazon-sns-subscription-member
tags:
- AWS
- Email
- Messaging
- Notifications
- Pub/Sub
- Push Notifications
- SMS
title: SubscriptionMember
---

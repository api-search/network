---
description: Represents a subscriber for Amazon Security Lake data.
layout: schema
name: Subscriber
properties_list:
- description: The unique identifier for the subscriber.
  name: subscriberId
  type: string
- description: The ARN of the subscriber.
  name: subscriberArn
  type: string
- description: The name of the subscriber.
  name: subscriberName
  type: string
- description: A description of the subscriber.
  name: subscriberDescription
  type: string
- description: The status of the subscriber.
  name: subscriberStatus
  type: string
- description: The access types granted to the subscriber.
  name: accessTypes
  type: array
- description: The ARN of the resource share for AWS RAM-based access.
  name: resourceShareArn
  type: string
- description: Timestamp when the subscriber was created.
  name: createdAt
  type: string
- description: Timestamp when the subscriber was last updated.
  name: updatedAt
  type: string
provider_name: Amazon Security Lake
provider_slug: amazon-security-lake
schema_file: json-schema/amazon-security-lake-subscriber-schema.json
slug: amazon-security-lake-subscriber
tags:
- AWS
- Data Lake
- Security
- SIEM
- Threat Detection
title: Subscriber
---

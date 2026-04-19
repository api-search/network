---
description: ''
layout: schema
name: MessageAttributeValue
properties_list:
- description: The data type of the attribute. Supported types are String, String.Array, Number, and Binary.
  name: DataType
  type: string
- description: The string value of the attribute
  name: StringValue
  type: string
- description: The binary (base64-encoded) value of the attribute
  name: BinaryValue
  type: string
provider_name: Amazon SNS
provider_slug: amazon-sns
schema_file: json-schema/amazon-sns-message-attribute-value-schema.json
slug: amazon-sns-message-attribute-value
tags:
- AWS
- Email
- Messaging
- Notifications
- Pub/Sub
- Push Notifications
- SMS
title: MessageAttributeValue
---

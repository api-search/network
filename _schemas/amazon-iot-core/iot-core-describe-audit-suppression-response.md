---
description: DescribeAuditSuppressionResponse schema
layout: schema
name: DescribeAuditSuppressionResponse
properties_list:
- description: An audit check name. Checks must be enabled for your account. (Use <code>DescribeAccountAuditConfiguration</code> to see the list of all checks, including those that are enabled or use <code>UpdateAcc
  name: checkName
  type: string
- description: Information that identifies the noncompliant resource.
  name: resourceIdentifier
  type: object
- description: ''
  name: expirationDate
  type: object
- description: ''
  name: suppressIndefinitely
  type: object
- description: ''
  name: description
  type: object
provider_name: Amazon IoT Core
provider_slug: amazon-iot-core
schema_file: json-schema/iot-core-describe-audit-suppression-response-schema.json
slug: iot-core-describe-audit-suppression-response
tags:
- AWS
- Device Management
- IoT
- MQTT
- Message Routing
title: DescribeAuditSuppressionResponse
---

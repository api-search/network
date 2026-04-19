---
description: <p>Defines where Network Firewall sends logs for the firewall for one log type. This is used in <a>LoggingConfiguration</a>. You can send each type of log to an Amazon S3 bucket, a CloudWatch log group, or a Kinesis Data Firehose delivery stream.</p> <p>Network Firewall generates logs for stateful rule groups. You can save alert and flow log types. The stateful rules engine records flow logs for all network traffic that it receives. It records alert logs for traffic that matches stateful rules that have the rule action set to <code>DROP</code> or <code>ALERT</code>. </p>
layout: schema
name: LogDestinationConfig
properties_list:
- description: ''
  name: LogType
  type: object
- description: ''
  name: LogDestinationType
  type: object
- description: ''
  name: LogDestination
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-log-destination-config-schema.json
slug: openapi-log-destination-config
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: LogDestinationConfig
---

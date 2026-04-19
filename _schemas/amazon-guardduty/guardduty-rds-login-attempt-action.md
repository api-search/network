---
description: Indicates that a login attempt was made to the potentially compromised database from a remote IP address.
layout: schema
name: RdsLoginAttemptAction
properties_list:
- description: ''
  name: RemoteIpDetails
  type: object
- description: ''
  name: LoginAttributes
  type: object
provider_name: Amazon GuardDuty
provider_slug: amazon-guardduty
schema_file: json-schema/guardduty-rds-login-attempt-action-schema.json
slug: guardduty-rds-login-attempt-action
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
title: RdsLoginAttemptAction
---

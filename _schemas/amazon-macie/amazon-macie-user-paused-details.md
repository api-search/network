---
description: Provides information about when a classification job was paused. For a one-time job, this object also specifies when the job will expire and be cancelled if it isn't resumed. For a recurring job, this object also specifies when the paused job run will expire and be cancelled if it isn't resumed. This object is present only if a job's current status (jobStatus) is USER_PAUSED. The information in this object applies only to a job that was paused while it had a status of RUNNING.
layout: schema
name: UserPausedDetails
properties_list:
- description: ''
  name: jobExpiresAt
  type: object
- description: ''
  name: jobImminentExpirationHealthEventArn
  type: object
- description: ''
  name: jobPausedAt
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-user-paused-details-schema.json
slug: amazon-macie-user-paused-details
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: UserPausedDetails
---

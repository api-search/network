---
description: Configuration for failed invocation destinations. Specify an SQS queue or SNS topic to receive records of failed asynchronous invocations or event source mapping batches.
layout: schema
name: DestinationConfig
properties_list:
- description: ''
  name: OnSuccess
  type: object
- description: ''
  name: OnFailure
  type: object
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-destination-config-schema.json
slug: aws-lambda-destination-config
tags: []
title: DestinationConfig
---

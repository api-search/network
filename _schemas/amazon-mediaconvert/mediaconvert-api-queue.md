---
description: You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don't specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html.
layout: schema
name: Queue
properties_list:
- description: ''
  name: Arn
  type: object
- description: ''
  name: CreatedAt
  type: object
- description: ''
  name: Description
  type: object
- description: ''
  name: LastUpdated
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: PricingPlan
  type: object
- description: ''
  name: ProgressingJobsCount
  type: object
- description: ''
  name: ReservationPlan
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: SubmittedJobsCount
  type: object
- description: ''
  name: Type
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-queue-schema.json
slug: mediaconvert-api-queue
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Queue
---

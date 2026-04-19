---
description: <p>Elastic Transcoder returns a warning if the resources used by your pipeline are not in the same region as the pipeline.</p> <p>Using resources in the same region, such as your Amazon S3 buckets, Amazon SNS notification topics, and AWS KMS key, reduces processing time and prevents cross-regional charges.</p>
layout: schema
name: Warning
properties_list:
- description: ''
  name: Code
  type: object
- description: ''
  name: Message
  type: object
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
schema_file: json-schema/amazon-elastic-transcoder-warning-schema.json
slug: amazon-elastic-transcoder-warning
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
title: Warning
---

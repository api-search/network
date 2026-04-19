---
description: <p>The Amazon Simple Notification Service (Amazon SNS) topic or topics to notify in order to report job status.</p> <important> <p>To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.</p> </important>
layout: schema
name: Notifications
properties_list:
- description: ''
  name: Progressing
  type: object
- description: ''
  name: Completed
  type: object
- description: ''
  name: Warning
  type: object
- description: ''
  name: Error
  type: object
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
schema_file: json-schema/amazon-elastic-transcoder-notifications-schema.json
slug: amazon-elastic-transcoder-notifications
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
title: Notifications
---

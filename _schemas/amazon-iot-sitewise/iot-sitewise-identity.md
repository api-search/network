---
description: <p>Contains an identity that can access an IoT SiteWise Monitor resource.</p> <note> <p>Currently, you can't use Amazon Web Services APIs to retrieve IAM Identity Center identity IDs. You can find the IAM Identity Center identity IDs in the URL of user and group pages in the <a href="https://console.aws.amazon.com/singlesignon">IAM Identity Center console</a>.</p> </note>
layout: schema
name: Identity
properties_list:
- description: ''
  name: user
  type: object
- description: ''
  name: group
  type: object
- description: ''
  name: iamUser
  type: object
- description: ''
  name: iamRole
  type: object
provider_name: Amazon IoT SiteWise
provider_slug: amazon-iot-sitewise
schema_file: json-schema/iot-sitewise-identity-schema.json
slug: iot-sitewise-identity
tags:
- AWS
- Asset Management
- Industrial IoT
- IoT
- Time Series Data
title: Identity
---

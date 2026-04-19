---
description: Each <code>S3Resource</code> object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional <code>KeyRange</code> value. The length of the range is defined at job creation, and has either an inclusive <code>BeginMarker</code>, an inclusive <code>EndMarker</code>, or both. Ranges are UTF-8 binary sorted.
layout: schema
name: S3Resource
properties_list:
- description: ''
  name: BucketArn
  type: object
- description: ''
  name: KeyRange
  type: object
- description: ''
  name: TargetOnDeviceServices
  type: object
provider_name: Amazon Snow Family
provider_slug: amazon-snow-family
schema_file: json-schema/amazon-snow-family-s3-resource-schema.json
slug: amazon-snow-family-s3-resource
tags:
- AWS
- Data Migration
- Edge Computing
- Offline Transfer
- Physical Appliance
title: S3Resource
---

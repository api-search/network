---
description: Contains an array of Amazon Web Services resource objects. Each object represents an Amazon S3 bucket, an Lambda function, or an Amazon Machine Image (AMI) based on Amazon EC2 that is associated with a particular job.
layout: schema
name: JobResource
properties_list:
- description: ''
  name: S3Resources
  type: object
- description: ''
  name: LambdaResources
  type: object
- description: ''
  name: Ec2AmiResources
  type: object
provider_name: Amazon Snow Family
provider_slug: amazon-snow-family
schema_file: json-schema/amazon-snow-family-job-resource-schema.json
slug: amazon-snow-family-job-resource
tags:
- AWS
- Data Migration
- Edge Computing
- Offline Transfer
- Physical Appliance
title: JobResource
---

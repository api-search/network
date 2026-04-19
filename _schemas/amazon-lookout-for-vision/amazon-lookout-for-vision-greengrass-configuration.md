---
description: <p>Configuration information for the AWS IoT Greengrass component created in a model packaging job. For more information, see <a>StartModelPackagingJob</a>. </p> <note> <p>You can't specify a component with the same <code>ComponentName</code> and <code>Componentversion</code> as an existing component with the same component name and component version.</p> </note>
layout: schema
name: GreengrassConfiguration
properties_list:
- description: ''
  name: CompilerOptions
  type: object
- description: ''
  name: TargetDevice
  type: object
- description: ''
  name: TargetPlatform
  type: object
- description: ''
  name: S3OutputLocation
  type: object
- description: ''
  name: ComponentName
  type: object
- description: ''
  name: ComponentVersion
  type: object
- description: ''
  name: ComponentDescription
  type: object
- description: ''
  name: Tags
  type: object
provider_name: Amazon Lookout for Vision
provider_slug: amazon-lookout-for-vision
schema_file: json-schema/amazon-lookout-for-vision-greengrass-configuration-schema.json
slug: amazon-lookout-for-vision-greengrass-configuration
tags:
- AWS
- Computer Vision
- Machine Learning
- Manufacturing
- Quality Inspection
- Anomaly Detection
title: GreengrassConfiguration
---

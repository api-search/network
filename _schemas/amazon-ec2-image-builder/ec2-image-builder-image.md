---
description: An Image Builder image. You must specify exactly one recipe for the image – either a container recipe (<code>containerRecipe</code>), which creates a container image, or an image recipe (<code>imageRecipe</code>), which creates an AMI.
layout: schema
name: Image
properties_list:
- description: ''
  name: arn
  type: object
- description: ''
  name: type
  type: object
- description: ''
  name: name
  type: object
- description: ''
  name: version
  type: object
- description: ''
  name: platform
  type: object
- description: ''
  name: enhancedImageMetadataEnabled
  type: object
- description: ''
  name: osVersion
  type: object
- description: ''
  name: state
  type: object
- description: ''
  name: imageRecipe
  type: object
- description: ''
  name: containerRecipe
  type: object
- description: ''
  name: sourcePipelineName
  type: object
- description: ''
  name: sourcePipelineArn
  type: object
- description: ''
  name: infrastructureConfiguration
  type: object
- description: ''
  name: distributionConfiguration
  type: object
- description: ''
  name: imageTestsConfiguration
  type: object
- description: ''
  name: dateCreated
  type: object
- description: ''
  name: outputResources
  type: object
- description: ''
  name: tags
  type: object
- description: ''
  name: buildType
  type: object
- description: ''
  name: imageSource
  type: object
- description: ''
  name: scanState
  type: object
- description: ''
  name: imageScanningConfiguration
  type: object
provider_name: Amazon EC2 Image Builder
provider_slug: amazon-ec2-image-builder
schema_file: json-schema/ec2-image-builder-image-schema.json
slug: ec2-image-builder-image
tags:
- Amazon Web Services
- Automation
- AWS
- Container Images
- EC2
- Image Building
- Virtual Machine Images
title: Image
---

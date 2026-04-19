---
description: Request body for publishing a layer version
layout: schema
name: PublishLayerVersionRequest
properties_list:
- description: Description of the layer version
  name: Description
  type: string
- description: The function layer archive
  name: Content
  type: object
- description: A list of compatible runtimes. Used for filtering with ListLayers and ListLayerVersions.
  name: CompatibleRuntimes
  type: array
- description: The layer's software license (SPDX identifier, URL, or text)
  name: LicenseInfo
  type: string
- description: A list of compatible instruction set architectures
  name: CompatibleArchitectures
  type: array
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-publish-layer-version-request-schema.json
slug: aws-lambda-publish-layer-version-request
tags: []
title: PublishLayerVersionRequest
---

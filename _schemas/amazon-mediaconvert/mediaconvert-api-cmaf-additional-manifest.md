---
description: Specify the details for each pair of HLS and DASH additional manifests that you want the service to generate for this CMAF output group. Each pair of manifests can reference a different subset of outputs in the group.
layout: schema
name: CmafAdditionalManifest
properties_list:
- description: ''
  name: ManifestNameModifier
  type: object
- description: ''
  name: SelectedOutputs
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-cmaf-additional-manifest-schema.json
slug: mediaconvert-api-cmaf-additional-manifest
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: CmafAdditionalManifest
---

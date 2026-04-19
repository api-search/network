---
description: Use Allowed renditions to specify a list of possible resolutions in your ABR stack. * MediaConvert will create an ABR stack exclusively from the list of resolutions that you specify. * Some resolutions in the Allowed renditions list may not be included, however you can force a resolution to be included by setting Required to ENABLED. * You must specify at least one resolution that is greater than or equal to any resolutions that you specify in Min top rendition size or Min bottom rendition size. * If you specify Allowed renditions, you must not specify a separate rule for Force include renditions.
layout: schema
name: AllowedRenditionSize
properties_list:
- description: ''
  name: Height
  type: object
- description: ''
  name: Required
  type: object
- description: ''
  name: Width
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-allowed-rendition-size-schema.json
slug: mediaconvert-api-allowed-rendition-size
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: AllowedRenditionSize
---

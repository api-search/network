---
description: <p>The <code>segmentation_descriptor</code> message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the <code>EXT-X-DATERANGE</code> or <code>EventStream</code> ad marker's SCTE-35 data.</p> <p> <code>segmentation_descriptor</code> messages must be sent with the <code>time_signal</code> message type.</p> <p>See the <code>segmentation_descriptor()</code> table of the 2022 SCTE-35 specification for more information.</p>
layout: schema
name: SegmentationDescriptor
properties_list:
- description: ''
  name: SegmentNum
  type: object
- description: ''
  name: SegmentationEventId
  type: object
- description: ''
  name: SegmentationTypeId
  type: object
- description: ''
  name: SegmentationUpid
  type: object
- description: ''
  name: SegmentationUpidType
  type: object
- description: ''
  name: SegmentsExpected
  type: object
- description: ''
  name: SubSegmentNum
  type: object
- description: ''
  name: SubSegmentsExpected
  type: object
provider_name: Amazon MediaTailor
provider_slug: amazon-mediatailor
schema_file: json-schema/mediatailor-api-segmentation-descriptor-schema.json
slug: mediatailor-api-segmentation-descriptor
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: SegmentationDescriptor
---

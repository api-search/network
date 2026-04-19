---
description: Inserts segmentation markers at each segmentation_time period. rai_segstart sets the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format.
layout: schema
name: M2tsSegmentationMarkers
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-m2ts-segmentation-markers-schema.json
slug: mediaconvert-api-m2ts-segmentation-markers
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: M2tsSegmentationMarkers
---

---
description: <p>For HLS, when set to <code>true</code>, MediaTailor passes through <code>EXT-X-CUE-IN</code>, <code>EXT-X-CUE-OUT</code>, and <code>EXT-X-SPLICEPOINT-SCTE35</code> ad markers from the origin manifest to the MediaTailor personalized manifest.</p> <p>No logic is applied to these ad markers. For example, if <code>EXT-X-CUE-OUT</code> has a value of <code>60</code>, but no ads are filled for that ad break, MediaTailor will not set the value to <code>0</code>.</p>
layout: schema
name: AdMarkerPassthrough
properties_list:
- description: ''
  name: Enabled
  type: object
provider_name: Amazon MediaTailor
provider_slug: amazon-mediatailor
schema_file: json-schema/mediatailor-api-ad-marker-passthrough-schema.json
slug: mediatailor-api-ad-marker-passthrough
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: AdMarkerPassthrough
---

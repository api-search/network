---
description: 'Specify how MediaConvert handles the display definition segment (DDS). To exclude the DDS from this set of captions: Keep the default, None. To include the DDS: Choose Specified. When you do, also specify the offset coordinates of the display window with DDS x-coordinate and DDS y-coordinate. To include the DDS, but not include display window data: Choose No display window. When you do, you can write position metadata to the page composition segment (PCS) with DDS x-coordinate and DDS y-coordinate. For video resolutions with a height of 576 pixels or less, MediaConvert doesn''t include the DDS, regardless of the value you choose for DDS handling. All burn-in and DVB-Sub font settings must match.'
layout: schema
name: DvbddsHandling
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-dvbdds-handling-schema.json
slug: mediaconvert-api-dvbdds-handling
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DvbddsHandling
---

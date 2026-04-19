---
description: Optional. Configuration for a destination queue to which the job can hop once a customer-defined minimum wait time has passed.
layout: schema
name: HopDestination
properties_list:
- description: ''
  name: Priority
  type: object
- description: ''
  name: Queue
  type: object
- description: ''
  name: WaitMinutes
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-hop-destination-schema.json
slug: mediaconvert-api-hop-destination
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: HopDestination
---

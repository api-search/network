---
description: Corresponds to SCTE-35 delivery_not_restricted_flag parameter. To declare delivery restrictions, include this element and its four "restriction" flags. To declare that there are no restrictions, omit this element.
layout: schema
name: Scte35DeliveryRestrictions
properties_list:
- description: ''
  name: ArchiveAllowedFlag
  type: object
- description: ''
  name: DeviceRestrictions
  type: object
- description: ''
  name: NoRegionalBlackoutFlag
  type: object
- description: ''
  name: WebDeliveryAllowedFlag
  type: object
provider_name: Amazon MediaLive
provider_slug: amazon-medialive
schema_file: json-schema/medialive-api-scte35-delivery-restrictions-schema.json
slug: medialive-api-scte35-delivery-restrictions
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: Scte35DeliveryRestrictions
---

---
description: Options for configuring max VNIC attachments on a flexible shape
layout: schema
name: ShapeMaxVnicAttachmentOptions
properties_list:
- description: The minimum number of VNIC attachments
  name: min
  type: integer
- description: The maximum number of VNIC attachments
  name: max
  type: number
- description: The default number of VNIC attachments per OCPU
  name: defaultPerOcpu
  type: number
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-shape-max-vnic-attachment-options-schema.json
slug: oci-compute-shape-max-vnic-attachment-options
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: ShapeMaxVnicAttachmentOptions
---

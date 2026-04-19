---
description: Inspection data for a single part.
layout: schema
name: PartData
properties_list:
- description: Identifier for a grouping of parts.
  name: grp_ident
  type: string
- description: Identifier for a unique part, sucha as a serial number.
  name: row_ident
  type: string
- description: Date & time that data for this part was last updated.
  name: updated_on
  type: string
- description: List of measurements recorded for part. Order of entries corresponds to order of specifications, so index of a measurement corresponds to the index of the feature specification & place it is for.
  name: measurements
  type: array
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-part-data-schema.json
slug: 1factory-part-data
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: PartData
---

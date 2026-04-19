---
description: Specification that defines feature to be measured.
layout: schema
name: Specification
properties_list:
- description: Balloon number for feature.
  name: bln_no
  type: string
- description: Sheet and zone of the specification
  name: sheet_zone
  type: string
- description: Place number - for features that have multiple places, feature specification is repeated for each place.
  name: place
  type: integer
- description: Characteristic being measured, or, in the case of a note, the text of the note.
  name: characteristic
  type: string
- description: Type of characteristic being measured.
  name: characteristic_type
  type: string
- description: Dimension type for this specification - Standard, Manufacturing or Deviation.
  name: dimension_type
  type: string
- description: Balloon number of specification that this feature references, for example a manufacturing dimension referencing the actual drawing dimension it corresponds to.
  name: referenced_feature
  type: string
- description: How the data for this specification is recorded - numerically, as a pass/fail, or calculated from other features.
  name: data_type
  type: string
- description: Nominal value for this specification.
  name: nominal
  type: number
- description: Lower specification limit for the feature.
  name: lower_spec_limit
  type: number
- description: Upper specification limit for the feature.
  name: upper_spec_limit
  type: number
- description: Unit of measure for this feature.
  name: unit
  type: string
- description: Descriptor of feature. For GD&T, this is used to record the datum.
  name: descriptor_datum
  type: string
- description: For GD&T features, defines the material condition for evaluating bonus tolerance, if applicable.
  name: bonus_tolerance
  type: string
- description: Optional label to add more information to the specification.
  name: label
  type: string
- description: How the feature should be inspected.
  name: inspection_method
  type: string
- description: How frequently should the feature be checked.
  name: sampling_rule
  type: string
- description: Manufacturing operation for the feature.
  name: operation
  type: string
- description: Indicates if feature is key for quality.
  name: is_key
  type: boolean
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-specification-schema.json
slug: 1factory-specification
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: Specification
---

---
description: MinimumRiskLevel schema from ATSDR API
layout: schema
name: MinimumRiskLevel
properties_list:
- description: Name of the hazardous substance.
  name: substance_name
  type: string
- description: CAS registry number.
  name: cas_number
  type: string
- description: Exposure route.
  name: route
  type: string
- description: Duration of exposure.
  name: duration
  type: string
- description: MRL value (units depend on route).
  name: mrl_value
  type: number
- description: Unit of measurement for the MRL value.
  name: mrl_unit
  type: string
- description: Year the MRL was last updated.
  name: year_updated
  type: integer
provider_name: Agency for Toxic Substances and Disease Registry
provider_slug: agency-for-toxic-substances-and-disease-registry
schema_file: json-schema/atsdr-toxic-substance-profiles-minimum-risk-level-schema.json
slug: atsdr-toxic-substance-profiles-minimum-risk-level
tags:
- Diseases
- Federal Government
- Public Health
- Toxic Substances
- Environmental Health
- Hazardous Materials
title: MinimumRiskLevel
---

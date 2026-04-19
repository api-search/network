---
description: SubstancePriority schema from ATSDR API
layout: schema
name: SubstancePriority
properties_list:
- description: Priority rank on the ATSDR Substance Priority List.
  name: rank
  type: integer
- description: Name of the substance.
  name: substance_name
  type: string
- description: CAS registry number.
  name: cas_number
  type: string
- description: Composite score used for ranking.
  name: total_score
  type: number
- description: Number of NPL sites where substance was found.
  name: npl_frequency
  type: integer
- description: Toxicity component of the score.
  name: toxicity_score
  type: number
- description: Priority list year.
  name: year
  type: integer
provider_name: Agency for Toxic Substances and Disease Registry
provider_slug: agency-for-toxic-substances-and-disease-registry
schema_file: json-schema/atsdr-toxic-substance-profiles-substance-priority-schema.json
slug: atsdr-toxic-substance-profiles-substance-priority
tags:
- Diseases
- Federal Government
- Public Health
- Toxic Substances
- Environmental Health
- Hazardous Materials
title: SubstancePriority
---

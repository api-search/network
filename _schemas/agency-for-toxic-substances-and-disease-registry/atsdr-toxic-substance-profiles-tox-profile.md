---
description: ToxProfile schema from ATSDR API
layout: schema
name: ToxProfile
properties_list:
- description: Name of the hazardous substance.
  name: substance_name
  type: string
- description: Chemical Abstracts Service registry number.
  name: cas_number
  type: string
- description: Year the toxicological profile was published or updated.
  name: profile_year
  type: integer
- description: Rank on the ATSDR Substance Priority List.
  name: substance_priority_list_rank
  type: integer
- description: Summary of known health effects from exposure.
  name: health_effects
  type: string
- description: Most common route of exposure (ingestion, inhalation, dermal).
  name: primary_route_of_exposure
  type: string
- description: URL to the full toxicological profile PDF.
  name: profile_url
  type: string
provider_name: Agency for Toxic Substances and Disease Registry
provider_slug: agency-for-toxic-substances-and-disease-registry
schema_file: json-schema/atsdr-toxic-substance-profiles-tox-profile-schema.json
slug: atsdr-toxic-substance-profiles-tox-profile
tags:
- Diseases
- Federal Government
- Public Health
- Toxic Substances
- Environmental Health
- Hazardous Materials
title: ToxProfile
---

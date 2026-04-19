---
description: ExposureInvestigation schema from ATSDR API
layout: schema
name: ExposureInvestigation
properties_list:
- description: Name of the contaminated site.
  name: site_name
  type: string
- description: US state abbreviation.
  name: state
  type: string
- description: County name.
  name: county
  type: string
- description: Year of the investigation.
  name: year
  type: integer
- description: Type of investigation (Health Consultation, Public Health Assessment, etc.).
  name: investigation_type
  type: string
- description: Primary hazardous substance involved.
  name: primary_contaminant
  type: string
- description: Investigation status.
  name: status
  type: string
provider_name: Agency for Toxic Substances and Disease Registry
provider_slug: agency-for-toxic-substances-and-disease-registry
schema_file: json-schema/atsdr-toxic-substance-profiles-exposure-investigation-schema.json
slug: atsdr-toxic-substance-profiles-exposure-investigation
tags:
- Diseases
- Federal Government
- Public Health
- Toxic Substances
- Environmental Health
- Hazardous Materials
title: ExposureInvestigation
---

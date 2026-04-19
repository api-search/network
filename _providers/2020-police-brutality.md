---
api_count: 1
apis:
- description: This repository accumulates and contextualizes evidence of police brutality during the 2020 George Floyd protests. Data is available as JSON and CSV files from the data_build branch, including geoloca
  name: 2020 Police Brutality API
  slug: 2020-police-brutality
capabilities:
- description: 'Workflow for accessing and analyzing documented police brutality incidents from the 2020 George Floyd protests. Designed for journalists, researchers, prosecutors, and activists who need programmatic '
  name: 2020 Police Brutality Incident Research
  slug: 2020-police-brutality-incident-research
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/2020PB
- title: ''
  type: GitHubRepository
  url: https://github.com/2020PB/police-brutality
- title: ''
  type: Documentation
  url: https://github.com/2020PB/police-brutality/blob/main/README.md
- title: ''
  type: SpectralRules
  url: rules/2020-police-brutality-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/2020-police-brutality-incident-research.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/2020-police-brutality-vocabulary.yaml
created: '2024-11-13'
description: This repository accumulates and contextualizes evidence of police brutality during the 2020 George Floyd protests. The goal is to assist journalists, politicians, prosecutors, activists and concerned individuals who can use the evidence accumulated here for political campaigns, news reporting, public education and prosecution of criminal police officers.
features:
- description: Documented evidence of police brutality with descriptions, dates, locations, and source links
  name: Incident Documentation
- description: GPS geolocation coordinates for each incident, enabling geographic analysis
  name: Location Data
- description: Categorical tags classifying incident types (foam-bullet, tear-gas, pepper-spray, etc.)
  name: Tag Classification
- description: Data available in JSON (v1 and v2) and CSV formats for different use cases
  name: Multiple Data Formats
- description: Each incident includes links to source documentation for verification
  name: Source Verification
- description: MIT licensed open dataset available for public use
  name: Open Data
image: /assets/icons/2020-police-brutality.png
integrations: []
jsonld:
- class_count: 5
  name: 2020 Police Brutality Context
  property_count: 11
  slug: 2020-police-brutality-context
layout: provider
modified: '2026-04-19'
name: 2020 Police Brutality
rules:
- name: 2020 Police Brutality API Rules
  rule_count: 19
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 7
  slug: 2020-police-brutality-spectral-rules
skills: []
slug: 2020-police-brutality
solutions: []
tags:
- Brutality
- Civil Rights
- Policing
- Public Data
url: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/apis.yml
use_cases:
- description: Investigative journalists use incident data for news reporting on police conduct
  name: Journalism and Reporting
- description: Prosecutors and civil rights attorneys use evidence for criminal and civil cases
  name: Legal Proceedings
- description: Researchers study patterns in police use of force during protests
  name: Academic Research
- description: Activists and policymakers use data to support police reform campaigns
  name: Policy Advocacy
- description: Organizations use the data to educate the public about police brutality
  name: Public Education
- description: Researchers map incidents by location to identify geographic patterns
  name: Geographic Analysis
---

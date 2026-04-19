---
class_count: 16
classes:
- Flag
- Segment
- CreateExperimentRequest
- Experiment
- UpdateExperimentRequest
- VersionListResponse
- ExperimentListResponse
- DeploymentListResponse
- VariantConfig
- FlagListResponse
- CreateFlagRequest
- Deployment
- UpdateFlagRequest
- name
- description
- version
context_file: json-ld/amplitude-experiment-management-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/json-ld/amplitude-experiment-management-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amplitude Experiment Management Api from Amplitude.
layout: jsonld
name: Amplitude Experiment Management Api Context
namespaces:
- prefix: amplitude
  uri: https://amplitude.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: projectId
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: evaluationMode
  type: string
- container: ''
  name: bucketingKey
  type: string
- container: ''
  name: bucketingSalt
  type: string
- container: set
  name: variants
  type: reference
- container: ''
  name: payload
  type: string
- container: ''
  name: rolloutWeight
  type: integer
- container: set
  name: deployments
  type: string
- container: set
  name: segments
  type: reference
- container: set
  name: conditions
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: prop
  type: string
- container: ''
  name: op
  type: string
- container: set
  name: values
  type: string
- container: ''
  name: variant
  type: string
- container: ''
  name: percentage
  type: integer
- container: ''
  name: state
  type: string
- container: ''
  name: rolledOutVariant
  type: string
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: endDate
  type: dateTime
- container: set
  name: versions
  type: reference
- container: ''
  name: flagId
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: createdBy
  type: string
- container: ''
  name: nextCursor
  type: string
- container: set
  name: experiments
  type: reference
- container: ''
  name: label
  type: string
- container: ''
  name: deleted
  type: boolean
- container: set
  name: flags
  type: reference
property_count: 32
provider_name: Amplitude
provider_slug: amplitude
slug: amplitude-experiment-management-api-context
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
- JSON-LD
- Linked Data
- Semantic Web
---

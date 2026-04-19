---
class_count: 46
classes:
- LandingZoneSummary
- GetLandingZoneResponse
- GetControlOperationResponse
- Baseline
- ResetEnabledBaselineResponse
- EnabledControlParameter
- BaselineOperation
- EnableControlResponse
- CreateLandingZoneRequest
- EnabledBaselineSummary
- LandingZone
- ControlOperation
- DisableBaselineResponse
- ResetEnabledControlResponse
- ControlOperationSummary
- EnabledBaselineParameter
- GetEnabledControlResponse
- DeleteLandingZoneResponse
- CreateLandingZoneResponse
- UpdateEnabledControlResponse
- ListLandingZonesResponse
- ResetLandingZoneResponse
- GetEnabledBaselineResponse
- EnabledControl
- UpdateEnabledBaselineResponse
- ListLandingZoneOperationsResponse
- LandingZoneOperationSummary
- ListBaselinesResponse
- ListEnabledControlsResponse
- UpdateLandingZoneResponse
- EnabledBaseline
- UpdateLandingZoneRequest
- EnableBaselineRequest
- GetLandingZoneOperationResponse
- ListEnabledBaselinesResponse
- DisableControlResponse
- EnabledControlSummary
- EnableBaselineResponse
- LandingZoneOperationDetail
- ListControlOperationsResponse
- GetBaselineOperationResponse
- EnableControlRequest
- GetBaselineResponse
- description
- name
- version
context_file: json-ld/amazon-control-tower-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/json-ld/amazon-control-tower-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Control Tower from Amazon Control Tower.
layout: jsonld
name: Amazon Control Tower Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/controltower/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: arn
  type: string
- container: ''
  name: baselineIdentifier
  type: string
- container: ''
  name: baselineOperation
  type: string
- container: ''
  name: baselineVersion
  type: string
- container: set
  name: baselines
  type: string
- container: ''
  name: controlIdentifier
  type: string
- container: ''
  name: controlOperation
  type: string
- container: set
  name: controlOperations
  type: string
- container: ''
  name: driftStatus
  type: reference
- container: ''
  name: driftStatusSummary
  type: reference
- container: ''
  name: enabledBaselineDetails
  type: string
- container: set
  name: enabledBaselines
  type: string
- container: ''
  name: enabledControl
  type: string
- container: ''
  name: enabledControlIdentifier
  type: string
- container: set
  name: enabledControls
  type: string
- container: ''
  name: endTime
  type: dateTime
- container: ''
  name: key
  type: string
- container: ''
  name: landingZone
  type: string
- container: ''
  name: landingZoneIdentifier
  type: string
- container: set
  name: landingZoneOperations
  type: string
- container: set
  name: landingZones
  type: string
- container: ''
  name: lastOperationIdentifier
  type: string
- container: ''
  name: latestAvailableVersion
  type: string
- container: ''
  name: manifest
  type: reference
- container: ''
  name: nextToken
  type: string
- container: ''
  name: operationDetails
  type: string
- container: ''
  name: operationIdentifier
  type: string
- container: ''
  name: operationType
  type: string
- container: set
  name: parameters
  type: string
- container: ''
  name: startTime
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: statusMessage
  type: string
- container: ''
  name: statusSummary
  type: reference
- container: ''
  name: tags
  type: reference
- container: ''
  name: targetIdentifier
  type: string
- container: ''
  name: value
  type: string
property_count: 36
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
slug: amazon-control-tower-context
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
- JSON-LD
- Linked Data
- Semantic Web
---

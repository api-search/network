---
description: PolicyRecommendation schema from Palo Alto Networks IoT Security API
layout: schema
name: PolicyRecommendation
properties_list:
- description: Unique recommendation identifier.
  name: id
  type: string
- description: Device identifier the recommendation applies to.
  name: deviceid
  type: string
- description: Device profile the recommendation applies to.
  name: profile
  type: string
- description: Recommended source security zone.
  name: source_zone
  type: string
- description: Recommended destination security zone.
  name: destination_zone
  type: string
- description: Recommended allowed applications.
  name: applications
  type: array
- description: Recommended allowed services and ports.
  name: services
  type: array
- description: Recommended policy action.
  name: action
  type: string
- description: Confidence score for the recommendation.
  name: confidence
  type: number
- description: Human-readable recommendation description.
  name: description
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/iot-security-api-policy-recommendation-schema.json
slug: iot-security-api-policy-recommendation
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: PolicyRecommendation
---

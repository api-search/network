---
description: Contains Security Information Event Management (SIEM) integration settings.
layout: schema
name: siem-settings
properties_list:
- description: Whether you enabled SIEM for all the security policies in the configuration version.
  name: enableForAllPolicies
  type: boolean
- description: Whether you enabled SIEM in a security configuration version.
  name: enableSiem
  type: boolean
- description: __Deprecated__ Whether you enabled SIEM for the Bot Manager events. Use `exceptions` parameter instead to set botman siem events exception.
  name: enabledBotmanSiemEvents
  type: boolean
- description: Describes all attack type exceptions that will be ignored in siem events.
  name: exceptions
  type: array
- description: The list of security policy identifiers for which to enable the SIEM integration.
  name: firewallPolicyIds
  type: array
- description: Uniquely identifies the SIEM settings.
  name: siemDefinitionId
  type: integer
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-siem-settings-schema.json
slug: api-security-siem-settings
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: siem-settings
---

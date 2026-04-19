---
description: Contains information about a match target.
layout: schema
name: match-target
properties_list:
- description: Contains a list of objects containing an API endpoint ID and name. This field applies only to API match targets.
  name: apis
  type: array
- description: The list of network list identifiers and names.
  name: bypassNetworkLists
  type: array
- description: Uniquely identifies the security configuration.
  name: configId
  type: integer
- description: The version of security configuration.
  name: configVersion
  type: integer
- description: Describes the rule to match on paths. Either `NO_MATCH` to not match on the default file, `BASE_MATCH` to match only requests for top-level hostnames ending in a trailing slash, or `RECURSIVE_MATCH` t
  name: defaultFile
  type: string
- description: __Read-only__ Defines the security controls to apply. For a security control to be effectively turned on, it has to be enabled in both the match target and the security policy.
  name: effectiveSecurityControls
  type: object
- description: Contains a list of file extensions.
  name: fileExtensions
  type: array
- description: Contains a list of file paths.
  name: filePaths
  type: array
- description: Contains a list of hostnames to protect.
  name: hostnames
  type: array
- description: Describes whether the match target applies when a match is found in the specified `fileExtensions` or when a match isn't found.
  name: isNegativeFileExtensionMatch
  type: boolean
- description: Describes whether the match target applies when a match is found in the specified paths or when a match isn't found.
  name: isNegativePathMatch
  type: boolean
- description: The security policy associated with the match target.
  name: securityPolicy
  type: object
- description: The position in the sequence of match targets.
  name: sequence
  type: integer
- description: Uniquely identifies the match target.
  name: targetId
  type: integer
- description: Describes the type of match target, either `website` or `api`.
  name: type
  type: string
- description: __Read-only__ Describes warnings, errors, or notices determined by a validation of this resource.
  name: validations
  type: object
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-match-target-schema.json
slug: api-security-match-target
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: match-target
---

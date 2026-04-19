---
description: Contains details about a hostname coverage match target.
layout: schema
name: hostname-coverage-match-target
properties_list:
- description: The list of API endpoint identifiers and names. This applies only for `api` match targets.
  name: apis
  type: array
- description: The network lists' identifiers and names in the match target.
  name: bypassNetworkLists
  type: array
- description: Describes the rule to match on paths. Either `NO_MATCH` not to match on the default file, `BASE_MATCH` to match only requests for top-level hostnames ending in a trailing slash, or `RECURSIVE_MATCH` t
  name: defaultFile
  type: string
- description: __Read-only__ The security controls to apply. For a security control to be effectively turned on, you must enable it in both the match target and the security policy.
  name: effectiveSecurityControls
  type: object
- description: The list of file extensions to apply the match target to.
  name: fileExtensions
  type: array
- description: The list of file paths to apply the match target to.
  name: filePaths
  type: array
- description: The list of hostnames to protect.
  name: hostnames
  type: array
- description: Whether the match target applies when a match is found in the specified `fileExtensions` or when a match isn't found.
  name: isNegativeFileExtensionMatch
  type: boolean
- description: Whether the match target applies when a match is found in the specified `filePaths` or when a match isn't found.
  name: isNegativePathMatch
  type: boolean
- description: The security policy associated with the match target.
  name: securityPolicy
  type: object
- description: The match target's position in the sequence of match targets.
  name: sequence
  type: integer
- description: Uniquely identifies the match target.
  name: targetId
  type: integer
- description: The type of match target. Either `website` or `api`.
  name: type
  type: string
- description: __Read-only__ Contains details about warnings, errors, or notices determined by a validation of this resource.
  name: validations
  type: object
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-hostname-coverage-match-target-schema.json
slug: api-security-hostname-coverage-match-target
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: hostname-coverage-match-target
---

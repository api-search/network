---
class_count: 8
classes:
- AsmIncident
- AssetInternetExposure
- AttackSurfaceRule
- AuditLog
- ExposedService
- Filter
- OwnedIpRange
- SortOrder
context_file: json-ld/palo-alto-cortex-xpanse-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xpanse-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cortex Xpanse Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cortex Xpanse Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: actorEmail
  type: string
- container: ''
  name: actorPrimaryUsername
  type: string
- container: ''
  name: actorType
  type: string
- container: ''
  name: alertCount
  type: integer
- container: set
  name: asmIdList
  type: string
- container: ''
  name: assetName
  type: string
- container: ''
  name: assetType
  type: string
- container: ''
  name: assignedUserMail
  type: string
- container: ''
  name: assignedUserPrettyName
  type: string
- container: ''
  name: attackSurfaceRuleId
  type: string
- container: ''
  name: attackSurfaceRuleName
  type: string
- container: ''
  name: attributionReason
  type: string
- container: set
  name: businessUnits
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: cidr
  type: string
- container: ''
  name: cloudId
  type: string
- container: ''
  name: cloudProvider
  type: string
- container: ''
  name: created
  type: integer
- container: ''
  name: creationTime
  type: integer
- container: ''
  name: description
  type: string
- container: ''
  name: discoveryType
  type: string
- container: set
  name: domain
  type: string
- container: ''
  name: enabledStatus
  type: string
- container: set
  name: externallyDetectedProviders
  type: string
- container: ''
  name: field
  type: string
- container: ''
  name: firstIp
  type: string
- container: ''
  name: incidentId
  type: string
- container: ''
  name: incidentName
  type: string
- container: set
  name: incidentType
  type: string
- container: ''
  name: ip
  type: string
- container: set
  name: ipAddress
  type: string
- container: set
  name: ipv6Address
  type: string
- container: ''
  name: isActive
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: keyword
  type: string
- container: ''
  name: lastIp
  type: string
- container: ''
  name: lastObserved
  type: integer
- container: ''
  name: modificationTime
  type: integer
- container: ''
  name: modified
  type: integer
- container: ''
  name: operator
  type: string
- container: ''
  name: port
  type: integer
- container: ''
  name: protocol
  type: string
- container: set
  name: provider
  type: string
- container: ''
  name: rangeId
  type: string
- container: ''
  name: rangeSize
  type: integer
- container: ''
  name: reason
  type: string
- container: ''
  name: releaseStatus
  type: string
- container: ''
  name: remediationGuidance
  type: string
- container: ''
  name: resolveComment
  type: string
- container: ''
  name: resolvedBy
  type: string
- container: ''
  name: result
  type: string
- container: ''
  name: serviceId
  type: string
- container: ''
  name: serviceName
  type: string
- container: ''
  name: serviceType
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: subType
  type: string
- container: set
  name: tags
  type: reference
- container: ''
  name: timestamp
  type: integer
- container: ''
  name: value
  type: string
property_count: 60
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cortex-xpanse-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---

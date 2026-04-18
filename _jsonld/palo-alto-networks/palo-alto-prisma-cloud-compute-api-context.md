---
class_count: 12
classes:
- CIScan
- ComplianceIssue
- CompliancePolicy
- Container
- Defender
- DefenderSummary
- Host
- Image
- RegistryConfig
- RuntimePolicy
- Vulnerability
- VulnerabilityPolicy
context_file: json-ld/palo-alto-prisma-cloud-compute-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-cloud-compute-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Cloud Compute Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Cloud Compute Api Context
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
  name: Id
  type: string
- container: ''
  name: accountId
  type: string
- container: ''
  name: appEmbedded
  type: integer
- container: set
  name: blacklist
  type: string
- container: ''
  name: block
  type: boolean
- container: ''
  name: byType
  type: reference
- container: ''
  name: cap
  type: integer
- container: ''
  name: category
  type: string
- container: ''
  name: cause
  type: string
- container: set
  name: checks
  type: reference
- container: ''
  name: cloudMetadata
  type: reference
- container: ''
  name: cluster
  type: string
- container: set
  name: clusters
  type: string
- container: set
  name: collections
  type: string
- container: set
  name: complianceIssues
  type: reference
- container: ''
  name: complianceIssuesCount
  type: integer
- container: ''
  name: condition
  type: reference
- container: ''
  name: connected
  type: boolean
- container: ''
  name: count
  type: integer
- container: ''
  name: created
  type: dateTime
- container: ''
  name: credentialID
  type: string
- container: ''
  name: cri
  type: integer
- container: ''
  name: critical
  type: integer
- container: ''
  name: cves
  type: reference
- container: ''
  name: cvss
  type: float
- container: ''
  name: description
  type: string
- container: ''
  name: disconnected
  type: integer
- container: ''
  name: docker
  type: integer
- container: ''
  name: dockerWindows
  type: integer
- container: ''
  name: effect
  type: string
- container: ''
  name: entityInfo
  type: reference
- container: ''
  name: fargate
  type: integer
- container: ''
  name: filesystem
  type: reference
- container: ''
  name: fixedVersion
  type: string
- container: ''
  name: high
  type: integer
- container: ''
  name: hostname
  type: string
- container: ''
  name: id
  type: integer
- container: set
  name: ids
  type: string
- container: ''
  name: imageId
  type: string
- container: ''
  name: imageName
  type: string
- container: ''
  name: instanceId
  type: string
- container: ''
  name: kernelVersion
  type: string
- container: ''
  name: lastModified
  type: dateTime
- container: ''
  name: link
  type: string
- container: ''
  name: low
  type: integer
- container: ''
  name: medium
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: network
  type: reference
- container: ''
  name: os
  type: string
- container: ''
  name: osDistro
  type: string
- container: ''
  name: osDistroVersion
  type: string
- container: ''
  name: packageName
  type: string
- container: ''
  name: packageVersion
  type: string
- container: ''
  name: pass
  type: boolean
- container: ''
  name: processes
  type: reference
- container: ''
  name: provider
  type: string
- container: ''
  name: publishedDate
  type: dateTime
- container: ''
  name: region
  type: string
- container: ''
  name: registry
  type: string
- container: ''
  name: repo
  type: string
- container: set
  name: repoDigests
  type: string
- container: ''
  name: repoTag
  type: reference
- container: set
  name: rules
  type: reference
- container: ''
  name: scanTime
  type: dateTime
- container: ''
  name: scanners
  type: integer
- container: ''
  name: serverless
  type: integer
- container: set
  name: severities
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: tag
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: total
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: version
  type: string
- container: set
  name: versionDistribution
  type: reference
- container: set
  name: vulnerabilities
  type: reference
- container: ''
  name: vulnerabilitiesCount
  type: integer
- container: ''
  name: vulnerabilityDistribution
  type: reference
- container: set
  name: whitelist
  type: string
property_count: 81
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-cloud-compute-api-context
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

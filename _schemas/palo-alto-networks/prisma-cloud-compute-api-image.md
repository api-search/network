---
description: Image schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: Image
properties_list:
- description: Unique image identifier composed of registry, repository, and tag.
  name: _id
  type: string
- description: Hostname of the machine where the image was scanned.
  name: hostname
  type: string
- description: Timestamp of the most recent scan.
  name: scanTime
  type: string
- description: Repository and tag information for the image.
  name: repoTag
  type: object
- description: Content-addressable image digests.
  name: repoDigests
  type: array
- description: Operating system distribution of the image.
  name: osDistro
  type: string
- description: Operating system distribution version.
  name: osDistroVersion
  type: string
- description: Vulnerabilities discovered in the image.
  name: vulnerabilities
  type: array
- description: Total number of vulnerabilities found.
  name: vulnerabilitiesCount
  type: integer
- description: Vulnerability count by severity level.
  name: vulnerabilityDistribution
  type: object
- description: Compliance check failures for the image.
  name: complianceIssues
  type: array
- description: Total number of compliance issues found.
  name: complianceIssuesCount
  type: integer
- description: Kubernetes clusters where this image is deployed.
  name: clusters
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-image-schema.json
slug: prisma-cloud-compute-api-image
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Image
---

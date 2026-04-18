---
description: Container schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: Container
properties_list:
- description: Unique container identifier.
  name: _id
  type: string
- description: Container name.
  name: name
  type: string
- description: Host where the container is running.
  name: hostname
  type: string
- description: ID of the container image.
  name: imageId
  type: string
- description: Full image name including registry, repository, and tag.
  name: imageName
  type: string
- description: Current container state.
  name: state
  type: string
- description: Container creation timestamp.
  name: created
  type: string
- description: Kubernetes cluster name.
  name: cluster
  type: string
- description: Kubernetes namespace.
  name: namespace
  type: string
- description: Number of vulnerabilities in the container image.
  name: vulnerabilitiesCount
  type: integer
- description: Number of compliance issues for this container.
  name: complianceIssuesCount
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-container-schema.json
slug: prisma-cloud-compute-api-container
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Container
---

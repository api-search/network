---
description: Schema for a Red Hat advisory (erratum) representing a security fix, bug fix, or enhancement update applicable to registered RHEL systems through the Insights Patch service.
layout: schema
name: Red Hat Insights Advisory
properties_list:
- description: The advisory identifier in Red Hat format (e.g., RHSA-2024:1234, RHBA-2024:5678).
  name: id
  type: string
- description: The type of advisory indicating the nature of the update.
  name: type
  type: string
- description: A brief summary of the advisory content.
  name: synopsis
  type: string
- description: A detailed description of the advisory including affected components and changes.
  name: description
  type: string
- description: The severity rating for security advisories, null for non-security advisories.
  name: severity
  type:
  - string
  - 'null'
- description: The date and time the advisory was publicly released.
  name: public_date
  type: string
- description: The date and time the advisory was last modified.
  name: modified_date
  type: string
- description: The number of registered systems to which this advisory is applicable.
  name: applicable_systems
  type: integer
- description: The list of CVE identifiers addressed by this advisory.
  name: cves
  type: array
- description: The list of updated package names included in the advisory.
  name: packages
  type: array
- description: External references related to the advisory.
  name: references
  type: array
- description: Whether applying this advisory requires a system reboot.
  name: reboot_required
  type: boolean
- description: The RHEL release versions this advisory applies to.
  name: release_versions
  type: array
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-insights-advisory-schema.json
slug: red-hat-insights-advisory
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Red Hat Insights Advisory
---

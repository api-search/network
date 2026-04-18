---
description: AttackCategory schema from Palo Alto Networks Prisma AIRS AI Red Teaming API
layout: schema
name: AttackCategory
properties_list:
- description: Unique identifier for the attack category.
  name: category_id
  type: string
- description: Human-readable category name.
  name: name
  type: string
- description: Description of the vulnerability class this category tests.
  name: description
  type: string
- description: Number of built-in attack probes in this category.
  name: attack_count
  type: integer
- description: Severity range of vulnerabilities this category can discover.
  name: severity_range
  type: object
- description: Example attack type names within this category.
  name: examples
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-ai-red-teaming-api-attack-category-schema.json
slug: prisma-airs-ai-red-teaming-api-attack-category
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AttackCategory
---

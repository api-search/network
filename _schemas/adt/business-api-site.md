---
description: A business site with ADT security systems.
layout: schema
name: Site
properties_list:
- description: Unique identifier of the site.
  name: id
  type: string
- description: Name of the business site.
  name: name
  type: string
- description: Physical address.
  name: address
  type: string
- description: Current security status.
  name: status
  type: string
- description: Number of security systems at this site.
  name: systemCount
  type: integer
provider_name: ADT
provider_slug: adt
schema_file: json-schema/business-api-site-schema.json
slug: business-api-site
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: Site
---

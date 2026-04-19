---
description: Physical site or location used to geographically organize network devices within Aruba Central.
layout: schema
name: Site
properties_list:
- description: Unique identifier for the site.
  name: site_id
  type: integer
- description: Name of the site.
  name: site_name
  type: string
- description: Street address of the site.
  name: address
  type: string
- description: City where the site is located.
  name: city
  type: string
- description: State or province where the site is located.
  name: state
  type: string
- description: Country where the site is located.
  name: country
  type: string
- description: Postal code for the site location.
  name: zipcode
  type: string
- description: Geographic longitude coordinate.
  name: longitude
  type: number
- description: Geographic latitude coordinate.
  name: latitude
  type: number
- description: Tags applied to the site.
  name: tags
  type: array
- description: Number of devices associated with the site.
  name: associated_device_count
  type: integer
provider_name: Aruba
provider_slug: aruba
schema_file: json-schema/aruba-central-site-schema.json
slug: aruba-central-site
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
title: Site
---

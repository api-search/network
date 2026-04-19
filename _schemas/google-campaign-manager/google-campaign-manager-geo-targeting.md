---
description: Geographic targeting configuration.
layout: schema
name: GeoTargeting
properties_list:
- description: Countries to target.
  name: countries
  type: array
- description: Regions to target.
  name: regions
  type: array
- description: Cities to target.
  name: cities
  type: array
- description: Metros to target.
  name: metros
  type: array
- description: Postal codes to target.
  name: postalCodes
  type: array
- description: Whether to exclude the specified geographic locations.
  name: excludeCountries
  type: boolean
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-geo-targeting-schema.json
slug: google-campaign-manager-geo-targeting
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: GeoTargeting
---

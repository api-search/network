---
description: A single agricultural statistics data record from the QuickStats database.
layout: schema
name: Statistics Record
properties_list:
- description: Data source type (SURVEY or CENSUS).
  name: source_desc
  type: string
- description: High-level sector of the agricultural economy.
  name: sector_desc
  type: string
- description: Commodity group within the sector.
  name: group_desc
  type: string
- description: Name of the agricultural commodity.
  name: commodity_desc
  type: string
- description: Commodity class or subtype.
  name: class_desc
  type: string
- description: Statistical measurement category.
  name: statisticcat_desc
  type: string
- description: Unit of measurement for the value.
  name: unit_desc
  type: string
- description: Short description combining commodity and statistic.
  name: short_desc
  type: string
- description: Domain category (TOTAL, CHEMICAL, IRRIGATION, etc.).
  name: domain_desc
  type: string
- description: Geographic aggregation level.
  name: agg_level_desc
  type: string
- description: Two-letter state abbreviation.
  name: state_alpha
  type: string
- description: Full state name.
  name: state_name
  type: string
- description: County name (if county-level data).
  name: county_name
  type: string
- description: Survey or census year.
  name: year
  type: integer
- description: Data collection frequency.
  name: freq_desc
  type: string
- description: Reference time period (YEAR, JAN, JUN, etc.).
  name: reference_period_desc
  type: string
- description: Statistical value (may include formatting like commas; use as string).
  name: value
  type: string
- description: Coefficient of variation percentage (data reliability indicator).
  name: CV_pct
  type: string
provider_name: Agricultural Statistics Service
provider_slug: agricultural-statistics-service
schema_file: json-schema/quickstats-api-statistics-record-schema.json
slug: quickstats-api-statistics-record
tags:
- Agriculture
- Federal Government
- Statistics
- Open Data
- Geospatial
title: Statistics Record
---

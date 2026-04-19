---
description: Additional attributes for an employer, including both global and country-specific settings.
layout: schema
name: EmployerAttributes
properties_list:
- description: The type classification of the employer.
  name: employerType
  type: string
- description: Attributes that vary by country, such as website URLs, phone numbers, and locale-specific information.
  name: countrySpecificAttributes
  type: array
- description: Locale-specific employer attributes.
  name: localeSpecificAttributes
  type: array
provider_name: Indeed
provider_slug: indeed
schema_file: json-schema/indeed-employer-employer-attributes-schema.json
slug: indeed-employer-employer-attributes
tags:
- Careers
- Employment
- Hiring
- Job Search
- Jobs
- Recruiting
title: EmployerAttributes
---

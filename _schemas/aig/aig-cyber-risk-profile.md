---
description: Cyber risk profile for cyber insurance underwriting
layout: schema
name: CyberRiskProfile
properties_list:
- description: Organization name
  name: organization_name
  type: string
- description: Annual revenue in USD
  name: annual_revenue
  type: number
- description: Number of employees
  name: employee_count
  type: integer
- description: Number of personal data records held
  name: data_records_count
  type: integer
- description: Multi-factor authentication enabled
  name: mfa_enabled
  type: boolean
- description: Endpoint protection solution deployed
  name: endpoint_protection
  type: boolean
- description: Data backup frequency
  name: backup_frequency
  type: string
- description: Incident response plan in place
  name: incident_response_plan
  type: boolean
- description: Number of prior data breaches
  name: prior_breaches
  type: integer
provider_name: AIG
provider_slug: aig
schema_file: json-schema/aig-cyber-risk-profile-schema.json
slug: aig-cyber-risk-profile
tags:
- Insurance
- Financial Services
- Property Casualty
- Cyber Insurance
- Enterprise
title: CyberRiskProfile
---

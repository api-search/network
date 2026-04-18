---
description: Represents a single application with detailed attributes including Instances, Activity, Contract, Fiscal Spend, Compliance, and SSO Protocols.
layout: schema
name: AppDetails
properties_list:
- description: The unique identifier of the application.
  name: ApplicationId
  type: string
- description: The name of the application.
  name: AppName
  type: string
- description: The current status of the application.
  name: AppStatus
  type: string
- description: The name of the vendor.
  name: VendorName
  type: string
- description: Application instances.
  name: Instances
  type: array
- description: Usage activity metrics for the application.
  name: Activity
  type: object
- description: Contract details associated with the application.
  name: Contracts
  type: array
- description: Fiscal spend data for the application.
  name: FiscalSpend
  type: object
- description: Security standard compliance information.
  name: Compliance
  type: object
- description: SSO protocols supported by the application.
  name: SSOProtocols
  type: array
provider_name: Productiv
provider_slug: productiv
schema_file: json-schema/app-details.json
slug: app-details
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
title: AppDetails
---

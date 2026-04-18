---
description: ''
layout: schema
name: BusinessPartner
properties_list:
- description: Business partner number
  name: BusinessPartner
  type: string
- description: Full name of the business partner
  name: BusinessPartnerFullName
  type: string
- description: Category (1=Organization, 2=Person, 3=Group)
  name: BusinessPartnerCategory
  type: string
- description: Business partner grouping
  name: BusinessPartnerGrouping
  type: string
- description: First name (for person category)
  name: FirstName
  type: string
- description: Last name (for person category)
  name: LastName
  type: string
- description: Organization name line 1
  name: OrganizationBPName1
  type: string
- description: Search term 1
  name: SearchTerm1
  type: string
- description: Correspondence language
  name: Language
  type: string
- description: Date the business partner was created
  name: CreationDate
  type: string
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-s4hana-cloud-business-partner-business-partner-schema.json
slug: sap-s4hana-cloud-business-partner-business-partner
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: BusinessPartner
---

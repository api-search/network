---
description: Sales order header partner entity (A_SalesOrderHeaderPartner) representing a business partner in a specific partner function role at the header level.
layout: schema
name: SalesOrderHeaderPartner
properties_list:
- description: Sales order number
  name: SalesOrder
  type: string
- description: Partner function code (e.g., AG=Sold-to, WE=Ship-to, RE=Bill-to, RG=Payer)
  name: PartnerFunction
  type: string
- description: Customer number
  name: Customer
  type: string
- description: Supplier number
  name: Supplier
  type: string
- description: Personnel number
  name: Personnel
  type: string
- description: Contact person number
  name: ContactPerson
  type: string
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
schema_file: json-schema/sap-s4hana-sales-order-sales-order-header-partner-schema.json
slug: sap-s4hana-sales-order-sales-order-header-partner
tags:
- Business Applications
- Cloud
- Enterprise Resource Planning
- ERP
- Finance
- Human Resources
- Inventory
- Logistics
- Manufacturing
- Plant Maintenance
- Procurement
- S/4HANA
- Sales
- SAP
title: SalesOrderHeaderPartner
---

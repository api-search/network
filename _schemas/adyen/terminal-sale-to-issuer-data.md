---
description: The POI System receives this information and sends it to the Acquirer for the Issuer without any change. Sale information intended for the Issuer.
layout: schema
name: SaleToIssuerData
properties_list:
- description: Information to print on the bank statement.
  name: StatementReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-sale-to-issuer-data-schema.json
slug: terminal-sale-to-issuer-data
tags:
- Payments
- Financial Services
- Fintech
title: SaleToIssuerData
---

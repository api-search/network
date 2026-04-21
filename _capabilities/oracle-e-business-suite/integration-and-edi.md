---
consumed_apis:
- oracle-isg-rest
- oracle-ecommerce-gateway
description: Integration capabilities combining ISG REST API for service management and e-Commerce Gateway for EDI document exchange with trading partners. Used by integration architects and B2B teams.
layout: capability
name: Oracle EBS Integration and EDI
operations:
- description: Authenticate.
  method: POST
  name: login
  path: /v1/auth
- description: List trading partners.
  method: GET
  name: get-trading-partners
  path: /v1/trading-partners
- description: List inbound transactions.
  method: GET
  name: get-inbound-transactions
  path: /v1/inbound-transactions
- description: List outbound transactions.
  method: GET
  name: get-outbound-transactions
  path: /v1/outbound-transactions
personas: []
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
search_terms:
- isg initialize
- invoke a rest method on a service.
- edi get trading partner by id
- erp
- enterprise
- outbound edi transactions.
- isg login
- list inbound transactions.
- edi import inbound transaction
- edi get outbound transactions
- isg invoke rest method
- isg logout
- get outbound transactions
- trading partner management.
- retrieve outbound edi transactions.
- soa gateway
- get trading partner by id.
- e-business suite
- business applications
- authenticate.
- initialize responsibility context.
- list trading partners.
- edi extract outbound transaction
- retrieve trading partners.
- edi get trading partners
- integration
- import an inbound edi transaction.
- get wadl for a rest service.
- inbound edi transactions.
- retrieve inbound edi transactions.
- edi
- oracle
- end the current session.
- list outbound transactions.
- get inbound transactions
- login
- edi get inbound transactions
- extract an outbound edi transaction.
- retrieve code conversion mappings.
- isg get service wadl
- edi get code conversions
- get trading partners
- authenticate and obtain session token.
- authentication.
slug: integration-and-edi
tags:
- Oracle
- Integration
- EDI
- SOA Gateway
tools:
- description: Authenticate and obtain session token.
  hints:
    readOnly: false
  name: isg-login
- description: End the current session.
  hints:
    readOnly: false
  name: isg-logout
- description: Initialize responsibility context.
  hints:
    readOnly: false
  name: isg-initialize
- description: Get WADL for a REST service.
  hints:
    readOnly: true
  name: isg-get-service-wadl
- description: Invoke a REST method on a service.
  hints:
    readOnly: false
  name: isg-invoke-rest-method
- description: Retrieve trading partners.
  hints:
    openWorld: true
    readOnly: true
  name: edi-get-trading-partners
- description: Get trading partner by ID.
  hints:
    readOnly: true
  name: edi-get-trading-partner-by-id
- description: Retrieve inbound EDI transactions.
  hints:
    readOnly: true
  name: edi-get-inbound-transactions
- description: Import an inbound EDI transaction.
  hints:
    readOnly: false
  name: edi-import-inbound-transaction
- description: Retrieve outbound EDI transactions.
  hints:
    readOnly: true
  name: edi-get-outbound-transactions
- description: Extract an outbound EDI transaction.
  hints:
    readOnly: false
  name: edi-extract-outbound-transaction
- description: Retrieve code conversion mappings.
  hints:
    readOnly: true
  name: edi-get-code-conversions
---

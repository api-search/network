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
- authentication.
- retrieve code conversion mappings.
- isg login
- login
- e-business suite
- get wadl for a rest service.
- invoke a rest method on a service.
- inbound edi transactions.
- edi get trading partner by id
- get inbound transactions
- oracle
- edi get code conversions
- authenticate.
- edi
- retrieve inbound edi transactions.
- integration
- business applications
- retrieve outbound edi transactions.
- erp
- edi get trading partners
- list trading partners.
- edi get outbound transactions
- trading partner management.
- isg invoke rest method
- isg initialize
- soa gateway
- import an inbound edi transaction.
- initialize responsibility context.
- extract an outbound edi transaction.
- edi get inbound transactions
- edi extract outbound transaction
- end the current session.
- enterprise
- isg get service wadl
- get outbound transactions
- retrieve trading partners.
- isg logout
- list outbound transactions.
- outbound edi transactions.
- get trading partners
- get trading partner by id.
- list inbound transactions.
- authenticate and obtain session token.
- edi import inbound transaction
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

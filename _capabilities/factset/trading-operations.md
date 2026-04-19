---
consumed_apis:
- factset-trading
- factset-private
- factset-events
- factset-sec-model
- factset-issues
- factset-scim
- factset-ib
- factset-marketplace
- factset-partners
description: Unified workflow for trading and operations including order management, private markets, event calendars, security modeling, and user provisioning. Used by operations teams.
layout: capability
name: FactSet Trading and Operations
operations:
- description: List trading resources.
  method: GET
  name: list-trading
  path: /v1/trading
- description: List events.
  method: GET
  name: list-events
  path: /v1/events
personas: []
provider_name: Factset
provider_slug: factset
search_terms:
- get marketplace
- portfolio analytics
- get private markets
- get security models.
- research
- refresh ib office
- administration
- operations
- list issues
- get partner documents.
- financial
- get events
- get private markets data.
- get partner docs
- list support issues.
- refresh ib office data.
- event calendar.
- trading operations.
- factset
- get event calendar.
- get open marketplace.
- manage user provisioning.
- get security models
- list events
- list events.
- investment analytics
- trading
- list trading resources.
- financial data
- manage users
- list trading
- market data
slug: trading-operations
tags:
- FactSet
- Trading
- Operations
- Administration
tools:
- description: List trading resources.
  hints:
    readOnly: true
  name: list-trading
- description: Get private markets data.
  hints:
    readOnly: true
  name: get-private-markets
- description: Get event calendar.
  hints:
    readOnly: true
  name: get-events
- description: Get security models.
  hints:
    readOnly: true
  name: get-security-models
- description: List support issues.
  hints:
    readOnly: true
  name: list-issues
- description: Manage user provisioning.
  hints:
    readOnly: true
  name: manage-users
- description: Refresh IB office data.
  hints:
    readOnly: true
  name: refresh-ib-office
- description: Get Open Marketplace.
  hints:
    readOnly: true
  name: get-marketplace
- description: Get partner documents.
  hints:
    readOnly: true
  name: get-partner-docs
---

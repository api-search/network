---
aid: plaid:plaid-transferauthorizationcreate
name: Plaid Create a transfer authorization
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Use the `/transfer/authorization/create` endpoint to authorize a transfer. This endpoint must be called prior to calling `/transfer/create`.  There are three possible outcomes to calling this endpoint: If the `authorization.decision` in the response is `declined`, the proposed transfer has failed the risk check and you cannot proceed with the transfer. If the `authorization.decision` is `approved`, and the `authorization.rationale_code` is `null`, the transfer has passed the risk check and yo...

---

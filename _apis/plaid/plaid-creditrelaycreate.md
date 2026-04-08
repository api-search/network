---
aid: plaid:plaid-creditrelaycreate
name: Plaid Create a relay token to share an Asset Report with a partner client
tags:
- Plaid
humanURL: 
properties: []
description: >-
  Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.  To grant a third party access to an Asset Report, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to your third party. Each third party has its own `secondary_client_id`; for example, `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each...

---

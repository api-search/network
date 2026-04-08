---
aid: vtex:vtex-starthandling
name: VTex Start handling order
tags:
- Orders
humanURL: 
properties: []
description: >-
  Changes the status of an order to indicate that it is in `handling`.  > Expect a `status 204` response with no content in case of a successful request. The store must validate this response to retry the call if the response differs from the `204` code, making this flow the store's responsibility. This endpoint can also respond with `status 500`.   > The `Change order workflow status` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfil...

---

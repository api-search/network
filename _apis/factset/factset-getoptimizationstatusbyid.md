---
aid: factset:factset-getoptimizationstatusbyid
name: Get FPO optimization status by id
tags:
- - - - FPO Optimizer
humanURL: 
properties: []
description: >-
  This is the endpoint to check on the progress of a previously requested optimization. If the optimization has finished computing, the body of the response will contain result in JSON. Otherwise, the optimization is still running and the X-FactSet-Api-PickUp-Progress header will contain a progress percentage.

---

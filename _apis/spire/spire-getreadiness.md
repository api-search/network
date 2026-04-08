---
aid: spire:spire-getreadiness
name: SPIRE Readiness probe
tags:
- Health
humanURL: 
properties: []
description: >-
  Returns HTTP 200 if the SPIRE component is ready to serve requests. For the SPIRE Server, readiness indicates the server has completed initialization and can accept gRPC connections from agents and administrators. For the SPIRE Agent, readiness indicates it has successfully attested to the server and is able to serve the Workload API. The path can be customized via the ready_path configuration option (default: /ready).

---

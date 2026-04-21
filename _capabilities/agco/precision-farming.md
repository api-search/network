---
consumed_apis:
- agco-agcommand
description: Unified workflow capability for AGCO precision farming — monitoring machine location, performance telemetry, and operating conditions across a connected fleet. Used by farm managers and precision agriculture software developers.
layout: capability
name: AGCO Precision Farming
operations:
- description: List all connected AGCO machines.
  method: GET
  name: list-machines
  path: /v1/machines
- description: Get machine telemetry.
  method: GET
  name: get-machine-telemetry
  path: /v1/machines/{machineId}/telemetry
- description: Get machine location history.
  method: GET
  name: get-machine-locations
  path: /v1/machines/{machineId}/locations
personas:
- description: Agricultural operation manager monitoring machine fleet location and performance.
  id: farm-manager
  name: Farm Manager
- description: Developer building farm management applications using AGCO machine telemetry data.
  id: precision-ag-developer
  name: Precision Ag Developer
provider_name: agco
provider_slug: agco
search_terms:
- machine fleet management.
- get real-time performance telemetry for an agco machine.
- list all agco agricultural machines connected to the account.
- get machine telemetry
- agricultural machine inventory and fleet management.
- gps-based machine location and field work tracking.
- agricultural operation manager monitoring machine fleet location and performance.
- precision farming
- iot
- agco
- get machine location history.
- farm manager
- precision ag developer
- real-time engine, fuel, and operational telemetry monitoring.
- agriculture
- list all connected agco machines.
- fleet monitoring and performance tracking for agco agricultural machines.
- machine location history.
- machine telematics.
- get machine telemetry.
- get location history for an agco machine.
- developer building farm management applications using agco machine telemetry data.
- telematics
- get machine locations
- list machines
slug: precision-farming
tags:
- AGCO
- Agriculture
- Precision Farming
- IoT
- Telematics
tools:
- description: List all AGCO agricultural machines connected to the account.
  hints:
    destructive: false
    readOnly: true
  name: list-machines
- description: Get real-time performance telemetry for an AGCO machine.
  hints:
    destructive: false
    readOnly: true
  name: get-machine-telemetry
- description: Get location history for an AGCO machine.
  hints:
    destructive: false
    readOnly: true
  name: get-machine-locations
---

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
- list all agco agricultural machines connected to the account.
- get real-time performance telemetry for an agco machine.
- iot
- agricultural machine inventory and fleet management.
- telematics
- precision farming
- get location history for an agco machine.
- machine telematics.
- machine fleet management.
- agriculture
- agricultural operation manager monitoring machine fleet location and performance.
- precision ag developer
- gps-based machine location and field work tracking.
- developer building farm management applications using agco machine telemetry data.
- get machine locations
- fleet monitoring and performance tracking for agco agricultural machines.
- get machine telemetry.
- list machines
- get machine telemetry
- machine location history.
- get machine location history.
- list all connected agco machines.
- agco
- farm manager
- real-time engine, fuel, and operational telemetry monitoring.
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

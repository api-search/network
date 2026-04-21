---
consumed_apis:
- opencue
description: Render farm management workflow using OpenCue for monitoring and managing render jobs, layers, frames, and hosts in a VFX production pipeline. Used by render wranglers and pipeline TDs to monitor and troubleshoot render farm operations.
layout: capability
name: Academy Software Foundation Render Farm Management
operations:
- description: List all active shows in the render farm
  method: GET
  name: list-shows
  path: /v1/shows
- description: List render jobs for a show
  method: GET
  name: list-jobs
  path: /v1/jobs
- description: Get details for a specific render job
  method: GET
  name: get-job
  path: /v1/jobs/{job_id}
- description: List all render host machines
  method: GET
  name: list-hosts
  path: /v1/hosts
personas:
- description: Production staff responsible for monitoring and managing render farm operations
  id: render-wrangler
  name: Render Wrangler
- description: Technical director building and maintaining VFX production pipeline tools
  id: pipeline-td
  name: Pipeline TD
provider_name: Academy Software Foundation
provider_slug: academy-software-foundation
search_terms:
- vfx
- list and manage render hosts
- list and manage render jobs
- list all active shows (productions) in the render farm
- academy software foundation
- list jobs
- pipeline td
- render wrangler
- list render jobs for a specific show with optional state filtering
- vfx pipeline
- list render hosts
- render farm
- list render jobs for a show
- technical director building and maintaining vfx production pipeline tools
- list all render host machines and their current utilization
- open source
- color management
- get details for a specific render job
- animation
- monitor and manage render jobs, hosts, and shows using opencue
- list all render host machines
- list render jobs
- film
- get detailed status and frame counts for a specific render job
- linux foundation
- list shows
- visual effects
- monitoring and management of distributed render farm resources and jobs
- list and manage render shows (productions)
- list hosts
- get render job
- standards
- production staff responsible for monitoring and managing render farm operations
- get job
- list all active shows in the render farm
- get or kill a specific render job
- opencue
- rendering
slug: render-farm-management
tags:
- Academy Software Foundation
- Render Farm
- Opencue
- Vfx Pipeline
tools:
- description: List all active shows (productions) in the render farm
  hints:
    openWorld: false
    readOnly: true
  name: list-shows
- description: List render jobs for a specific show with optional state filtering
  hints:
    openWorld: false
    readOnly: true
  name: list-render-jobs
- description: Get detailed status and frame counts for a specific render job
  hints:
    openWorld: false
    readOnly: true
  name: get-render-job
- description: List all render host machines and their current utilization
  hints:
    openWorld: false
    readOnly: true
  name: list-render-hosts
---

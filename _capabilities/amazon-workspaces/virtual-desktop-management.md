---
consumed_apis:
- workspaces
description: Unified workflow for IT administrators and end user computing teams to provision, manage, and maintain Amazon WorkSpaces virtual desktops at scale, including workspace lifecycle, bundle management, directory integration, and image management.
layout: capability
name: Amazon WorkSpaces Virtual Desktop Management
operations:
- description: List virtual desktops.
  method: GET
  name: describe-workspaces
  path: /v1/workspaces
- description: Provision new virtual desktops.
  method: POST
  name: create-workspaces
  path: /v1/workspaces
- description: List available bundles.
  method: GET
  name: describe-workspace-bundles
  path: /v1/bundles
- description: List directories.
  method: GET
  name: describe-workspace-directories
  path: /v1/directories
- description: List workspace images.
  method: GET
  name: describe-workspace-images
  path: /v1/images
personas: []
provider_name: Amazon WorkSpaces
provider_slug: amazon-workspaces
search_terms:
- IT Administrator
- End User Computing Engineer
- workspace image management.
- administration
- describe workspaces
- permanently terminate virtual desktop workspaces.
- provision new virtual desktops.
- hardware bundle catalog.
- directory management.
- list available workspace images for provisioning.
- cloud-based virtual desktop provisioning and management
- workflow for it administrators to provision and manage amazon workspaces virtual desktops including lifecycle, bundles, directories, and images.
- list virtual desktops.
- create workspaces
- provision new virtual desktop workspaces for users.
- terminate workspaces
- list workspace images.
- manages workspaces provisioning, lifecycle, and policy.
- list available bundles.
- reboot virtual desktop workspaces to resolve issues.
- describe workspace bundles
- list directories.
- desktop
- reboot workspaces
- virtual desktop lifecycle management.
- remote work and desktop-as-a-service infrastructure
- it administration of desktop resources
- aws
- desktop as a service
- describe workspace images
- list and describe all virtual desktop workspaces.
- virtual desktop
- describe workspace directories
- list available hardware configuration bundles.
- end user computing
- list registered directories for workspace deployment.
- designs and operates virtual desktop infrastructure.
slug: virtual-desktop-management
tags:
- AWS
- Virtual Desktop
- End User Computing
- Desktop as a Service
- Administration
tools:
- description: List and describe all virtual desktop workspaces.
  hints:
    openWorld: true
    readOnly: true
  name: describe-workspaces
- description: Provision new virtual desktop workspaces for users.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-workspaces
- description: Permanently terminate virtual desktop workspaces.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: terminate-workspaces
- description: Reboot virtual desktop workspaces to resolve issues.
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: reboot-workspaces
- description: List available hardware configuration bundles.
  hints:
    openWorld: true
    readOnly: true
  name: describe-workspace-bundles
- description: List registered directories for workspace deployment.
  hints:
    openWorld: true
    readOnly: true
  name: describe-workspace-directories
- description: List available workspace images for provisioning.
  hints:
    openWorld: true
    readOnly: true
  name: describe-workspace-images
---

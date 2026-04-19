---
consumed_apis:
- app-store-connect
description: Unified workflow for managing the Apple app lifecycle including app metadata, builds, TestFlight beta testing, and beta group management. Used by app developers and release managers.
layout: capability
name: Apple App Lifecycle
operations:
- description: List all apps.
  method: GET
  name: list-apps
  path: /v1/apps
- description: List all builds.
  method: GET
  name: list-builds
  path: /v1/builds
- description: List beta testers.
  method: GET
  name: list-testers
  path: /v1/testers
- description: Add a beta tester.
  method: POST
  name: create-tester
  path: /v1/testers
- description: List beta groups.
  method: GET
  name: list-groups
  path: /v1/groups
- description: Create a beta group.
  method: POST
  name: create-group
  path: /v1/groups
personas: []
provider_name: Apple
provider_slug: apple
search_terms:
- list all builds.
- app management.
- macos
- list beta groups.
- beta group management.
- read app
- list all beta testers.
- list beta groups
- create beta group
- modify build
- technology
- list apps
- remove a beta tester.
- create a new beta group.
- beta tester management.
- app management
- list beta testers
- mobile
- create beta tester
- add a beta tester.
- developer
- get beta group details.
- app store
- list testers
- build management.
- get beta tester details.
- add a new beta tester.
- delete beta group
- modify app
- get details of a specific app.
- update app metadata.
- delete a beta group.
- list beta testers.
- ios
- testflight
- read build
- modify beta group
- update build information.
- create tester
- list builds
- update a beta group.
- create a beta group.
- apple
- read beta group
- list groups
- list all apps in app store connect.
- create group
- delete beta tester
- read beta tester
- list all apps.
- get build details.
- list all beta groups.
slug: app-lifecycle
tags:
- Apple
- App Store
- TestFlight
- App Management
tools:
- description: List all apps in App Store Connect.
  hints:
    openWorld: true
    readOnly: true
  name: list-apps
- description: Get details of a specific app.
  hints:
    readOnly: true
  name: read-app
- description: Update app metadata.
  hints:
    idempotent: true
    readOnly: false
  name: modify-app
- description: List all builds.
  hints:
    readOnly: true
  name: list-builds
- description: Get build details.
  hints:
    readOnly: true
  name: read-build
- description: Update build information.
  hints:
    idempotent: true
    readOnly: false
  name: modify-build
- description: List all beta testers.
  hints:
    readOnly: true
  name: list-beta-testers
- description: Add a new beta tester.
  hints:
    readOnly: false
  name: create-beta-tester
- description: Get beta tester details.
  hints:
    readOnly: true
  name: read-beta-tester
- description: Remove a beta tester.
  hints:
    destructive: true
    idempotent: true
  name: delete-beta-tester
- description: List all beta groups.
  hints:
    readOnly: true
  name: list-beta-groups
- description: Create a new beta group.
  hints:
    readOnly: false
  name: create-beta-group
- description: Get beta group details.
  hints:
    readOnly: true
  name: read-beta-group
- description: Update a beta group.
  hints:
    idempotent: true
    readOnly: false
  name: modify-beta-group
- description: Delete a beta group.
  hints:
    destructive: true
    idempotent: true
  name: delete-beta-group
---

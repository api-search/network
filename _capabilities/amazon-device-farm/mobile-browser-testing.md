---
consumed_apis:
- device-farm
description: Workflow capability for QA engineers and mobile developers to run automated tests on real physical devices and desktop browsers using AWS Device Farm. Combines project management, device pool configuration, test scheduling, artifact collection, and remote access session management.
layout: capability
name: AWS Device Farm Mobile and Browser Testing
operations:
- description: List all Device Farm test projects
  method: GET
  name: list-projects
  path: /v1/projects
- description: Create a new test project
  method: POST
  name: create-project
  path: /v1/projects
- description: List available real physical devices
  method: GET
  name: list-devices
  path: /v1/devices
- description: List device pools
  method: GET
  name: list-device-pools
  path: /v1/device-pools
- description: Create a device pool with filter rules
  method: POST
  name: create-device-pool
  path: /v1/device-pools
- description: Upload an app or test package
  method: POST
  name: create-upload
  path: /v1/uploads
- description: List uploads for a project
  method: GET
  name: list-uploads
  path: /v1/uploads
- description: Schedule a test run on real devices
  method: POST
  name: schedule-run
  path: /v1/runs
- description: List test runs for a project
  method: GET
  name: list-runs
  path: /v1/runs
- description: Get test run results and status
  method: GET
  name: get-run
  path: /v1/runs/{runArn}
- description: Stop a running test
  method: DELETE
  name: stop-run
  path: /v1/runs/{runArn}
- description: Start a remote access session on a device
  method: POST
  name: create-remote-access-session
  path: /v1/remote-access-sessions
- description: List remote access sessions
  method: GET
  name: list-remote-access-sessions
  path: /v1/remote-access-sessions
- description: List Selenium test grid projects
  method: GET
  name: list-test-grid-projects
  path: /v1/test-grid-projects
- description: Create a new Selenium test grid project
  method: POST
  name: create-test-grid-project
  path: /v1/test-grid-projects
personas: []
provider_name: Amazon Device Farm
provider_slug: amazon-device-farm
search_terms:
- list available real physical devices for testing
- list remote access sessions
- get upload
- create a new selenium test grid project
- create device pool
- list all device farm test projects
- create upload
- stop a currently running test
- stop a running test
- create a new device farm test project
- create an upload slot and get a pre-signed url to upload your app or test package
- list jobs
- start an interactive remote access session on a real device
- mobile app developer running tests on real devices to validate app quality
- test run lifecycle
- testing web applications in selenium-powered desktop browsers
- mobile testing
- interactive remote access to real devices for debugging
- stop run
- list artifacts
- list test runs for a project
- create remote access session
- list selenium test grid projects
- get test run results and status
- stop remote access session
- list test grid projects
- list unique problems found across test runs
- quality assurance
- list devices
- device testing
- schedule a test run on real devices
- end-to-end testing workflow for mobile apps on real devices and web apps in browsers
- create a signed url for selenium remotewebdriver to connect to device farm
- testing mobile applications on real physical ios and android devices
- get the status and results of a test run
- quality assurance engineer managing test infrastructure and running automated test suites
- list test artifacts like screenshots, logs, and videos from a run
- Mobile Developer
- app and test artifact uploads
- get run
- list selenium test grid projects for browser testing
- application testing
- list unique problems
- list jobs within a test run
- list available real physical devices
- list projects
- create a device pool with rules to filter devices for testing
- create a device pool with filter rules
- selenium browser test grid projects
- real device catalog
- create test grid url
- upload an app or test package
- list device pools
- stop an active remote access session
- schedule run
- remote device access sessions
- test project management
- list device pools configured for a project
- create a new test project
- start a remote access session on a device
- aws
- test automation
- device pool configuration
- create test grid project
- check the status of an uploaded app or test package
- QA Engineer
- schedule a test run on real physical devices
- amazon device farm
- list uploads for a project
- individual run management
- browser testing
- create project
- list all test runs for a project
- list runs
- list uploads
- list all aws device farm test projects
slug: mobile-browser-testing
tags:
- Amazon Device Farm
- Mobile Testing
- Browser Testing
- Quality Assurance
- Test Automation
- AWS
tools:
- description: List all AWS Device Farm test projects
  hints:
    openWorld: true
    readOnly: true
  name: list-projects
- description: Create a new Device Farm test project
  hints:
    destructive: false
    readOnly: false
  name: create-project
- description: List available real physical devices for testing
  hints:
    openWorld: true
    readOnly: true
  name: list-devices
- description: List device pools configured for a project
  hints:
    openWorld: true
    readOnly: true
  name: list-device-pools
- description: Create a device pool with rules to filter devices for testing
  hints:
    destructive: false
    readOnly: false
  name: create-device-pool
- description: Create an upload slot and get a pre-signed URL to upload your app or test package
  hints:
    destructive: false
    readOnly: false
  name: create-upload
- description: Check the status of an uploaded app or test package
  hints:
    openWorld: false
    readOnly: true
  name: get-upload
- description: Schedule a test run on real physical devices
  hints:
    destructive: false
    readOnly: false
  name: schedule-run
- description: Get the status and results of a test run
  hints:
    openWorld: false
    readOnly: true
  name: get-run
- description: List all test runs for a project
  hints:
    openWorld: true
    readOnly: true
  name: list-runs
- description: Stop a currently running test
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: stop-run
- description: List jobs within a test run
  hints:
    openWorld: true
    readOnly: true
  name: list-jobs
- description: Start an interactive remote access session on a real device
  hints:
    destructive: false
    readOnly: false
  name: create-remote-access-session
- description: Stop an active remote access session
  hints:
    destructive: true
    readOnly: false
  name: stop-remote-access-session
- description: List Selenium test grid projects for browser testing
  hints:
    openWorld: true
    readOnly: true
  name: list-test-grid-projects
- description: Create a signed URL for Selenium RemoteWebDriver to connect to Device Farm
  hints:
    destructive: false
    readOnly: false
  name: create-test-grid-url
- description: List test artifacts like screenshots, logs, and videos from a run
  hints:
    openWorld: true
    readOnly: true
  name: list-artifacts
- description: List unique problems found across test runs
  hints:
    openWorld: true
    readOnly: true
  name: list-unique-problems
---

---
consumed_apis:
- scand-manager
description: Workflow capability for DevSecOps engineers and security teams running automated API conformance scans on Kubernetes. Combines scan job management and log retrieval into a unified interface for CI/CD pipeline integration, on-premises security testing, and runtime compliance validation.
layout: capability
name: 42Crunch API Security Scanning
operations:
- description: List all active and completed API conformance scans
  method: GET
  name: list-scans
  path: /v1/scans
- description: Start a new API conformance scan job on Kubernetes
  method: POST
  name: run-scan
  path: /v1/scans
- description: Get the current status of a specific API conformance scan
  method: GET
  name: get-scan-status
  path: /v1/scans/{name}
- description: Cancel and remove a specific API conformance scan job
  method: DELETE
  name: cancel-scan
  path: /v1/scans/{name}
- description: Retrieve execution logs from an API conformance scan
  method: GET
  name: get-scan-logs
  path: /v1/scans/{name}/logs
- description: Check the scan manager service health
  method: GET
  name: check-health
  path: /v1/health
personas: []
provider_name: 42Crunch
provider_slug: 42crunch
search_terms:
- check the health status of the 42crunch scan manager service to verify availability
- conformance scanning
- DevSecOps Engineer
- workflow for devsecops engineers running automated api conformance scans on kubernetes with ci/cd pipeline integration.
- ensuring apis are secure and compliant with security standards
- check or remove a specific scan job
- managing containerized workloads for api scan execution
- get scan status
- access scan execution logs
- check scanner health
- cancel and remove a specific api conformance scan job
- list all api conformance scan jobs including their current status (started, active, succeeded, failed)
- check the scan manager service health
- get the current status of a specific api conformance scan job (started, active, succeeded, failed, unknown)
- platform
- list scans
- run api scan
- security
- cancel scan
- retrieve execution logs from an api conformance scan
- security professionals managing api conformance testing, reviewing scan results, and ensuring apis meet security standards before and after deployment.
- run scan
- get the current status of a specific api conformance scan
- kubernetes
- retrieve execution logs from an api conformance scan job to diagnose failures or review results
- validating api runtime behavior against openapi contract specifications
- start a new 42crunch api conformance scan job on kubernetes using a scan token from the 42crunch platform
- devsecops
- start a new api conformance scan job on kubernetes
- check health
- cancel and remove a specific api conformance scan job from the kubernetes cluster
- list all active and completed api conformance scans
- manage api conformance scan jobs
- service health check
- cancel api scan
- list api scans
- openapi
- ci/cd
- scanning
- api security
- Security Team
- engineers embedding api security scanning into ci/cd pipelines and automating conformance testing as part of the development workflow.
- get scan logs
slug: api-security-scanning
tags:
- API Security
- Conformance Scanning
- Kubernetes
- DevSecOps
- CI/CD
tools:
- description: List all API conformance scan jobs including their current status (started, active, succeeded, failed)
  hints:
    openWorld: false
    readOnly: true
  name: list-api-scans
- description: Start a new 42Crunch API conformance scan job on Kubernetes using a scan token from the 42Crunch platform
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: run-api-scan
- description: Get the current status of a specific API conformance scan job (started, active, succeeded, failed, unknown)
  hints:
    openWorld: false
    readOnly: true
  name: get-scan-status
- description: Cancel and remove a specific API conformance scan job from the Kubernetes cluster
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: cancel-api-scan
- description: Retrieve execution logs from an API conformance scan job to diagnose failures or review results
  hints:
    openWorld: false
    readOnly: true
  name: get-scan-logs
- description: Check the health status of the 42Crunch scan manager service to verify availability
  hints:
    openWorld: false
    readOnly: true
  name: check-scanner-health
---

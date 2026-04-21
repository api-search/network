---
consumed_apis:
- automation
- admin-rest
description: Workflow for security vulnerability management, automated patching, compliance reporting, and health monitoring across WebSphere environments for security engineers and compliance teams.
layout: capability
name: WebSphere Security and Compliance
operations:
- description: List known vulnerabilities
  method: GET
  name: list-vulnerabilities
  path: /v1/vulnerabilities
- description: Get vulnerability details
  method: GET
  name: get-vulnerability
  path: /v1/vulnerabilities
- description: List available fixes
  method: GET
  name: list-fixes
  path: /v1/fixes
- description: List compliance reports
  method: GET
  name: list-compliance-reports
  path: /v1/compliance
- description: Get overall health status
  method: GET
  name: get-overall-health
  path: /v1/health
- description: List security users
  method: GET
  name: list-users
  path: /v1/security-users
personas: []
provider_name: IBM WebSphere
provider_slug: websphere
search_terms:
- compliance
- fix and patch management
- list available fixes
- ibm websphere
- list vulnerabilities
- list servers managed by websphere automation
- vulnerability tracking and remediation
- j2ee
- get overall environment health
- apply a fix to managed servers
- apply fix
- health monitoring
- list compliance reports
- list users
- get vulnerability details
- resolve vulnerability
- get overall health
- security
- cloud native
- get overall health status
- list available security fixes
- initiate vulnerability resolution
- get server health
- list managed servers
- middleware
- get vulnerability
- security user management
- list fixes
- enterprise java
- list known vulnerabilities
- compliance reporting
- application server
- microservices
- get individual server health
- list known security vulnerabilities
- list security users
- vulnerability management
slug: security-and-compliance
tags:
- IBM WebSphere
- Security
- Compliance
- Vulnerability Management
tools:
- description: List known security vulnerabilities
  hints:
    readOnly: true
  name: list-vulnerabilities
- description: Get vulnerability details
  hints:
    readOnly: true
  name: get-vulnerability
- description: Initiate vulnerability resolution
  hints:
    readOnly: false
  name: resolve-vulnerability
- description: List available security fixes
  hints:
    readOnly: true
  name: list-fixes
- description: Apply a fix to managed servers
  hints:
    readOnly: false
  name: apply-fix
- description: Get overall environment health
  hints:
    readOnly: true
  name: get-overall-health
- description: Get individual server health
  hints:
    readOnly: true
  name: get-server-health
- description: List compliance reports
  hints:
    readOnly: true
  name: list-compliance-reports
- description: List servers managed by WebSphere Automation
  hints:
    readOnly: true
  name: list-managed-servers
---

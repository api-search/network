---
consumed_apis:
- github-security
description: Unified workflow for security operations combining code scanning, Dependabot, and secret scanning. Used by security engineers for vulnerability management, dependency auditing, and secret leak remediation.
layout: capability
name: GitHub Security Operations
operations:
- description: List code scanning alerts
  method: GET
  name: listCodeScanningAlertsForRepository
  path: /v1/repositories/{owner}/{repo}/code-scanning/alerts
- description: Get a code scanning alert
  method: GET
  name: getCodeScanningAlert
  path: /v1/repositories/{owner}/{repo}/code-scanning/alerts/{alert_number}
- description: Update a code scanning alert
  method: PATCH
  name: updateCodeScanningAlert
  path: /v1/repositories/{owner}/{repo}/code-scanning/alerts/{alert_number}
- description: List analyses
  method: GET
  name: listCodeScanningAnalysesForRepository
  path: /v1/repositories/{owner}/{repo}/code-scanning/analyses
- description: List Dependabot alerts
  method: GET
  name: listDependabotAlertsForRepository
  path: /v1/repositories/{owner}/{repo}/dependabot/alerts
- description: Get a Dependabot alert
  method: GET
  name: getDependabotAlert
  path: /v1/repositories/{owner}/{repo}/dependabot/alerts/{alert_number}
- description: Update a Dependabot alert
  method: PATCH
  name: updateDependabotAlert
  path: /v1/repositories/{owner}/{repo}/dependabot/alerts/{alert_number}
- description: List secret scanning alerts
  method: GET
  name: listSecretScanningAlertsForRepository
  path: /v1/repositories/{owner}/{repo}/secret-scanning/alerts
- description: Get a secret scanning alert
  method: GET
  name: getSecretScanningAlert
  path: /v1/repositories/{owner}/{repo}/secret-scanning/alerts/{alert_number}
- description: Update a secret scanning alert
  method: PATCH
  name: updateSecretScanningAlert
  path: /v1/repositories/{owner}/{repo}/secret-scanning/alerts/{alert_number}
- description: Check vulnerability alert status
  method: GET
  name: checkIfVulnerabilityAlertsAreEnabledForRepository
  path: /v1/repositories/{owner}/{repo}/vulnerability-alerts
- description: Enable vulnerability alerts
  method: PUT
  name: enableVulnerabilityAlerts
  path: /v1/repositories/{owner}/{repo}/vulnerability-alerts
personas: []
provider_name: GitHub
provider_slug: github
search_terms:
- check vulnerability alert status
- individual code scanning alert
- getCodeScanningAlert
- get code scanning analysis
- disable vulnerability alerts
- check vulnerability alerts
- t1
- enable vulnerability alerts
- listDependabotAlertsForRepository
- listCodeScanningAlertsForRepository
- list secret scanning alerts
- update a dependabot alert
- list analyses
- upload sarif
- update a code scanning alert (dismiss, reopen)
- code scanning alert management
- list locations for a secret scanning alert
- code scanning
- get a dependabot alert
- code
- software development
- secret scanning alert management
- getSecretScanningAlert
- enableVulnerabilityAlerts
- get code scanning default setup configuration
- list dependabot secrets
- get a secret scanning alert
- github
- vulnerability management
- get a code scanning alert
- get dependabot alert
- updateDependabotAlert
- pipelines
- list dependabot alerts
- list code scanning analyses
- update a code scanning alert
- secret scanning
- updateSecretScanningAlert
- dependabot
- checkIfVulnerabilityAlertsAreEnabledForRepository
- getDependabotAlert
- get default setup
- update secret scanning alert
- update a dependabot alert (dismiss, reopen)
- check if vulnerability alerts are enabled
- platform
- dependabot alert management
- update default setup
- code scanning analyses
- update code scanning alert
- get a code scanning analysis
- list secret scanning locations
- get secret scanning alert
- vulnerability alert settings
- security
- listCodeScanningAnalysesForRepository
- update code scanning default setup
- listSecretScanningAlertsForRepository
- update a secret scanning alert
- get code scanning alert
- update a secret scanning alert (resolve, reopen)
- source control
- updateCodeScanningAlert
- individual dependabot alert
- upload sarif analysis data
- list code scanning alerts for a repository
- individual secret scanning alert
- update dependabot alert
- list code scanning alerts
slug: security-operations
tags:
- GitHub
- Security
- Code Scanning
- Dependabot
- Secret Scanning
- Vulnerability Management
tools:
- description: List code scanning alerts for a repository
  hints:
    readOnly: true
  name: list-code-scanning-alerts
- description: Get a code scanning alert
  hints:
    readOnly: true
  name: get-code-scanning-alert
- description: Update a code scanning alert (dismiss, reopen)
  hints:
    idempotent: true
  name: update-code-scanning-alert
- description: List code scanning analyses
  hints:
    readOnly: true
  name: list-code-scanning-analyses
- description: Get a code scanning analysis
  hints:
    readOnly: true
  name: get-code-scanning-analysis
- description: Upload SARIF analysis data
  hints: {}
  name: upload-sarif
- description: Get code scanning default setup configuration
  hints:
    readOnly: true
  name: get-default-setup
- description: Update code scanning default setup
  hints:
    idempotent: true
  name: update-default-setup
- description: List Dependabot alerts
  hints:
    readOnly: true
  name: list-dependabot-alerts
- description: Get a Dependabot alert
  hints:
    readOnly: true
  name: get-dependabot-alert
- description: Update a Dependabot alert (dismiss, reopen)
  hints:
    idempotent: true
  name: update-dependabot-alert
- description: List Dependabot secrets
  hints:
    readOnly: true
  name: list-dependabot-secrets
- description: List secret scanning alerts
  hints:
    readOnly: true
  name: list-secret-scanning-alerts
- description: Get a secret scanning alert
  hints:
    readOnly: true
  name: get-secret-scanning-alert
- description: Update a secret scanning alert (resolve, reopen)
  hints:
    idempotent: true
  name: update-secret-scanning-alert
- description: List locations for a secret scanning alert
  hints:
    readOnly: true
  name: list-secret-scanning-locations
- description: Check if vulnerability alerts are enabled
  hints:
    readOnly: true
  name: check-vulnerability-alerts
- description: Enable vulnerability alerts
  hints: {}
  name: enable-vulnerability-alerts
- description: Disable vulnerability alerts
  hints:
    destructive: true
  name: disable-vulnerability-alerts
---

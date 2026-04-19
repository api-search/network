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
- enable vulnerability alerts
- software development
- updateDependabotAlert
- code scanning
- listCodeScanningAlertsForRepository
- code scanning alert management
- getDependabotAlert
- get code scanning alert
- update secret scanning alert
- security
- update a dependabot alert
- listSecretScanningAlertsForRepository
- get a code scanning analysis
- individual code scanning alert
- list locations for a secret scanning alert
- list analyses
- update code scanning default setup
- t1
- list code scanning analyses
- list code scanning alerts for a repository
- upload sarif
- secret scanning
- individual secret scanning alert
- upload sarif analysis data
- listDependabotAlertsForRepository
- list dependabot secrets
- get code scanning default setup configuration
- list code scanning alerts
- update a secret scanning alert (resolve, reopen)
- enableVulnerabilityAlerts
- check if vulnerability alerts are enabled
- github
- get default setup
- update a code scanning alert
- update a code scanning alert (dismiss, reopen)
- get secret scanning alert
- get a secret scanning alert
- update code scanning alert
- dependabot alert management
- update default setup
- get a code scanning alert
- update a dependabot alert (dismiss, reopen)
- listCodeScanningAnalysesForRepository
- pipelines
- list secret scanning locations
- updateCodeScanningAlert
- dependabot
- code
- list secret scanning alerts
- checkIfVulnerabilityAlertsAreEnabledForRepository
- code scanning analyses
- check vulnerability alert status
- updateSecretScanningAlert
- list dependabot alerts
- individual dependabot alert
- getCodeScanningAlert
- secret scanning alert management
- vulnerability alert settings
- platform
- get dependabot alert
- disable vulnerability alerts
- source control
- update dependabot alert
- check vulnerability alerts
- update a secret scanning alert
- getSecretScanningAlert
- vulnerability management
- get a dependabot alert
- get code scanning analysis
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

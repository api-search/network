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
- check vulnerability alerts
- individual dependabot alert
- listCodeScanningAnalysesForRepository
- getSecretScanningAlert
- check vulnerability alert status
- get dependabot alert
- get a code scanning analysis
- update a secret scanning alert
- secret scanning
- check if vulnerability alerts are enabled
- enableVulnerabilityAlerts
- pipelines
- list locations for a secret scanning alert
- platform
- list code scanning alerts
- dependabot alert management
- get a secret scanning alert
- update a dependabot alert (dismiss, reopen)
- disable vulnerability alerts
- listCodeScanningAlertsForRepository
- listSecretScanningAlertsForRepository
- getCodeScanningAlert
- get code scanning default setup configuration
- update a code scanning alert
- get a code scanning alert
- list secret scanning locations
- updateCodeScanningAlert
- list secret scanning alerts
- software development
- github
- code scanning
- t1
- update secret scanning alert
- update a code scanning alert (dismiss, reopen)
- list code scanning alerts for a repository
- checkIfVulnerabilityAlertsAreEnabledForRepository
- code scanning analyses
- dependabot
- security
- secret scanning alert management
- update dependabot alert
- list dependabot alerts
- update code scanning alert
- enable vulnerability alerts
- getDependabotAlert
- source control
- updateDependabotAlert
- list dependabot secrets
- update default setup
- get code scanning alert
- listDependabotAlertsForRepository
- code scanning alert management
- get a dependabot alert
- updateSecretScanningAlert
- get secret scanning alert
- individual secret scanning alert
- get default setup
- update code scanning default setup
- vulnerability alert settings
- list code scanning analyses
- upload sarif analysis data
- list analyses
- upload sarif
- code
- update a secret scanning alert (resolve, reopen)
- update a dependabot alert
- get code scanning analysis
- individual code scanning alert
- vulnerability management
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

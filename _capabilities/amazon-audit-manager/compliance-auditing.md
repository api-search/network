---
consumed_apis: []
description: Workflow capability for conducting continuous compliance auditing with Amazon Audit Manager including assessment creation, evidence collection, and report generation.
layout: capability
name: Compliance Auditing Workflow
operations:
- description: List all assessments
  method: GET
  name: list-assessments
  path: /v1/assessments
- description: Create a new assessment
  method: POST
  name: create-assessment
  path: /v1/assessments
- description: List available frameworks
  method: GET
  name: list-frameworks
  path: /v1/frameworks
personas: []
provider_name: Amazon Audit Manager
provider_slug: amazon-audit-manager
search_terms:
- create control
- amazon audit manager
- get audit manager account settings including default destinations and process owners.
- generate a compliance assessment report from collected evidence.
- list controls
- update settings
- list available compliance frameworks such as soc 2, pci dss, and hipaa.
- create a new assessment
- list assessments
- get assessment
- create a custom compliance control for use in frameworks and assessments.
- list assessment reports
- get settings
- create assessment
- list frameworks
- list all assessments
- compliance
- get complete details of a compliance assessment including control status.
- aws
- list available frameworks
- compliance assessment management
- compliance framework management
- list compliance controls available for building assessments.
- risk management
- create a new compliance assessment using a regulatory framework.
- list all compliance assessments to understand current audit coverage.
- create assessment report
- list generated assessment reports for compliance documentation.
- audit
- update audit manager settings including sns notifications and default report destination.
slug: compliance-auditing
tags:
- Amazon Audit Manager
- Compliance
- Audit
- Risk Management
- AWS
tools:
- description: List all compliance assessments to understand current audit coverage.
  hints:
    openWorld: true
    readOnly: true
  name: list-assessments
- description: Create a new compliance assessment using a regulatory framework.
  hints:
    openWorld: false
    readOnly: false
  name: create-assessment
- description: Get complete details of a compliance assessment including control status.
  hints:
    openWorld: true
    readOnly: true
  name: get-assessment
- description: List available compliance frameworks such as SOC 2, PCI DSS, and HIPAA.
  hints:
    openWorld: true
    readOnly: true
  name: list-frameworks
- description: List compliance controls available for building assessments.
  hints:
    openWorld: true
    readOnly: true
  name: list-controls
- description: Create a custom compliance control for use in frameworks and assessments.
  hints:
    openWorld: false
    readOnly: false
  name: create-control
- description: List generated assessment reports for compliance documentation.
  hints:
    openWorld: true
    readOnly: true
  name: list-assessment-reports
- description: Generate a compliance assessment report from collected evidence.
  hints:
    openWorld: false
    readOnly: false
  name: create-assessment-report
- description: Get Audit Manager account settings including default destinations and process owners.
  hints:
    openWorld: true
    readOnly: true
  name: get-settings
- description: Update Audit Manager settings including SNS notifications and default report destination.
  hints:
    openWorld: false
    readOnly: false
  name: update-settings
---

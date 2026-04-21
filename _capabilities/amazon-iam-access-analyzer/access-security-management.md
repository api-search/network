---
consumed_apis:
- iam-access-analyzer
description: Unified capability for security teams to manage access analyzers, review findings, validate policies, and enforce least-privilege access controls across AWS accounts.
layout: capability
name: Amazon IAM Access Analyzer - Access Security Management
operations:
- description: List all access analyzers in the account
  method: GET
  name: list-analyzers
  path: /v1/analyzers
- description: Create a new access analyzer
  method: POST
  name: create-analyzer
  path: /v1/analyzers
- description: List findings from an analyzer
  method: GET
  name: list-findings
  path: /v1/findings
- description: Validate an IAM policy for best practices
  method: POST
  name: validate-policy
  path: /v1/policies/validate
- description: Start generating a policy based on CloudTrail activity
  method: POST
  name: start-policy-generation
  path: /v1/policies/generate
personas: []
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
search_terms:
- create a new iam access analyzer for an account or organization
- validate an iam policy for best practices
- compliance
- list all iam access analyzers configured in the account
- manage access analyzers
- list analyzers
- create access preview
- Security Engineer
- review access analyzer findings
- create analyzer
- retrieve a policy generated from cloudtrail activity
- Cloud Security Engineer
- list archive rules for an analyzer
- get details of a specific access finding
- list findings from an analyzer
- get finding
- iam
- reviews access findings and remediates unintended access
- start policy generation
- list security findings from an access analyzer
- validate policy
- ensuring access controls meet security standards
- list all access analyzers in the account
- security
- validate iam policies
- get generated policy
- generate iam policies from activity logs
- manage analyzers, findings, validate policies, and generate least-privilege policies
- list findings
- preview access changes before deploying permission changes
- policy management
- access control
- creating, validating, and optimizing iam policies
- list archive rules
- generate an iam policy based on cloudtrail access activity logs
- aws
- create a new access analyzer
- IAM Administrator
- managing who can access what resources
- start generating a policy based on cloudtrail activity
- manages iam policies, roles, and access controls
- validate an iam policy document for best practices and security issues
slug: access-security-management
tags:
- AWS
- IAM
- Security
- Access Control
- Compliance
- Policy Management
tools:
- description: List all IAM Access Analyzers configured in the account
  hints:
    openWorld: true
    readOnly: true
  name: list-analyzers
- description: Create a new IAM Access Analyzer for an account or organization
  hints:
    readOnly: false
  name: create-analyzer
- description: List security findings from an access analyzer
  hints:
    openWorld: true
    readOnly: true
  name: list-findings
- description: Get details of a specific access finding
  hints:
    openWorld: true
    readOnly: true
  name: get-finding
- description: Validate an IAM policy document for best practices and security issues
  hints:
    openWorld: false
    readOnly: true
  name: validate-policy
- description: Generate an IAM policy based on CloudTrail access activity logs
  hints:
    readOnly: false
  name: start-policy-generation
- description: Retrieve a policy generated from CloudTrail activity
  hints:
    openWorld: false
    readOnly: true
  name: get-generated-policy
- description: Preview access changes before deploying permission changes
  hints:
    readOnly: false
  name: create-access-preview
- description: List archive rules for an analyzer
  hints:
    openWorld: true
    readOnly: true
  name: list-archive-rules
---

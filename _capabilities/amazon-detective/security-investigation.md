---
consumed_apis:
- detective
description: Workflow capability for SOC analysts and security engineers to conduct end-to-end security investigations using Amazon Detective. Combines behavior graph management, member account administration, investigation lifecycle management, and indicator analysis into a unified workflow for threat hunting and security forensics.
layout: capability
name: Amazon Detective Security Investigation
operations:
- description: List all behavior graphs
  method: GET
  name: list-graphs
  path: /v1/graphs
- description: Create a new behavior graph
  method: POST
  name: create-graph
  path: /v1/graphs
- description: List member accounts contributing to the behavior graph
  method: GET
  name: list-members
  path: /v1/graphs/{graphArn}/members
- description: Invite AWS accounts to become member accounts
  method: POST
  name: create-members
  path: /v1/graphs/{graphArn}/members
- description: Remove member accounts from the behavior graph
  method: DELETE
  name: delete-members
  path: /v1/graphs/{graphArn}/members
- description: List all investigations in a behavior graph
  method: GET
  name: list-investigations
  path: /v1/investigations
- description: Start a new investigation on an IAM user or role
  method: POST
  name: start-investigation
  path: /v1/investigations
- description: Get results and status of an investigation
  method: GET
  name: get-investigation
  path: /v1/investigations/{investigationId}
- description: Archive or reactivate an investigation
  method: PUT
  name: update-investigation-state
  path: /v1/investigations/{investigationId}
- description: Get indicators of compromise from an investigation
  method: GET
  name: list-indicators
  path: /v1/investigations/{investigationId}/indicators
- description: List data source packages in the behavior graph
  method: GET
  name: list-datasource-packages
  path: /v1/datasources
personas: []
provider_name: Amazon Detective
provider_slug: amazon-detective
search_terms:
- list datasource packages
- security operations center analyst using detective to investigate alerts and hunt threats
- initiate a detective investigation on a suspicious iam user or role
- list investigations
- list detective administrator accounts in the organization
- create a new behavior graph
- individual investigation management
- archive a completed investigation or reactivate an archived one
- multi-account security management via aws organizations integration
- create members
- security engineer managing the detective behavior graph, member accounts, and data sources
- list member accounts contributing to the behavior graph
- end-to-end security investigation using machine learning and graph analysis
- managing the detective behavior graph and contributing member accounts
- investigation
- forensics
- invite aws accounts to contribute data to a behavior graph
- soc
- get detailed membership information for specific accounts
- Security Engineer
- invite aws accounts to become member accounts
- list indicators
- create a new amazon detective behavior graph to begin security monitoring
- behavior graph management for security investigation
- get results and status of an investigation
- create graph
- security
- update datasource packages
- get investigation
- get the organization behavior graph configuration including auto-enable settings
- list all security investigations with filtering by severity, status, and state
- delete members
- amazon detective
- security investigation
- end-to-end security investigation workflow for soc analysts
- list graphs
- indicators of compromise from an investigation
- list all behavior graphs
- threat hunting
- data source package management
- get indicators of compromise (ttps, flagged ips, impossible travel) from an investigation
- describe organization configuration
- aws
- archive or reactivate an investigation
- SOC Analyst
- remove member accounts from the behavior graph
- list all amazon detective behavior graphs
- get members
- get the results, severity, and status of a security investigation
- enable additional data source packages like eks audit logs or ad audit logs
- list data source packages and their ingest status in a behavior graph
- start a new investigation on an iam user or role
- security investigation lifecycle management
- list data source packages in the behavior graph
- list all investigations in a behavior graph
- list members
- update investigation state
- member account management for the behavior graph
- get indicators of compromise from an investigation
- start investigation
- list organization admin accounts
- list member accounts contributing data to a behavior graph
- remove member accounts from a behavior graph
slug: security-investigation
tags:
- Amazon Detective
- Security Investigation
- Forensics
- Threat Hunting
- SOC
- AWS
tools:
- description: List all Amazon Detective behavior graphs
  hints:
    openWorld: true
    readOnly: true
  name: list-graphs
- description: Create a new Amazon Detective behavior graph to begin security monitoring
  hints:
    destructive: false
    readOnly: false
  name: create-graph
- description: List member accounts contributing data to a behavior graph
  hints:
    openWorld: true
    readOnly: true
  name: list-members
- description: Get detailed membership information for specific accounts
  hints:
    openWorld: false
    readOnly: true
  name: get-members
- description: Invite AWS accounts to contribute data to a behavior graph
  hints:
    destructive: false
    readOnly: false
  name: create-members
- description: Remove member accounts from a behavior graph
  hints:
    destructive: true
    readOnly: false
  name: delete-members
- description: Initiate a Detective investigation on a suspicious IAM user or role
  hints:
    destructive: false
    readOnly: false
  name: start-investigation
- description: Get the results, severity, and status of a security investigation
  hints:
    openWorld: false
    readOnly: true
  name: get-investigation
- description: List all security investigations with filtering by severity, status, and state
  hints:
    openWorld: true
    readOnly: true
  name: list-investigations
- description: Archive a completed investigation or reactivate an archived one
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: update-investigation-state
- description: Get indicators of compromise (TTPs, flagged IPs, impossible travel) from an investigation
  hints:
    openWorld: true
    readOnly: true
  name: list-indicators
- description: List data source packages and their ingest status in a behavior graph
  hints:
    openWorld: true
    readOnly: true
  name: list-datasource-packages
- description: Enable additional data source packages like EKS audit logs or AD audit logs
  hints:
    destructive: false
    readOnly: false
  name: update-datasource-packages
- description: Get the organization behavior graph configuration including auto-enable settings
  hints:
    openWorld: false
    readOnly: true
  name: describe-organization-configuration
- description: List Detective administrator accounts in the organization
  hints:
    openWorld: true
    readOnly: true
  name: list-organization-admin-accounts
---

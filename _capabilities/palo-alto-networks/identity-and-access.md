---
consumed_apis:
- sase-iam
- sase-tenancy
- sase-subscription
- cloud-identity-engine
description: Unified identity and access management capability for managing service accounts, access policies, roles, tenant service groups, and subscriptions across SASE IAM, Tenancy, and Subscription APIs.
layout: capability
name: Palo Alto Networks Identity and Access Management
operations:
- description: List all service accounts with optional filtering.
  method: GET
  name: list-service-accounts
  path: /v1/service-accounts
- description: Create a new service account.
  method: POST
  name: create-service-account
  path: /v1/service-accounts
- description: Get details of a specific service account.
  method: GET
  name: get-service-account
  path: /v1/service-accounts/{account_id}
- description: Update an existing service account.
  method: PUT
  name: update-service-account
  path: /v1/service-accounts/{account_id}
- description: Delete a service account.
  method: DELETE
  name: delete-service-account
  path: /v1/service-accounts/{account_id}
- description: Generate credentials for a service account.
  method: POST
  name: generate-service-account-credentials
  path: /v1/service-accounts/{account_id}/keys
- description: Revoke a specific key for a service account.
  method: DELETE
  name: revoke-service-account-key
  path: /v1/service-accounts/{account_id}/keys/{key_id}
- description: List all access policies with optional filtering.
  method: GET
  name: list-access-policies
  path: /v1/access-policies
- description: Create a new access policy.
  method: POST
  name: create-access-policy
  path: /v1/access-policies
- description: Get details of a specific access policy.
  method: GET
  name: get-access-policy
  path: /v1/access-policies/{policy_id}
- description: Update an existing access policy.
  method: PUT
  name: update-access-policy
  path: /v1/access-policies/{policy_id}
- description: Delete an access policy.
  method: DELETE
  name: delete-access-policy
  path: /v1/access-policies/{policy_id}
- description: List all available roles.
  method: GET
  name: list-roles
  path: /v1/roles
- description: List all tenant service groups with optional filtering.
  method: GET
  name: list-tenant-service-groups
  path: /v1/tenant-service-groups
- description: Create a new tenant service group.
  method: POST
  name: create-tenant-service-group
  path: /v1/tenant-service-groups
- description: Get details of a specific tenant service group.
  method: GET
  name: get-tenant-service-group
  path: /v1/tenant-service-groups/{tsg_id}
- description: Update an existing tenant service group.
  method: PUT
  name: update-tenant-service-group
  path: /v1/tenant-service-groups/{tsg_id}
- description: Delete a tenant service group.
  method: DELETE
  name: delete-tenant-service-group
  path: /v1/tenant-service-groups/{tsg_id}
- description: List child tenant service groups for a given parent.
  method: GET
  name: list-child-tenant-service-groups
  path: /v1/tenant-service-groups/{tsg_id}/children
- description: List all subscriptions for a tenant service group.
  method: GET
  name: list-subscriptions
  path: /v1/subscriptions
- description: Get details of a specific subscription.
  method: GET
  name: get-subscription
  path: /v1/subscriptions/{subscription_id}
- description: Get entitlements for a specific subscription.
  method: GET
  name: get-subscription-entitlements
  path: /v1/subscriptions/{subscription_id}/entitlements
- description: Allocate licenses from a subscription to tenant service groups.
  method: PUT
  name: allocate-licenses
  path: /v1/subscriptions/{subscription_id}/allocation
personas:
- description: Manages service accounts, roles, and access policies for platform API access.
  id: iam-admin
  name: IAM Administrator
- description: Manages multi-tenant hierarchies and service group configurations for MSSPs.
  id: tenant-operator
  name: Tenant Operator
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- update an existing service account.
- palo alto networks
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- ai security engineer
- access management
- delete an access policy by id.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- investigates security incidents, triages alerts, and coordinates response actions.
- cybersecurity
- get, update, or delete a specific service account.
- delete tenant service group
- get details of a specific service account.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- soar
- manages service accounts, roles, and access policies for platform api access.
- designs and implements network security architectures and policies.
- soc analyst
- list all sase service accounts with optional filtering by tsg.
- conducts automated adversarial testing against ai systems and llm applications.
- sase
- revoke service account key
- sd wan operator
- secure access service edge with remote networking, sd-wan, and zero trust access.
- delete an access policy.
- list all available sase roles.
- vulnerability manager
- list service accounts
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- generate service account credentials
- get, update, or delete a specific access policy.
- get details of a specific access policy by id.
- manage sase access policies.
- get subscription
- list all service accounts with optional filtering.
- researches threat actors, malware campaigns, and vulnerability trends.
- create a new access policy.
- update service account
- list all access policies with optional filtering.
- delete service account
- delete access policy
- mssp operator
- malware researcher
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- incident responder
- cloud identity engine
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- get tenant service group
- list child tenant service groups for a given parent.
- sase admin
- browser security admin
- update an existing access policy.
- list child tenant service groups
- manages multi-tenant security operations at scale for managed service providers.
- list sase subscriptions.
- platform engineer
- get entitlements for a specific subscription.
- cloud security engineer
- create a new service account.
- list tenant service groups
- list all subscriptions for a tenant service group.
- firewall
- network security engineer
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- get service account
- list child tenant service groups.
- monitors and remediates cloud security misconfigurations and compliance violations.
- manages enterprise browser policies and secure browsing configurations.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- compliance team
- create access policy
- allocate licenses from a subscription.
- update tenant service group
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- get access policy
- designs sase and sd-wan network architectures for secure remote access.
- cloud security
- get, update, or delete a specific tenant service group.
- delete a tenant service group.
- cloud security posture management, compliance monitoring, and workload protection.
- allocate licenses
- get details of a specific subscription.
- threat hunter
- data loss prevention, saas security monitoring, and identity security posture.
- iam admin
- sre
- manage sase service accounts.
- manages logging infrastructure, integrations, and platform automation.
- manage sase tenant service groups.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- saas security admin
- secures ai applications with runtime scanning and vulnerability assessment.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- generate credentials for a service account.
- get subscription entitlements
- manage enterprise browser policies, user sessions, and deployments.
- proactively searches for threats and iocs across telemetry data.
- data protection analyst
- manages multi-tenant hierarchies and service group configurations for mssps.
- firewall policy management, network objects, and cloud-native firewall configuration.
- list all available roles.
- threat intel analyst
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- create service account
- ai runtime security scanning and automated red teaming for ai applications.
- get details of a specific access policy.
- create a new sase service account.
- executes containment, eradication, and recovery actions during security incidents.
- compliance officer
- list available sase roles.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- red team operator
- get details of a specific service account by id.
- analyzes suspicious files and samples for malware characteristics.
- allocate licenses from a subscription to tenant service groups.
- threat intelligence
- list all tenant service groups with optional filtering.
- get details of a specific tenant service group.
- update an existing tenant service group.
- tenancy
- create tenant service group
- monitors network health, performance, and digital experience metrics.
- subscription manager
- digital experience monitoring, log management, and best practice assessment.
- update access policy
- network architect
- list access policies
- enterprise it
- revoke a specific key for a service account.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- subscriptions
- network security
- identity
- create a new tenant service group.
- identity and access management, tenant hierarchies, and subscription management.
- delete a service account by id.
- firewall admin
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- list subscriptions
- xdr
- delete a service account.
- list roles
- network operations
- investigates dlp incidents and manages sensitive data protection policies.
- tenant operator
- enterprise browser policy management and secure browsing.
slug: identity-and-access
tags:
- Palo Alto Networks
- Identity
- Access Management
- Tenancy
- Subscriptions
- Cloud Identity Engine
tools:
- description: List all SASE service accounts with optional filtering by TSG.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-service-accounts
- description: Create a new SASE service account.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-service-account
- description: Get details of a specific service account by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-service-account
- description: Update an existing service account.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-service-account
- description: Delete a service account by ID.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-service-account
- description: Generate credentials for a service account.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: generate-service-account-credentials
- description: Revoke a specific key for a service account.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: revoke-service-account-key
- description: List all access policies with optional filtering.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-access-policies
- description: Create a new access policy.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-access-policy
- description: Get details of a specific access policy by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-access-policy
- description: Update an existing access policy.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-access-policy
- description: Delete an access policy by ID.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-access-policy
- description: List all available SASE roles.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-roles
- description: List all tenant service groups with optional filtering.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-tenant-service-groups
- description: Create a new tenant service group.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-tenant-service-group
- description: Get details of a specific tenant service group.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-tenant-service-group
- description: Update an existing tenant service group.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-tenant-service-group
- description: Delete a tenant service group.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-tenant-service-group
- description: List child tenant service groups for a given parent.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-child-tenant-service-groups
- description: List all subscriptions for a tenant service group.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-subscriptions
- description: Get details of a specific subscription.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-subscription
- description: Get entitlements for a specific subscription.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-subscription-entitlements
- description: Allocate licenses from a subscription to tenant service groups.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: allocate-licenses
---

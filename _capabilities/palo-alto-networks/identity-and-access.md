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
- palo alto networks
- get details of a specific tenant service group.
- revoke service account key
- designs sase and sd-wan network architectures for secure remote access.
- network security engineer
- secures ai applications with runtime scanning and vulnerability assessment.
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- list tenant service groups
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- manage sase tenant service groups.
- update an existing tenant service group.
- get access policy
- list available sase roles.
- get, update, or delete a specific service account.
- list child tenant service groups for a given parent.
- xdr
- update access policy
- delete a tenant service group.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- create a new access policy.
- get entitlements for a specific subscription.
- list child tenant service groups.
- allocate licenses from a subscription to tenant service groups.
- delete an access policy by id.
- create a new service account.
- identity
- enterprise browser policy management and secure browsing.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- update an existing service account.
- update an existing access policy.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- ai security engineer
- list all access policies with optional filtering.
- data protection analyst
- network architect
- data loss prevention, saas security monitoring, and identity security posture.
- saas security admin
- generate credentials for a service account.
- revoke a specific key for a service account.
- list service accounts
- manages multi-tenant hierarchies and service group configurations for mssps.
- network security
- soar
- manages enterprise browser policies and secure browsing configurations.
- list all tenant service groups with optional filtering.
- delete an access policy.
- compliance team
- update tenant service group
- investigates dlp incidents and manages sensitive data protection policies.
- researches threat actors, malware campaigns, and vulnerability trends.
- subscription manager
- compliance officer
- delete access policy
- get details of a specific service account by id.
- list all sase service accounts with optional filtering by tsg.
- tenant operator
- executes containment, eradication, and recovery actions during security incidents.
- vulnerability manager
- access management
- list all subscriptions for a tenant service group.
- cybersecurity
- subscriptions
- malware researcher
- designs and implements network security architectures and policies.
- list subscriptions
- allocate licenses from a subscription.
- incident responder
- get, update, or delete a specific access policy.
- create a new sase service account.
- generate service account credentials
- mssp operator
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- get details of a specific service account.
- manages service accounts, roles, and access policies for platform api access.
- update service account
- threat intel analyst
- firewall policy management, network objects, and cloud-native firewall configuration.
- sase
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- cloud identity engine
- tenancy
- soc analyst
- firewall admin
- proactively searches for threats and iocs across telemetry data.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- allocate licenses
- get tenant service group
- create tenant service group
- network operations
- enterprise it
- manages logging infrastructure, integrations, and platform automation.
- create a new tenant service group.
- browser security admin
- threat hunter
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- create service account
- list all available roles.
- manage sase access policies.
- delete a service account by id.
- analyzes suspicious files and samples for malware characteristics.
- monitors and remediates cloud security misconfigurations and compliance violations.
- monitors network health, performance, and digital experience metrics.
- identity and access management, tenant hierarchies, and subscription management.
- get subscription
- ai runtime security scanning and automated red teaming for ai applications.
- list all service accounts with optional filtering.
- list child tenant service groups
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- list access policies
- platform engineer
- digital experience monitoring, log management, and best practice assessment.
- iam admin
- get details of a specific access policy by id.
- get service account
- get, update, or delete a specific tenant service group.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- list roles
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- get subscription entitlements
- list sase subscriptions.
- red team operator
- delete service account
- list all available sase roles.
- get details of a specific access policy.
- delete tenant service group
- sre
- manages multi-tenant security operations at scale for managed service providers.
- threat intelligence
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- conducts automated adversarial testing against ai systems and llm applications.
- firewall
- investigates security incidents, triages alerts, and coordinates response actions.
- cloud security
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- cloud security posture management, compliance monitoring, and workload protection.
- manage enterprise browser policies, user sessions, and deployments.
- manage sase service accounts.
- get details of a specific subscription.
- cloud security engineer
- create access policy
- sd wan operator
- delete a service account.
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

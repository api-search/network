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
- subscriptions
- secures ai applications with runtime scanning and vulnerability assessment.
- list child tenant service groups
- allocate licenses
- list child tenant service groups for a given parent.
- xdr
- vulnerability manager
- soar
- update tenant service group
- delete service account
- network security engineer
- get tenant service group
- list all available sase roles.
- get subscription
- manages service accounts, roles, and access policies for platform api access.
- list sase subscriptions.
- get, update, or delete a specific access policy.
- manage sase access policies.
- list all access policies with optional filtering.
- threat hunter
- browser security admin
- soc analyst
- platform engineer
- create service account
- manages logging infrastructure, integrations, and platform automation.
- delete access policy
- network architect
- digital experience monitoring, log management, and best practice assessment.
- saas security admin
- tenant operator
- tenancy
- manage sase service accounts.
- identity and access management, tenant hierarchies, and subscription management.
- update an existing service account.
- ai security engineer
- iam admin
- subscription manager
- network operations
- monitors network health, performance, and digital experience metrics.
- manages multi-tenant security operations at scale for managed service providers.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- get service account
- update an existing tenant service group.
- list service accounts
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- list tenant service groups
- sase
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- list all sase service accounts with optional filtering by tsg.
- revoke a specific key for a service account.
- delete a service account by id.
- firewall
- network security
- designs sase and sd-wan network architectures for secure remote access.
- list all subscriptions for a tenant service group.
- revoke service account key
- researches threat actors, malware campaigns, and vulnerability trends.
- enterprise it
- create a new access policy.
- get details of a specific access policy.
- delete an access policy by id.
- allocate licenses from a subscription.
- delete an access policy.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- generate credentials for a service account.
- create a new service account.
- allocate licenses from a subscription to tenant service groups.
- incident responder
- identity
- create a new tenant service group.
- cloud security posture management, compliance monitoring, and workload protection.
- list available sase roles.
- designs and implements network security architectures and policies.
- conducts automated adversarial testing against ai systems and llm applications.
- delete a tenant service group.
- get details of a specific subscription.
- list roles
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- cybersecurity
- threat intel analyst
- monitors and remediates cloud security misconfigurations and compliance violations.
- delete tenant service group
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- get entitlements for a specific subscription.
- manages enterprise browser policies and secure browsing configurations.
- cloud security
- delete a service account.
- proactively searches for threats and iocs across telemetry data.
- update an existing access policy.
- firewall admin
- get details of a specific tenant service group.
- list all service accounts with optional filtering.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- get access policy
- get details of a specific service account.
- get details of a specific access policy by id.
- data protection analyst
- red team operator
- firewall policy management, network objects, and cloud-native firewall configuration.
- sd wan operator
- investigates security incidents, triages alerts, and coordinates response actions.
- manage sase tenant service groups.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- update service account
- create tenant service group
- executes containment, eradication, and recovery actions during security incidents.
- generate service account credentials
- list child tenant service groups.
- manages multi-tenant hierarchies and service group configurations for mssps.
- create access policy
- list all tenant service groups with optional filtering.
- manage enterprise browser policies, user sessions, and deployments.
- analyzes suspicious files and samples for malware characteristics.
- list access policies
- access management
- mssp operator
- sre
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- ai runtime security scanning and automated red teaming for ai applications.
- create a new sase service account.
- malware researcher
- compliance team
- get, update, or delete a specific service account.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- data loss prevention, saas security monitoring, and identity security posture.
- threat intelligence
- list subscriptions
- palo alto networks
- update access policy
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- list all available roles.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- cloud security engineer
- get subscription entitlements
- get, update, or delete a specific tenant service group.
- get details of a specific service account by id.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- compliance officer
- cloud identity engine
- investigates dlp incidents and manages sensitive data protection policies.
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

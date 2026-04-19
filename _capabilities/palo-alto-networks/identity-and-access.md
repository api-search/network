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
- get service account
- enterprise it
- list all service accounts with optional filtering.
- list service accounts
- create access policy
- compliance officer
- list child tenant service groups.
- data protection analyst
- designs sase and sd-wan network architectures for secure remote access.
- delete an access policy by id.
- create a new sase service account.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- list tenant service groups
- malware researcher
- ai runtime security scanning and automated red teaming for ai applications.
- network security
- researches threat actors, malware campaigns, and vulnerability trends.
- manages enterprise browser policies and secure browsing configurations.
- cloud security posture management, compliance monitoring, and workload protection.
- list child tenant service groups for a given parent.
- list available sase roles.
- delete a tenant service group.
- manage sase service accounts.
- list child tenant service groups
- create a new access policy.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- proactively searches for threats and iocs across telemetry data.
- list all sase service accounts with optional filtering by tsg.
- platform engineer
- cloud identity engine
- delete a service account by id.
- get, update, or delete a specific access policy.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- analyzes suspicious files and samples for malware characteristics.
- delete tenant service group
- firewall policy management, network objects, and cloud-native firewall configuration.
- list all available sase roles.
- monitors network health, performance, and digital experience metrics.
- vulnerability manager
- list access policies
- update an existing service account.
- manages multi-tenant security operations at scale for managed service providers.
- conducts automated adversarial testing against ai systems and llm applications.
- manages logging infrastructure, integrations, and platform automation.
- access management
- get details of a specific access policy.
- get entitlements for a specific subscription.
- list roles
- compliance team
- designs and implements network security architectures and policies.
- manages multi-tenant hierarchies and service group configurations for mssps.
- get, update, or delete a specific service account.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- create a new tenant service group.
- saas security admin
- tenant operator
- incident responder
- list all tenant service groups with optional filtering.
- generate service account credentials
- secure access service edge with remote networking, sd-wan, and zero trust access.
- get details of a specific service account.
- cloud security engineer
- tenancy
- manage sase tenant service groups.
- list all subscriptions for a tenant service group.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- get access policy
- get details of a specific subscription.
- firewall
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- sase
- sd wan operator
- threat intel analyst
- manage enterprise browser policies, user sessions, and deployments.
- list all access policies with optional filtering.
- delete service account
- network operations
- manages service accounts, roles, and access policies for platform api access.
- threat hunter
- get details of a specific tenant service group.
- cybersecurity
- revoke service account key
- get, update, or delete a specific tenant service group.
- firewall admin
- list subscriptions
- soc analyst
- create service account
- mssp operator
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- identity and access management, tenant hierarchies, and subscription management.
- monitors and remediates cloud security misconfigurations and compliance violations.
- get tenant service group
- browser security admin
- sase admin
- create a new service account.
- threat intelligence
- palo alto networks
- identity
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- delete an access policy.
- generate credentials for a service account.
- soar
- investigates security incidents, triages alerts, and coordinates response actions.
- update tenant service group
- cloud security
- update an existing tenant service group.
- network architect
- delete a service account.
- allocate licenses
- executes containment, eradication, and recovery actions during security incidents.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- ai security engineer
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- list sase subscriptions.
- sre
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- network security engineer
- list all available roles.
- iam admin
- update service account
- data loss prevention, saas security monitoring, and identity security posture.
- digital experience monitoring, log management, and best practice assessment.
- secures ai applications with runtime scanning and vulnerability assessment.
- update an existing access policy.
- red team operator
- get details of a specific access policy by id.
- get details of a specific service account by id.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- get subscription entitlements
- enterprise browser policy management and secure browsing.
- manage sase access policies.
- allocate licenses from a subscription to tenant service groups.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- update access policy
- revoke a specific key for a service account.
- allocate licenses from a subscription.
- get subscription
- investigates dlp incidents and manages sensitive data protection policies.
- subscription manager
- delete access policy
- create tenant service group
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- subscriptions
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
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

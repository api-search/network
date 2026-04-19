---
description: An Anypoint Platform organization or business group. Organizations are the top-level containers that hold all platform resources including users, environments, and deployed applications.
layout: schema
name: Organization
properties_list:
- description: Unique identifier of the organization
  name: id
  type: string
- description: Display name of the organization
  name: name
  type: string
- description: Timestamp when the organization was created
  name: createdAt
  type: string
- description: Timestamp when the organization was last updated
  name: updatedAt
  type: string
- description: User ID of the organization owner
  name: ownerId
  type: string
- description: Client ID for the organization used in API authentication
  name: clientId
  type: string
- description: Identity provider ID if external identity management is configured
  name: idprovider_id
  type: string
- description: Whether the organization uses federated identity management
  name: isFederated
  type: boolean
- description: IDs of parent organizations in the business group hierarchy
  name: parentOrganizationIds
  type: array
- description: IDs of child business groups
  name: subOrganizationIds
  type: array
- description: IDs of tenant organizations
  name: tenantOrganizationIds
  type: array
- description: Whether multi-factor authentication is required
  name: mfaRequired
  type: boolean
- description: Whether automatic admin promotion is disabled
  name: isAutomaticAdminPromotionExempt
  type: boolean
- description: Domain associated with the organization
  name: domain
  type: string
- description: Whether this is the root (master) organization
  name: isMaster
  type: boolean
- description: Environments belonging to this organization
  name: environments
  type: array
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-organization-schema.json
slug: mulesoft-anypoint-platform-organization
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: Organization
---

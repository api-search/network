---
description: Represents an organization in Workday. Organizations include supervisory organizations, cost centers, companies, regions, and other organizational types used to structure the enterprise.
layout: schema
name: Organization
properties_list:
- description: The Workday ID of the organization.
  name: id
  type: string
- description: A display descriptor for the organization.
  name: descriptor
  type: string
- description: The name of the organization.
  name: name
  type: string
- description: The organization reference ID or code.
  name: code
  type: string
- description: The type of organization (e.g., Supervisory, Cost Center, Company, Region).
  name: organizationType
  type: object
- description: The sub-type of the organization.
  name: organizationSubType
  type: object
- description: The parent organization in the hierarchy.
  name: superiorOrganization
  type: object
- description: The manager of the organization.
  name: manager
  type: object
- description: The primary location of the organization.
  name: location
  type: object
- description: The staffing model (e.g., Position Management, Job Management).
  name: staffingModel
  type: string
- description: The number of members in the organization.
  name: memberCount
  type: integer
- description: Subordinate organizations in the hierarchy.
  name: subordinateOrganizations
  type: array
- description: Positions within this organization.
  name: positions
  type: array
- description: Workers assigned to this organization.
  name: workers
  type: array
- description: Whether the organization is inactive.
  name: isInactive
  type: boolean
- description: Whether to include inactive subordinate organizations.
  name: includeInactiveSubOrganizations
  type: boolean
- description: The date the organization becomes available.
  name: availabilityDate
  type:
  - string
  - 'null'
- description: The last time the organization was updated.
  name: lastUpdated
  type: string
- description: An external system identifier for the organization.
  name: externalID
  type: string
- description: A link to the full organization resource.
  name: href
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/organization.json
slug: organization
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Organization
---

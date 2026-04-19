---
description: Schema defining the structure of an AWS Organization resource, including accounts, organizational units, policies, and the organization hierarchy.
layout: schema
name: AWS Organizations Definition
properties_list:
- description: The unique identifier of the organization.
  name: Id
  type: string
- description: The Amazon Resource Name of the organization.
  name: Arn
  type: string
- description: Specifies the functionality available to the organization.
  name: FeatureSet
  type: string
- description: The ARN of the management account.
  name: MasterAccountArn
  type: string
- description: The unique identifier of the management account.
  name: MasterAccountId
  type: string
- description: The email address associated with the management account.
  name: MasterAccountEmail
  type: string
- description: A list of policy types enabled for the organization.
  name: AvailablePolicyTypes
  type: array
- description: The member accounts in the organization.
  name: Accounts
  type: array
- description: The organizational units in the organization.
  name: OrganizationalUnits
  type: array
- description: The policies attached in the organization.
  name: Policies
  type: array
- description: The root containers in the organization.
  name: Roots
  type: array
provider_name: Amazon Organizations
provider_slug: amazon-organizations
schema_file: json-schema/amazon-organizations-schema.json
slug: amazon-organizations
tags:
- Account Management
- AWS
- Consolidated Billing
- Governance
- Multi-Account
- Organizations
- Policies
title: AWS Organizations Definition
---

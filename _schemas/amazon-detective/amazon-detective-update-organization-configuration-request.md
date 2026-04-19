---
description: Request to update organization configuration
layout: schema
name: UpdateOrganizationConfigurationRequest
properties_list:
- description: The ARN of the organization behavior graph.
  name: GraphArn
  type: string
- description: Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.
  name: AutoEnable
  type: boolean
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-update-organization-configuration-request-schema.json
slug: amazon-detective-update-organization-configuration-request
tags:
- AWS
- Forensics
- Investigation
- Security
title: UpdateOrganizationConfigurationRequest
---

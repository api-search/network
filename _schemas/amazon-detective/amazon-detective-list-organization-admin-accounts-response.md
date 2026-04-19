---
description: Response from listing organization admin accounts
layout: schema
name: ListOrganizationAdminAccountsResponse
properties_list:
- description: The list of delegated administrator accounts.
  name: Administrators
  type: array
- description: If there are more accounts remaining in the results, then this is the pagination token.
  name: NextToken
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-list-organization-admin-accounts-response-schema.json
slug: amazon-detective-list-organization-admin-accounts-response
tags:
- AWS
- Forensics
- Investigation
- Security
title: ListOrganizationAdminAccountsResponse
---

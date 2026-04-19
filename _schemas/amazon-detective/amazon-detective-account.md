---
description: An AWS account to invite to become a member account in a behavior graph
layout: schema
name: Account
properties_list:
- description: The account identifier of the AWS account.
  name: AccountId
  type: string
- description: The AWS account root user email address for the AWS account.
  name: EmailAddress
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-account-schema.json
slug: amazon-detective-account
tags:
- AWS
- Forensics
- Investigation
- Security
title: Account
---

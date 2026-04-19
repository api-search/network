---
description: A member account that could not be processed
layout: schema
name: UnprocessedAccount
properties_list:
- description: The AWS account identifier of the member account that was not processed.
  name: AccountId
  type: string
- description: The reason that the member account request could not be processed.
  name: Reason
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-unprocessed-account-schema.json
slug: amazon-detective-unprocessed-account
tags:
- AWS
- Forensics
- Investigation
- Security
title: UnprocessedAccount
---

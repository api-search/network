---
description: Represents a B2B Data Interchange profile — the system-side resource that represents your EDI sender or receiver entity.
layout: schema
name: Profile
properties_list:
- description: Unique identifier for the profile
  name: profileId
  type: string
- description: Amazon Resource Name (ARN) for the profile
  name: profileArn
  type: string
- description: Name of the profile
  name: name
  type: string
- description: Legal business name of the organization
  name: businessName
  type: string
- description: Phone number for the profile contact
  name: phone
  type: string
- description: Email address for the profile contact
  name: email
  type: string
- description: Whether CloudWatch logging is enabled for this profile
  name: logging
  type: string
- description: CloudWatch log group name for this profile
  name: logGroupName
  type: string
- description: Timestamp when the profile was created
  name: createdAt
  type: string
- description: Timestamp when the profile was last modified
  name: modifiedAt
  type: string
provider_name: Amazon B2B Data Interchange
provider_slug: amazon-b2b-data-interchange
schema_file: json-schema/profile.json
slug: profile
tags:
- EDI
- B2B
- Data Interchange
- Supply Chain
- Healthcare
- Financial Services
- Amazon Web Services
- AWS
title: Profile
---

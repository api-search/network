---
description: Organization Config rule creation or deletion status in each member account. This includes the name of the rule, the status, error code and error message when the rule creation or deletion failed.
layout: schema
name: MemberAccountStatus
properties_list:
- description: ''
  name: AccountId
  type: object
- description: ''
  name: ConfigRuleName
  type: object
- description: ''
  name: MemberAccountRuleStatus
  type: object
- description: ''
  name: ErrorCode
  type: object
- description: ''
  name: ErrorMessage
  type: object
- description: ''
  name: LastUpdateTime
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-member-account-status-schema.json
slug: config-member-account-status
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: MemberAccountStatus
---

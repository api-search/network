---
description: Attributes of a NetBackup backup policy
layout: schema
name: PolicyAttributes
properties_list:
- description: Unique name of the policy
  name: policyName
  type: string
- description: The policy type defining the type of backup
  name: policyType
  type: string
- description: Whether the policy is currently active
  name: active
  type: boolean
- description: Date and time the policy becomes effective
  name: effectiveDate
  type: string
- description: Arguments for snapshot method if applicable
  name: snapshotMethodArgs
  type: string
- description: ''
  name: backupCopies
  type: object
- description: Job priority for this policy
  name: priority
  type: integer
- description: Keyword tag for the policy
  name: keyword
  type: string
- description: Data classification associated with this policy
  name: dataClassification
  type: string
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
schema_file: json-schema/veritas-netbackup-rest-policy-attributes-schema.json
slug: veritas-netbackup-rest-policy-attributes
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
title: PolicyAttributes
---

---
description: Details about a member account in a behavior graph
layout: schema
name: MemberDetail
properties_list:
- description: The AWS account identifier of the member account.
  name: AccountId
  type: string
- description: The AWS account root user email address for the member account.
  name: EmailAddress
  type: string
- description: The ARN of the behavior graph that the member account was invited to.
  name: GraphArn
  type: string
- description: The AWS account identifier of the administrator account for the behavior graph.
  name: AdministratorId
  type: string
- description: The current membership status of the member account.
  name: Status
  type: string
- description: The date and time that Detective sent the invitation to the member account.
  name: InvitedTime
  type: string
- description: The date and time that the member account was last updated.
  name: UpdatedTime
  type: string
- description: Data volume in bytes per day for the member account.
  name: VolumeUsageInBytes
  type: integer
- description: The data and time when the member account data volume was last updated.
  name: VolumeUsageUpdatedTime
  type: string
- description: The member account data volume as a percentage of the maximum allowed data volume.
  name: PercentOfGraphUtilization
  type: number
- description: For member accounts with a status of ACCEPTED_BUT_DISABLED, the reason the member account is not enabled.
  name: DisabledReason
  type: string
- description: The type of behavior graph membership.
  name: InvitationType
  type: string
provider_name: Amazon Detective
provider_slug: amazon-detective
schema_file: json-schema/amazon-detective-member-detail-schema.json
slug: amazon-detective-member-detail
tags:
- AWS
- Forensics
- Investigation
- Security
title: MemberDetail
---

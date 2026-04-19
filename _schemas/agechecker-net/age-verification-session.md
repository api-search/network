---
description: Session schema from AgeChecker.Net API
layout: schema
name: Session
properties_list:
- description: Unique session identifier.
  name: session_id
  type: string
- description: Current session status.
  name: status
  type: string
- description: Verification result.
  name: result
  type: string
- description: Whether age was verified.
  name: age_verified
  type: boolean
- description: Whether photo ID was required.
  name: requires_photo_id
  type: boolean
- description: When the session was created.
  name: created_at
  type: string
- description: When the session was completed.
  name: completed_at
  type: string
provider_name: AgeChecker.Net
provider_slug: agechecker-net
schema_file: json-schema/age-verification-session-schema.json
slug: age-verification-session
tags:
- Age Verification
- Identity
- Compliance
- Regulatory
- E-Commerce
title: Session
---

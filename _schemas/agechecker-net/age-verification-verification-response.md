---
description: VerificationResponse schema from AgeChecker.Net API
layout: schema
name: VerificationResponse
properties_list:
- description: Verification outcome.
  name: result
  type: string
- description: Unique session identifier for this verification.
  name: session_id
  type: string
- description: Whether the customer must upload a photo ID to complete verification.
  name: requires_photo_id
  type: boolean
- description: Whether age was successfully verified.
  name: age_verified
  type: boolean
- description: The minimum age threshold checked.
  name: minimum_age
  type: integer
- description: URL to redirect customer if photo ID is required.
  name: redirect_url
  type: string
provider_name: AgeChecker.Net
provider_slug: agechecker-net
schema_file: json-schema/age-verification-verification-response-schema.json
slug: age-verification-verification-response
tags:
- Age Verification
- Identity
- Compliance
- Regulatory
- E-Commerce
title: VerificationResponse
---

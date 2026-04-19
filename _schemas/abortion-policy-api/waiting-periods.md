---
description: Abortion waiting period restrictions in a US state, covering mandatory time between counseling and abortion care.
layout: schema
name: WaitingPeriods
properties_list:
- description: Hours a person must wait between receiving state-mandated counseling and obtaining abortion. Null means no waiting period.
  name: waiting_period_hours
  type: integer
- description: 1=counseling required by state; 2=counseling must be at the facility, requiring two clinic trips.
  name: counseling_visits
  type: integer
- description: Conditions under which waiting period may be waived.
  name: exception_health
  type: string
- description: Additional notes on unusual waiting period policies.
  name: waiting_period_notes
  type: string
- description: Conditions under which counseling requirement can be waived.
  name: counseling_waived_condition
  type: string
- description: Date this policy record was last updated.
  name: Last Updated
  type: string
provider_name: Abortion Policy API
provider_slug: abortion-policy-api
schema_file: json-schema/waiting-periods-schema.json
slug: waiting-periods
tags:
- Abortion
- Policies
- Healthcare
- Government
title: WaitingPeriods
---

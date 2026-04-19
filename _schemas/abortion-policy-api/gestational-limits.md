---
description: Abortion restrictions related to gestational limits (bans after certain weeks of pregnancy) for a US state or territory.
layout: schema
name: GestationalLimits
properties_list:
- description: Weeks since Last Menstrual Period (LMP) after which abortion is banned. Null means no gestational restriction. 99 means viability standard. 28 means third trimester ban. 0 means complete ban.
  name: banned_after_weeks_since_LMP
  type: integer
- description: If true, abortion is permitted when necessary to save the pregnant person's life.
  name: exception_life
  type: boolean
- description: Health exception type. "Physical" (excluding mental health), "Any" (may include mental health), or "Major Bodily Function" (substantial irreversible impairment).
  name: exception_health
  type: string
- description: Fetal anomaly exception type. "Serious fetal anomaly" or "Lethal fetal anomaly".
  name: exception_fetal
  type: string
- description: If true, exceptions may be granted in cases of rape or incest.
  name: exception_rape_or_incest
  type: boolean
- description: Date this policy record was last updated.
  name: Last Updated
  type: string
provider_name: Abortion Policy API
provider_slug: abortion-policy-api
schema_file: json-schema/gestational-limits-schema.json
slug: gestational-limits
tags:
- Abortion
- Policies
- Healthcare
- Government
title: GestationalLimits
---

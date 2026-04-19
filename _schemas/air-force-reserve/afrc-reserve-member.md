---
description: An Air Force Reserve member record
layout: schema
name: ReserveMember
properties_list:
- description: Military service number or SSAN
  name: service_number
  type: string
- description: Military rank
  name: rank
  type: string
- description: Member last name
  name: last_name
  type: string
- description: Member first name
  name: first_name
  type: string
- description: Assigned reserve unit
  name: unit
  type: string
- description: Air Force Specialty Code (career field)
  name: afsc
  type: string
- description: Current duty status
  name: duty_status
  type: string
- description: Date of enlistment
  name: enlistment_date
  type: string
provider_name: Air Force Reserve
provider_slug: air-force-reserve
schema_file: json-schema/afrc-reserve-member-schema.json
slug: afrc-reserve-member
tags:
- Federal Government
- Military
- Defense
- Air Force
- United States Government
title: ReserveMember
---

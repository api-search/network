---
description: An equipment reservation at a core facility.
layout: schema
name: Reservation
properties_list:
- description: Unique identifier for the reservation.
  name: id
  type: integer
- description: Name of the reserved equipment.
  name: equipment_name
  type: string
- description: Reservation start time (ISO 8601).
  name: start_time
  type: string
- description: Reservation end time (ISO 8601).
  name: end_time
  type: string
- description: Username of the person who made the reservation.
  name: user
  type: string
provider_name: agilent-technologies
provider_slug: agilent-technologies
schema_file: json-schema/ilab-operations-api-reservation-schema.json
slug: ilab-operations-api-reservation
tags:
- Life Sciences
- Diagnostics
- Laboratory
- Scientific Instruments
- LIMS
- Laboratory Automation
title: Reservation
---

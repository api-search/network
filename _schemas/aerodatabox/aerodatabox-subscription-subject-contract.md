---
description: Describes subscription subject
layout: schema
name: SubscriptionSubjectContract
properties_list:
- description: ''
  name: type
  type: object
- description: Subject ID of a subscription. Complements SubjectType. E.g. SubjectType = "FlightNumber" and SubjectId = "DL 47" means that this subscription is for all updates of flight with number DL47.
  name: id
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-subscription-subject-contract-schema.json
slug: aerodatabox-subscription-subject-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: SubscriptionSubjectContract
---

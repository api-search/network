---
description: Represents a position in Workday. A position defines a role within a supervisory organization and can be filled by a worker.
layout: schema
name: Position
properties_list:
- description: The Workday ID of the position.
  name: id
  type: string
- description: A display descriptor for the position.
  name: descriptor
  type: string
- description: The position reference ID (e.g., P-00001).
  name: positionID
  type: string
- description: The job profile associated with this position.
  name: jobProfile
  type: object
- description: The name of the job profile.
  name: jobProfileName
  type: string
- description: The business title for this position.
  name: businessTitle
  type: string
- description: The supervisory organization this position belongs to.
  name: supervisoryOrganization
  type: object
- description: The worker currently filling this position, if any.
  name: worker
  type: object
- description: The time type for the position (e.g., Full Time, Part Time).
  name: positionTimeType
  type: object
- description: The worker type for this position (e.g., Employee, Contingent Worker).
  name: workerType
  type: object
- description: The worker sub-type for the position.
  name: workerSubType
  type: object
- description: The primary work location for the position.
  name: location
  type: object
- description: The compensation grade associated with this position.
  name: compensationGrade
  type: object
- description: The pay rate type (e.g., Salary, Hourly).
  name: payRateType
  type: object
- description: Whether the position is currently filled by a worker.
  name: isFilled
  type: boolean
- description: Whether the position is available for recruiting.
  name: isAvailableForRecruit
  type: boolean
- description: Whether the position has been closed.
  name: isClosed
  type: boolean
- description: Whether the position is frozen.
  name: isFrozen
  type: boolean
- description: The headcount for this position.
  name: headcountCount
  type: integer
- description: The date the position becomes available.
  name: availableDate
  type:
  - string
  - 'null'
- description: The earliest allowed hire date.
  name: earliestHireDate
  type:
  - string
  - 'null'
- description: A link to the full position resource.
  name: href
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/position.json
slug: position
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Position
---

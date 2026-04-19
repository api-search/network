---
description: A time-boxed iteration in agile delivery during which a team completes a set of planned work items.
layout: schema
name: Sprint
properties_list:
- description: Unique identifier for the sprint.
  name: id
  type: string
- description: Human-readable name of the sprint.
  name: name
  type: string
- description: The sprint goal agreed on during sprint planning.
  name: goal
  type: string
- description: Sprint start date.
  name: start_date
  type: string
- description: Sprint end date.
  name: end_date
  type: string
- description: Story points completed in the sprint.
  name: velocity
  type: integer
- description: ''
  name: status
  type: string
provider_name: Agile Delivery
provider_slug: agile-delivery
schema_file: json-schema/agile-delivery-sprint-schema.json
slug: agile-delivery-sprint
tags:
- Agile
- Iterative Development
- Project Management
- Software Development
- Sprint
- Scrum
title: Sprint
---

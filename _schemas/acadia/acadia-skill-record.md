---
description: A skill record in the employee skills matrix
layout: schema
name: SkillRecord
properties_list:
- description: Unique skill identifier
  name: skillId
  type: string
- description: Skill name
  name: name
  type: string
- description: Whether this skill is required for the role
  name: required
  type: boolean
- description: Whether the employee has completed this skill
  name: completed
  type: boolean
- description: When the skill was completed
  name: completedAt
  type: string
- description: Score achieved (0-100)
  name: score
  type: integer
provider_name: Acadia
provider_slug: acadia
schema_file: json-schema/acadia-skill-record-schema.json
slug: acadia-skill-record
tags:
- Connected Worker
- Knowledge Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
title: SkillRecord
---

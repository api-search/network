---
description: An entry in the Helix Swarm activity stream recording an action performed by a user.
layout: schema
name: Activity
properties_list:
- description: The unique activity entry identifier.
  name: id
  type: integer
- description: A past-tense description of the action performed.
  name: action
  type: string
- description: The related changelist ID, if applicable.
  name: change
  type: integer
- description: The date and time the activity occurred.
  name: date
  type: string
- description: Contextual information about the activity.
  name: description
  type: string
- description: A URL linking to the activity target.
  name: link
  type: string
- description: The activity streams this entry appears in.
  name: streams
  type: array
- description: The object that received the action.
  name: target
  type: string
- description: An associated comment thread topic.
  name: topic
  type: string
- description: The activity type classification.
  name: type
  type: string
- description: The username of the user who performed the action.
  name: user
  type: string
provider_name: Perforce
provider_slug: perforce
schema_file: json-schema/perforce-helix-swarm-activity-schema.json
slug: perforce-helix-swarm-activity
tags: []
title: Activity
---

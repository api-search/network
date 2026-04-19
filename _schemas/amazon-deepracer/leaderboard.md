---
description: A DeepRacer racing leaderboard where participants submit model performances.
layout: schema
name: Leaderboard
properties_list:
- description: The ARN uniquely identifying the leaderboard.
  name: arn
  type: string
- description: The display name of the leaderboard.
  name: name
  type: string
- description: Current status.
  name: status
  type: string
- description: Timestamp when submissions close.
  name: submissionClosureTime
  type: string
- description: Whether this leaderboard qualifies participants for championship events.
  name: isQualifier
  type: boolean
- description: The type of track used for this leaderboard.
  name: trackType
  type: string
- description: Minimum number of consecutive laps required.
  name: minimumCountOfLaps
  type: integer
provider_name: Amazon DeepRacer
provider_slug: amazon-deepracer
schema_file: json-schema/leaderboard-schema.json
slug: leaderboard
tags:
- Autonomous Vehicles
- AWS
- Machine Learning
- Reinforcement Learning
- Robotics
title: Leaderboard
---

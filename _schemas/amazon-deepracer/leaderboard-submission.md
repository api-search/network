---
description: A participant's submission to a DeepRacer leaderboard including race performance.
layout: schema
name: LeaderboardSubmission
properties_list:
- description: Unique identifier for this submission.
  name: leaderboardSubmissionId
  type: string
- description: The participant's alias or username.
  name: participantName
  type: string
- description: The ARN of the model submitted for evaluation.
  name: modelArn
  type: string
- description: The participant's current rank on the leaderboard.
  name: rank
  type: integer
- description: The participant's best single lap time in seconds.
  name: lapTime
  type: number
- description: The participant's average lap time.
  name: avgLapTime
  type: number
provider_name: Amazon DeepRacer
provider_slug: amazon-deepracer
schema_file: json-schema/leaderboard-submission-schema.json
slug: leaderboard-submission
tags:
- Autonomous Vehicles
- AWS
- Machine Learning
- Reinforcement Learning
- Robotics
title: LeaderboardSubmission
---

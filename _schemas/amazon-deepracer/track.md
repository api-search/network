---
description: A virtual or physical racing track used for DeepRacer training and evaluation.
layout: schema
name: Track
properties_list:
- description: The ARN uniquely identifying the racing track.
  name: arn
  type: string
- description: The display name of the track.
  name: name
  type: string
- description: The classification type of the track.
  name: trackType
  type: string
- description: The size category of the track.
  name: trackDimension
  type: string
provider_name: Amazon DeepRacer
provider_slug: amazon-deepracer
schema_file: json-schema/track-schema.json
slug: track
tags:
- Autonomous Vehicles
- AWS
- Machine Learning
- Reinforcement Learning
- Robotics
title: Track
---

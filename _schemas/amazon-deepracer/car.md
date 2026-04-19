---
description: A physical DeepRacer vehicle registered to an AWS account.
layout: schema
name: Car
properties_list:
- description: The ARN uniquely identifying the DeepRacer vehicle.
  name: vehicleArn
  type: string
- description: The display name of the vehicle.
  name: vehicleName
  type: string
- description: The ARN of the fleet this vehicle belongs to.
  name: fleetArn
  type: string
- description: Timestamp when the vehicle was registered.
  name: createdAt
  type: string
- description: Timestamp when the vehicle was last updated.
  name: lastModifiedTime
  type: string
- description: Tags associated with the vehicle.
  name: tagsList
  type: array
provider_name: Amazon DeepRacer
provider_slug: amazon-deepracer
schema_file: json-schema/car-schema.json
slug: car
tags:
- Autonomous Vehicles
- AWS
- Machine Learning
- Reinforcement Learning
- Robotics
title: Car
---

---
description: A container definition describes a container within a task definition.
layout: schema
name: ContainerDefinition
properties_list:
- description: The name of a container. Up to 255 characters (uppercase and lowercase letters, numbers, underscores, and hyphens).
  name: name
  type: string
- description: The image used to start a container. Images in the Docker Hub registry are available by default. You can also specify an ECR repository.
  name: image
  type: string
- description: The number of cpu units reserved for the container.
  name: cpu
  type: integer
- description: The amount (in MiB) of memory to present to the container. Corresponds to the hard limit.
  name: memory
  type: integer
- description: The soft limit (in MiB) of memory to reserve for the container.
  name: memoryReservation
  type: integer
- description: Allows containers to communicate without port mappings. Only supported for bridge network mode.
  name: links
  type: array
- description: The list of port mappings for the container.
  name: portMappings
  type: array
- description: If the essential parameter of a container is marked as true and that container fails or stops, all other containers that are part of the task are stopped.
  name: essential
  type: boolean
- description: The entry point that is passed to the container.
  name: entryPoint
  type: array
- description: The command that is passed to the container.
  name: command
  type: array
- description: The environment variables to pass to a container.
  name: environment
  type: array
- description: A list of files containing the environment variables to pass to a container.
  name: environmentFiles
  type: array
- description: The mount points for data volumes in your container.
  name: mountPoints
  type: array
- description: Data volumes to mount from another container.
  name: volumesFrom
  type: array
- description: The secrets to pass to the container from AWS Secrets Manager or SSM Parameter Store.
  name: secrets
  type: array
- description: The dependencies defined for container startup and shutdown.
  name: dependsOn
  type: array
- description: Time duration (in seconds) to wait before giving up on resolving dependencies for a container.
  name: startTimeout
  type: integer
- description: Time duration (in seconds) to wait before the container is forcefully killed if it does not exit normally on its own.
  name: stopTimeout
  type: integer
- description: ''
  name: hostname
  type: string
- description: The user to run as inside the container.
  name: user
  type: string
- description: The working directory to run commands inside the container in.
  name: workingDirectory
  type: string
- description: ''
  name: disableNetworking
  type: boolean
- description: When this parameter is true, the container is given elevated privileges on the host container instance.
  name: privileged
  type: boolean
- description: When this parameter is true, the container is given read-only access to its root file system.
  name: readonlyRootFilesystem
  type: boolean
- description: ''
  name: dnsServers
  type: array
- description: ''
  name: dnsSearchDomains
  type: array
- description: ''
  name: extraHosts
  type: array
- description: ''
  name: dockerSecurityOptions
  type: array
- description: ''
  name: interactive
  type: boolean
- description: ''
  name: pseudoTerminal
  type: boolean
- description: A key/value map of labels to add to the container.
  name: dockerLabels
  type: object
- description: ''
  name: ulimits
  type: array
- description: ''
  name: systemControls
  type: array
- description: ''
  name: resourceRequirements
  type: array
- description: ''
  name: firelensConfiguration
  type: object
- description: ''
  name: repositoryCredentials
  type: object
- description: ''
  name: restartPolicy
  type: object
- description: ''
  name: credentialSpecs
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-container-definition-schema.json
slug: amazon-ecs-container-definition
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: ContainerDefinition
---

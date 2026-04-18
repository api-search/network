---
description: A job template defines the parameters for running an Ansible playbook against an inventory of managed hosts.
layout: schema
name: JobTemplate
properties_list:
- description: The unique identifier of the job template.
  name: id
  type: integer
- description: The name of the job template.
  name: name
  type: string
- description: A description of the job template.
  name: description
  type: string
- description: The type of job to execute.
  name: job_type
  type: string
- description: The ID of the inventory to run against.
  name: inventory
  type: integer
- description: The ID of the project containing the playbook.
  name: project
  type: integer
- description: The playbook filename to execute from the project.
  name: playbook
  type: string
- description: The number of parallel processes to use for execution.
  name: forks
  type: integer
- description: A host pattern to further limit the inventory scope.
  name: limit
  type: string
- description: The verbosity level for job output (0-5).
  name: verbosity
  type: integer
- description: Extra variables in YAML or JSON format.
  name: extra_vars
  type: string
- description: Whether to prompt for extra variables on launch.
  name: ask_variables_on_launch
  type: boolean
- description: Whether to prompt for inventory on launch.
  name: ask_inventory_on_launch
  type: boolean
- description: Whether to prompt for credentials on launch.
  name: ask_credential_on_launch
  type: boolean
- description: Whether the survey is enabled for this template.
  name: survey_enabled
  type: boolean
- description: The date and time the template was created.
  name: created
  type: string
- description: The date and time the template was last modified.
  name: modified
  type: string
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-ansible-automation-platform-job-template-schema.json
slug: red-hat-ansible-automation-platform-job-template
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: JobTemplate
---

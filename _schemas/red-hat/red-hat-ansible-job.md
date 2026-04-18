---
description: Schema for a job execution record in the Red Hat Ansible Automation Platform, representing a single run of a job template including its status, timing, and output metadata.
layout: schema
name: Red Hat Ansible Automation Platform Job
properties_list:
- description: The unique numeric identifier of the job execution.
  name: id
  type: integer
- description: The name of the job, typically inherited from the job template.
  name: name
  type: string
- description: A description of the job.
  name: description
  type: string
- description: The current execution status of the job.
  name: status
  type: string
- description: Whether the job execution resulted in a failure.
  name: failed
  type: boolean
- description: The ISO 8601 timestamp when job execution began.
  name: started
  type:
  - string
  - 'null'
- description: The ISO 8601 timestamp when job execution completed.
  name: finished
  type:
  - string
  - 'null'
- description: The elapsed wall-clock time in seconds for the job execution.
  name: elapsed
  type: number
- description: The type of job that was executed.
  name: job_type
  type: string
- description: How the job was launched.
  name: launch_type
  type: string
- description: The ID of the job template that was executed.
  name: job_template
  type: integer
- description: The ID of the inventory targeted by this job.
  name: inventory
  type: integer
- description: The ID of the project containing the playbook.
  name: project
  type: integer
- description: The playbook filename that was executed.
  name: playbook
  type: string
- description: The number of parallel processes used for execution.
  name: forks
  type: integer
- description: The host pattern used to limit the inventory scope.
  name: limit
  type: string
- description: The verbosity level of the job output (0=normal, 5=maximum debug).
  name: verbosity
  type: integer
- description: Extra variables passed to the playbook in YAML or JSON format.
  name: extra_vars
  type: string
- description: Artifacts collected during job execution, such as set_stats data.
  name: artifacts
  type: object
- description: Summary counts of host statuses from job execution.
  name: host_status_counts
  type: object
- description: The ISO 8601 timestamp when the job record was created.
  name: created
  type: string
- description: The ISO 8601 timestamp when the job record was last modified.
  name: modified
  type: string
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-ansible-job-schema.json
slug: red-hat-ansible-job
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Red Hat Ansible Automation Platform Job
---

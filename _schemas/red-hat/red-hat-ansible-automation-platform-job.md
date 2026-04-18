---
description: A job represents a single execution of a job template, tracking the playbook run status, timing, and output.
layout: schema
name: Job
properties_list:
- description: The unique identifier of the job.
  name: id
  type: integer
- description: The name of the job.
  name: name
  type: string
- description: The current execution status of the job.
  name: status
  type: string
- description: Whether the job execution failed.
  name: failed
  type: boolean
- description: When the job execution started.
  name: started
  type: string
- description: When the job execution finished.
  name: finished
  type: string
- description: The elapsed time in seconds for job execution.
  name: elapsed
  type: number
- description: The ID of the job template that was executed.
  name: job_template
  type: integer
- description: The ID of the inventory used for this job.
  name: inventory
  type: integer
- description: The ID of the project used for this job.
  name: project
  type: integer
- description: The playbook that was executed.
  name: playbook
  type: string
- description: How the job was launched.
  name: launch_type
  type: string
- description: The date and time the job record was created.
  name: created
  type: string
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-ansible-automation-platform-job-schema.json
slug: red-hat-ansible-automation-platform-job
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Job
---

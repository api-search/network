---
consumed_apis:
- netbackup
description: Backup operations workflow for backup administrators to manage jobs, policies, clients, and catalog images across NetBackup environments.
layout: capability
name: Veritas NetBackup Backup Operations
operations:
- description: List all backup jobs.
  method: GET
  name: list-jobs
  path: /v1/jobs
- description: Get job details.
  method: GET
  name: get-job
  path: /v1/jobs/{jobId}
- description: List all backup policies.
  method: GET
  name: list-policies
  path: /v1/policies
- description: Create a new backup policy.
  method: POST
  name: create-policy
  path: /v1/policies
- description: List all clients.
  method: GET
  name: list-clients
  path: /v1/clients
- description: List backup images.
  method: GET
  name: list-images
  path: /v1/images
personas: []
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
search_terms:
- backup job management.
- list policies
- list images
- get file contents of a backup image.
- list all backup jobs.
- netbackup client management.
- suspend a running backup job.
- create policy
- delete a backup policy.
- individual job operations.
- delete policy
- authenticate to netbackup and obtain a jwt token.
- list all netbackup clients.
- get details for a specific client.
- get a specific backup policy.
- expire a backup image.
- get image
- enterprise
- get try logs for a backup job.
- get job try logs
- get policy
- backup image catalog.
- suspend job
- storage
- list jobs
- get client
- veritas
- cancel a running backup job.
- restart a failed backup job.
- list backup images.
- backup
- get image contents
- resume a suspended backup job.
- login
- get details for a specific backup job.
- restart job
- get job details.
- create a new backup policy.
- expire image
- list clients
- get job
- disaster recovery
- recovery
- get job file list
- cancel job
- list backup images in the catalog.
- list all clients.
- list all backup jobs with optional filters.
- get file list for a backup job.
- update a backup policy.
- update policy
- get details for a specific backup image.
- data protection
- backup policy management.
- list all backup policies.
- resume job
slug: backup-operations
tags:
- Veritas
- Backup
- Data Protection
tools:
- description: Authenticate to NetBackup and obtain a JWT token.
  hints:
    readOnly: false
  name: login
- description: List all backup jobs with optional filters.
  hints:
    readOnly: true
  name: list-jobs
- description: Get details for a specific backup job.
  hints:
    readOnly: true
  name: get-job
- description: Cancel a running backup job.
  hints:
    destructive: true
  name: cancel-job
- description: Suspend a running backup job.
  hints:
    readOnly: false
  name: suspend-job
- description: Resume a suspended backup job.
  hints:
    readOnly: false
  name: resume-job
- description: Restart a failed backup job.
  hints:
    readOnly: false
  name: restart-job
- description: Get file list for a backup job.
  hints:
    readOnly: true
  name: get-job-file-list
- description: Get try logs for a backup job.
  hints:
    readOnly: true
  name: get-job-try-logs
- description: List all backup policies.
  hints:
    readOnly: true
  name: list-policies
- description: Get a specific backup policy.
  hints:
    readOnly: true
  name: get-policy
- description: Create a new backup policy.
  hints:
    readOnly: false
  name: create-policy
- description: Update a backup policy.
  hints:
    idempotent: true
    readOnly: false
  name: update-policy
- description: Delete a backup policy.
  hints:
    destructive: true
  name: delete-policy
- description: List all NetBackup clients.
  hints:
    readOnly: true
  name: list-clients
- description: Get details for a specific client.
  hints:
    readOnly: true
  name: get-client
- description: List backup images in the catalog.
  hints:
    readOnly: true
  name: list-images
- description: Get details for a specific backup image.
  hints:
    readOnly: true
  name: get-image
- description: Expire a backup image.
  hints:
    destructive: true
  name: expire-image
- description: Get file contents of a backup image.
  hints:
    readOnly: true
  name: get-image-contents
---

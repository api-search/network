---
consumed_apis: []
description: Workflow capability for executing lift-and-shift migrations from on-premises to AWS using Application Migration Service.
layout: capability
name: Lift And Shift Migration Workflow
operations:
- description: List all source servers with lifecycle state
  method: GET
  name: describe-source-servers
  path: /v1/source-servers
- description: Launch test instances for source servers
  method: POST
  name: start-test
  path: /v1/test
- description: Start production cutover to AWS
  method: POST
  name: start-cutover
  path: /v1/cutover
- description: Monitor all migration jobs
  method: GET
  name: describe-jobs
  path: /v1/jobs
personas: []
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
search_terms:
- list all source servers and their current migration lifecycle state to understand readiness.
- migration
- finalize cutover
- amazon application migration service
- list waves
- track migration progress at the wave level for large-scale migrations.
- describe jobs
- review replication settings for a source server to ensure correct staging area configuration.
- get replication configuration
- source servers to migrate
- cutover migration operations
- terminate test instances after validation to avoid unnecessary costs.
- terminate test instances
- monitor all migration jobs to track progress and identify any failures.
- get launch configuration
- list all source servers with lifecycle state
- review launch settings for a source server to verify target instance type and licensing.
- launch test instances for source servers
- lift and shift
- cloud migration
- describe source servers
- launch test instances to validate migration without impacting production source servers.
- aws
- finalize the cutover to disconnect replication and complete the migration.
- list applications
- test migration operations
- review migration application groupings to track which servers belong to each application.
- monitor all migration jobs
- start production cutover to aws
- execute the production cutover to migrate source servers to aws with minimal downtime.
- start test
- start cutover
- migration jobs
slug: lift-and-shift-migration
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
tools:
- description: List all source servers and their current migration lifecycle state to understand readiness.
  hints:
    openWorld: true
    readOnly: true
  name: describe-source-servers
- description: Review replication settings for a source server to ensure correct staging area configuration.
  hints:
    openWorld: true
    readOnly: true
  name: get-replication-configuration
- description: Review launch settings for a source server to verify target instance type and licensing.
  hints:
    openWorld: true
    readOnly: true
  name: get-launch-configuration
- description: Launch test instances to validate migration without impacting production source servers.
  hints:
    openWorld: false
    readOnly: false
  name: start-test
- description: Terminate test instances after validation to avoid unnecessary costs.
  hints:
    openWorld: false
    readOnly: false
  name: terminate-test-instances
- description: Execute the production cutover to migrate source servers to AWS with minimal downtime.
  hints:
    openWorld: false
    readOnly: false
  name: start-cutover
- description: Finalize the cutover to disconnect replication and complete the migration.
  hints:
    openWorld: false
    readOnly: false
  name: finalize-cutover
- description: Monitor all migration jobs to track progress and identify any failures.
  hints:
    openWorld: true
    readOnly: true
  name: describe-jobs
- description: Review migration application groupings to track which servers belong to each application.
  hints:
    openWorld: true
    readOnly: true
  name: list-applications
- description: Track migration progress at the wave level for large-scale migrations.
  hints:
    openWorld: true
    readOnly: true
  name: list-waves
---

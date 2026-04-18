---
description: Attributes of a NetBackup job
layout: schema
name: JobAttributes
properties_list:
- description: Unique identifier for the job
  name: jobId
  type: integer
- description: Identifier of the parent job, if this is a child job
  name: parentJobId
  type: integer
- description: The type of job
  name: jobType
  type: string
- description: Current state of the job
  name: state
  type: string
- description: Exit status code of the job. A value of 0 indicates success.
  name: status
  type: integer
- description: Name of the policy associated with the job
  name: policyName
  type: string
- description: Type of the policy (e.g., Standard, VMware, Oracle)
  name: policyType
  type: string
- description: Name of the schedule that triggered the job
  name: scheduleName
  type: string
- description: Type of the schedule
  name: scheduleType
  type: string
- description: Hostname of the client being backed up or restored
  name: clientName
  type: string
- description: Hostname of the media server processing the job
  name: mediaServer
  type: string
- description: Name of the storage unit used by the job
  name: storageUnit
  type: string
- description: Timestamp when the job started
  name: startTime
  type: string
- description: Timestamp when the job completed or was last updated
  name: endTime
  type: string
- description: Total elapsed time in seconds
  name: elapsedTime
  type: integer
- description: Total kilobytes of data transferred
  name: kilobytesTransferred
  type: integer
- description: Total number of files processed
  name: filesTransferred
  type: integer
- description: Completion percentage (0-100)
  name: percentComplete
  type: integer
- description: Description of the operation currently being performed
  name: currentOperation
  type: string
- description: Current attempt number for the job
  name: attempt
  type: integer
- description: Whether the job can be restarted
  name: restartable
  type: boolean
- description: Whether the job can be suspended
  name: suspendable
  type: boolean
- description: Whether the job can be resumed
  name: resumable
  type: boolean
- description: Whether the job can be cancelled
  name: cancellable
  type: boolean
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
schema_file: json-schema/veritas-netbackup-rest-job-attributes-schema.json
slug: veritas-netbackup-rest-job-attributes
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
title: JobAttributes
---

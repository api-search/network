---
description: Schema for a Splunk Enterprise search job resource. A search job represents an asynchronous execution of a Splunk Search Processing Language (SPL) query. Jobs progress through states from QUEUED through DONE or FAILED, producing events and results that can be retrieved via the REST API.
layout: schema
name: Splunk Search Job
properties_list:
- description: The unique search identifier (search ID) assigned to this job. Format is typically <epoch_time>.<sequential_number>.
  name: sid
  type: string
- description: The name of the search job resource, typically the SID
  name: name
  type: string
- description: The full REST API URI for this search job resource
  name: id
  type: string
- description: ISO 8601 timestamp of the last update to this search job
  name: updated
  type: string
- description: ISO 8601 timestamp of when this search job was created
  name: published
  type: string
- description: The Splunk user who created the search job
  name: author
  type: string
- description: The detailed properties and status of the search job
  name: content
  type: object
- description: Related resource links for the search job
  name: links
  type: object
- description: Access control information for the search job
  name: acl
  type: object
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-search-job-schema.json
slug: splunk-search-job
tags:
- Analytics
- Data Analysis
- Logging
- Machine Data
- Monitoring
- Observability
- Platform
- Security
- SIEM
title: Splunk Search Job
---

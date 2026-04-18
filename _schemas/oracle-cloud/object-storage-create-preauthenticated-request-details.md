---
description: Details for creating a preauthenticated request.
layout: schema
name: CreatePreauthenticatedRequestDetails
properties_list:
- description: A user-specified name for the pre-authenticated request.
  name: name
  type: string
- description: Name of object to grant access to. Omit for bucket-level access.
  name: objectName
  type: string
- description: The operation that can be performed.
  name: accessType
  type: string
- description: The expiration date for the pre-authenticated request.
  name: timeExpires
  type: string
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/object-storage-create-preauthenticated-request-details-schema.json
slug: object-storage-create-preauthenticated-request-details
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: CreatePreauthenticatedRequestDetails
---

---
description: Details for updating an instance
layout: schema
name: UpdateInstanceDetails
properties_list:
- description: A user-friendly name. Does not have to be unique. Avoid entering confidential information.
  name: displayName
  type: string
- description: The shape of the instance. Changing the shape requires the instance to be stopped first.
  name: shape
  type: string
- description: Custom metadata key/value pairs
  name: metadata
  type: object
- description: Additional metadata key/value pairs
  name: extendedMetadata
  type: object
- description: The fault domain for the instance
  name: faultDomain
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-update-instance-details-schema.json
slug: oci-compute-update-instance-details
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: UpdateInstanceDetails
---

---
description: Options for VM migration during infrastructure maintenance on launch
layout: schema
name: LaunchInstanceAvailabilityConfigDetails
properties_list:
- description: Whether live migration is the preferred option
  name: isLiveMigrationPreferred
  type: boolean
- description: The lifecycle state for an instance when maintenance is due
  name: recoveryAction
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-launch-instance-availability-config-details-schema.json
slug: oci-compute-launch-instance-availability-config-details
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: LaunchInstanceAvailabilityConfigDetails
---

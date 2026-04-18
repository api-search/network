---
description: Options for VM migration during infrastructure maintenance
layout: schema
name: InstanceAvailabilityConfig
properties_list:
- description: Whether live migration is the preferred option during maintenance
  name: isLiveMigrationPreferred
  type: boolean
- description: The lifecycle state for an instance when maintenance is due
  name: recoveryAction
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-instance-availability-config-schema.json
slug: oci-compute-instance-availability-config
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: InstanceAvailabilityConfig
---

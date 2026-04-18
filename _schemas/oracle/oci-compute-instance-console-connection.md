---
description: The details for a console connection to an instance. A console connection enables you to connect to the serial console or VNC console of an instance for troubleshooting.
layout: schema
name: InstanceConsoleConnection
properties_list:
- description: The OCID of the console connection
  name: id
  type: string
- description: The OCID of the instance the console connection connects to
  name: instanceId
  type: string
- description: The OCID of the compartment
  name: compartmentId
  type: string
- description: The SSH connection string for the console connection
  name: connectionString
  type: string
- description: The SSH public key fingerprint for the console connection
  name: fingerprint
  type: string
- description: The SSH connection string for the VNC console
  name: vncConnectionString
  type: string
- description: The lifecycle state of the console connection
  name: lifecycleState
  type: string
- description: The SSH public key fingerprint of the service host
  name: serviceHostKeyFingerprint
  type: string
provider_name: Oracle
provider_slug: oracle
schema_file: json-schema/oci-compute-instance-console-connection-schema.json
slug: oci-compute-instance-console-connection
tags:
- Cloud
- Database
- Enterprise
- Infrastructure
- SaaS
title: InstanceConsoleConnection
---

---
description: A Mule application deployed to CloudHub. Contains metadata about the application configuration, deployment status, worker settings, and runtime properties.
layout: schema
name: Application
properties_list:
- description: Unique domain name for the application, used as the subdomain in the CloudHub URL (e.g., myapp.cloudhub.io)
  name: domain
  type: string
- description: Full domain including the cloudhub.io suffix
  name: fullDomain
  type: string
- description: Current deployment status of the application
  name: status
  type: string
- description: Human-readable description of the application
  name: description
  type: string
- description: CloudHub region where the application is deployed
  name: region
  type: string
- description: Mule runtime version information
  name: muleVersion
  type: object
- description: Application properties passed to the Mule runtime
  name: properties
  type: object
- description: Unix timestamp of the last application update
  name: lastUpdateTime
  type: integer
- description: Name of the deployed application archive file
  name: fileName
  type: string
- description: Whether Anypoint Monitoring is enabled for this application
  name: monitoringEnabled
  type: boolean
- description: Whether automatic restart on failure is enabled
  name: monitoringAutoRestart
  type: boolean
- description: Whether static IPs are allocated to this application
  name: staticIPsEnabled
  type: boolean
- description: Whether persistent queues are enabled
  name: persistentQueues
  type: boolean
- description: Whether persistent queue data is encrypted
  name: persistentQueuesEncrypted
  type: boolean
- description: Whether the application uses Object Store v1
  name: objectStoreV1
  type: boolean
- description: Whether next-generation logging is enabled
  name: loggingNgEnabled
  type: boolean
- description: Transaction tracking configuration
  name: trackingSettings
  type: object
- description: ID of the VPN if the application is connected to one
  name: vpnId
  type: string
- description: VPN configuration for the application
  name: vpnConfig
  type: object
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-application-schema.json
slug: mulesoft-anypoint-platform-application
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: Application
---

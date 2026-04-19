---
description: Schema for a Mule application deployed to the Anypoint Platform, including configuration for CloudHub, Runtime Fabric, and hybrid deployment targets.
layout: schema
name: MuleSoft Anypoint Application
properties_list:
- description: Unique domain name for the application, used as the subdomain in the CloudHub URL
  name: domain
  type: string
- description: Full domain including the platform suffix (e.g., myapp.cloudhub.io)
  name: fullDomain
  type: string
- description: Current deployment status of the application
  name: status
  type: string
- description: Human-readable description of the application purpose and functionality
  name: description
  type: string
- description: Unique identifier of the organization that owns this application
  name: organizationId
  type: string
- description: Unique identifier of the environment where this application is deployed
  name: environmentId
  type: string
- description: Cloud region where the application is deployed
  name: region
  type: string
- description: ''
  name: muleVersion
  type: object
- description: ''
  name: workers
  type: object
- description: The target platform for deployment
  name: deploymentTarget
  type: string
- description: Application properties passed as runtime configuration to the Mule runtime
  name: properties
  type: object
- description: List of property keys that are treated as secure and masked in the UI
  name: secureProperties
  type: array
- description: Timestamp of the last application update or redeployment
  name: lastUpdateTime
  type: string
- description: Timestamp when the application was first created
  name: createdAt
  type: string
- description: Name of the deployed application archive file (JAR or ZIP)
  name: fileName
  type: string
- description: Whether Anypoint Monitoring is enabled for this application
  name: monitoringEnabled
  type: boolean
- description: Whether the platform automatically restarts the application on failure
  name: monitoringAutoRestart
  type: boolean
- description: Whether static IP addresses are allocated to this application
  name: staticIPsEnabled
  type: boolean
- description: Whether persistent queues are enabled for reliable message processing
  name: persistentQueues
  type: boolean
- description: Whether persistent queue data is encrypted at rest
  name: persistentQueuesEncrypted
  type: boolean
- description: Whether the application uses the legacy Object Store v1
  name: objectStoreV1
  type: boolean
- description: Whether the application uses Object Store v2
  name: objectStoreV2
  type: boolean
- description: Whether next-generation logging with Anypoint Monitoring is enabled
  name: loggingNgEnabled
  type: boolean
- description: ''
  name: trackingSettings
  type: object
- description: List of IP addresses assigned to the application workers
  name: ipAddresses
  type: array
- description: ''
  name: vpnConfig
  type: object
- description: Custom log level configuration for application packages
  name: logLevels
  type: array
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-application-schema.json
slug: mulesoft-application
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: MuleSoft Anypoint Application
---

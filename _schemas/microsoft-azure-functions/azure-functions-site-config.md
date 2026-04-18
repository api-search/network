---
description: Configuration of an App Service app.
layout: schema
name: SiteConfig
properties_list:
- description: Number of workers.
  name: numberOfWorkers
  type: integer
- description: Default documents.
  name: defaultDocuments
  type: array
- description: .NET Framework version.
  name: netFrameworkVersion
  type: string
- description: Version of PHP.
  name: phpVersion
  type: string
- description: Version of Python.
  name: pythonVersion
  type: string
- description: Version of Node.js.
  name: nodeVersion
  type: string
- description: Version of PowerShell.
  name: powerShellVersion
  type: string
- description: Linux App Framework and version
  name: linuxFxVersion
  type: string
- description: Xenon App Framework and version
  name: windowsFxVersion
  type: string
- description: <code>true</code> if request tracing is enabled; otherwise, <code>false</code>.
  name: requestTracingEnabled
  type: boolean
- description: Request tracing expiration time.
  name: requestTracingExpirationTime
  type: string
- description: <code>true</code> if remote debugging is enabled; otherwise, <code>false</code>.
  name: remoteDebuggingEnabled
  type: boolean
- description: Remote debugging version.
  name: remoteDebuggingVersion
  type: string
- description: <code>true</code> if HTTP logging is enabled; otherwise, <code>false</code>.
  name: httpLoggingEnabled
  type: boolean
- description: Flag to use Managed Identity Creds for ACR pull
  name: acrUseManagedIdentityCreds
  type: boolean
- description: If using user managed identity, the user managed identity ClientId
  name: acrUserManagedIdentityID
  type: string
- description: HTTP logs directory size limit.
  name: logsDirectorySizeLimit
  type: integer
- description: <code>true</code> if detailed error logging is enabled; otherwise, <code>false</code>.
  name: detailedErrorLoggingEnabled
  type: boolean
- description: Publishing user name.
  name: publishingUsername
  type: string
- description: Application settings. This property is not returned in response to normal create and read requests since it may contain sensitive information.
  name: appSettings
  type: array
- description: Application metadata. This property cannot be retrieved, since it may contain secrets.
  name: metadata
  type: array
- description: Connection strings. This property is not returned in response to normal create and read requests since it may contain sensitive information.
  name: connectionStrings
  type: array
- description: Site MachineKey.
  name: machineKey
  type: object
- description: Handler mappings.
  name: handlerMappings
  type: array
- description: Document root.
  name: documentRoot
  type: string
- description: SCM type.
  name: scmType
  type: object
- description: <code>true</code> to use 32-bit worker process; otherwise, <code>false</code>.
  name: use32BitWorkerProcess
  type: boolean
- description: <code>true</code> if WebSocket is enabled; otherwise, <code>false</code>.
  name: webSocketsEnabled
  type: boolean
- description: <code>true</code> if Always On is enabled; otherwise, <code>false</code>.
  name: alwaysOn
  type: boolean
- description: Java version.
  name: javaVersion
  type: string
- description: Java container.
  name: javaContainer
  type: string
- description: Java container version.
  name: javaContainerVersion
  type: string
- description: App command line to launch.
  name: appCommandLine
  type: string
- description: Managed pipeline mode.
  name: managedPipelineMode
  type: object
- description: Virtual applications.
  name: virtualApplications
  type: array
- description: Site load balancing.
  name: loadBalancing
  type: object
- description: This is work around for polymorphic types.
  name: experiments
  type: object
- description: Site limits.
  name: limits
  type: object
- description: <code>true</code> if Auto Heal is enabled; otherwise, <code>false</code>.
  name: autoHealEnabled
  type: boolean
- description: Auto Heal rules.
  name: autoHealRules
  type: object
- description: Tracing options.
  name: tracingOptions
  type: string
- description: Virtual Network name.
  name: vnetName
  type: string
- description: Virtual Network Route All enabled. This causes all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied.
  name: vnetRouteAllEnabled
  type: boolean
- description: The number of private ports assigned to this app. These will be assigned dynamically on runtime.
  name: vnetPrivatePortsCount
  type: integer
- description: Cross-Origin Resource Sharing (CORS) settings.
  name: cors
  type: object
- description: Push endpoint settings.
  name: push
  type: object
- description: Information about the formal API definition for the app.
  name: apiDefinition
  type: object
- description: Azure API management settings linked to the app.
  name: apiManagementConfig
  type: object
- description: Auto-swap slot name.
  name: autoSwapSlotName
  type: string
- description: <code>true</code> to enable local MySQL; otherwise, <code>false</code>.
  name: localMySqlEnabled
  type: boolean
- description: Managed Service Identity Id
  name: managedServiceIdentityId
  type: integer
- description: Explicit Managed Service Identity Id
  name: xManagedServiceIdentityId
  type: integer
- description: Identity to use for Key Vault Reference authentication.
  name: keyVaultReferenceIdentity
  type: string
- description: IP security restrictions for main.
  name: ipSecurityRestrictions
  type: array
- description: Default action for main access restriction if no rules are matched.
  name: ipSecurityRestrictionsDefaultAction
  type: object
- description: IP security restrictions for scm.
  name: scmIpSecurityRestrictions
  type: array
- description: Default action for scm access restriction if no rules are matched.
  name: scmIpSecurityRestrictionsDefaultAction
  type: object
- description: IP security restrictions for scm to use main.
  name: scmIpSecurityRestrictionsUseMain
  type: boolean
- description: 'Http20Enabled: configures a web site to allow clients to connect over http2.0'
  name: http20Enabled
  type: boolean
- description: 'Http20ProxyFlag: Configures a website to allow http2.0 to pass be proxied all the way to the app. 0 = disabled, 1 = pass through all http2 traffic, 2 = pass through gRPC only.'
  name: http20ProxyFlag
  type: integer
- description: 'MinTlsVersion: configures the minimum version of TLS required for SSL requests'
  name: minTlsVersion
  type: object
- description: The minimum strength TLS cipher suite allowed for an application
  name: minTlsCipherSuite
  type: object
- description: 'ScmMinTlsVersion: configures the minimum version of TLS required for SSL requests for SCM site'
  name: scmMinTlsVersion
  type: object
- description: State of FTP / FTPS service
  name: ftpsState
  type: object
- description: Number of preWarmed instances. This setting only applies to the Consumption and Elastic Plans
  name: preWarmedInstanceCount
  type: integer
- description: Maximum number of workers that a site can scale out to. This setting only applies to the Consumption and Elastic Premium Plans
  name: functionAppScaleLimit
  type: integer
- description: Maximum number of workers that a site can scale out to. This setting only applies to apps in plans where ElasticScaleEnabled is <code>true</code>
  name: elasticWebAppScaleLimit
  type: integer
- description: Health check path
  name: healthCheckPath
  type: string
- description: Gets or sets a value indicating whether functions runtime scale monitoring is enabled. When enabled, the ScaleController will not monitor event sources directly, but will instead call to the runtime t
  name: functionsRuntimeScaleMonitoringEnabled
  type: boolean
- description: Sets the time zone a site uses for generating timestamps. Compatible with Linux and Windows App Service. Setting the WEBSITE_TIME_ZONE app setting takes precedence over this config. For Linux, expects
  name: websiteTimeZone
  type: string
- description: Number of minimum instance count for a site This setting only applies to the Elastic Plans
  name: minimumElasticInstanceCount
  type: integer
- description: List of Azure Storage Accounts.
  name: azureStorageAccounts
  type: object
- description: Property to allow or block all public traffic.
  name: publicNetworkAccess
  type: string
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
schema_file: json-schema/azure-functions-site-config-schema.json
slug: azure-functions-site-config
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
title: SiteConfig
---

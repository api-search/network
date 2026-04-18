---
description: Site resource specific properties
layout: schema
name: SiteProperties
properties_list:
- description: Current state of the app.
  name: state
  type: string
- description: Hostnames associated with the app.
  name: hostNames
  type: array
- description: Name of the repository site.
  name: repositorySiteName
  type: string
- description: State indicating whether the app has exceeded its quota usage. Read-only.
  name: usageState
  type: object
- description: <code>true</code> if the app is enabled; otherwise, <code>false</code>. Setting this value to false disables the app (takes the app offline).
  name: enabled
  type: boolean
- description: Enabled hostnames for the app.Hostnames need to be assigned (see HostNames) AND enabled. Otherwise, the app is not served on those hostnames.
  name: enabledHostNames
  type: array
- description: Management information availability state for the app.
  name: availabilityState
  type: object
- description: Hostname SSL states are used to manage the SSL bindings for app's hostnames.
  name: hostNameSslStates
  type: array
- description: 'Resource ID of the associated App Service plan, formatted as: "/subscriptions/{subscriptionID}/resourceGroups/{groupName}/providers/Microsoft.Web/serverfarms/{appServicePlanName}".'
  name: serverFarmId
  type: string
- description: <code>true</code> if reserved; otherwise, <code>false</code>.
  name: reserved
  type: boolean
- description: 'Obsolete: Hyper-V sandbox.'
  name: isXenon
  type: boolean
- description: Hyper-V sandbox.
  name: hyperV
  type: boolean
- description: Last time the app was modified, in UTC. Read-only.
  name: lastModifiedTimeUtc
  type: string
- description: Property to configure various DNS related settings for a site.
  name: dnsConfiguration
  type: object
- description: Property to configure various outbound traffic routing options over virtual network for a site
  name: outboundVnetRouting
  type: object
- description: Configuration of an App Service app. This property is not returned in response to normal create and read requests since it may contain sensitive information.
  name: siteConfig
  type: object
- description: Configuration specific of the Azure Function app.
  name: functionAppConfig
  type: object
- description: Dapr configuration of the app.
  name: daprConfig
  type: object
- description: Workload profile name for function app to execute on.
  name: workloadProfileName
  type: string
- description: Function app resource requirements.
  name: resourceConfig
  type: object
- description: Azure Traffic Manager hostnames associated with the app. Read-only.
  name: trafficManagerHostNames
  type: array
- description: <code>true</code> to stop SCM (KUDU) site when the app is stopped; otherwise, <code>false</code>. The default is <code>false</code>.
  name: scmSiteAlsoStopped
  type: boolean
- description: Specifies which deployment slot this app will swap into. Read-only.
  name: targetSwapSlot
  type: string
- description: App Service Environment to use for the app.
  name: hostingEnvironmentProfile
  type: object
- description: <code>true</code> to enable client affinity; <code>false</code> to stop sending session affinity cookies, which route client requests in the same session to the same instance. Default is <code>true</c
  name: clientAffinityEnabled
  type: boolean
- description: <code>true</code> to enable client affinity partitioning using CHIPS cookies, this will add the <code>partitioned</code> property to the affinity cookies; <code>false</code> to stop sending partitione
  name: clientAffinityPartitioningEnabled
  type: boolean
- description: <code>true</code> to override client affinity cookie domain with X-Forwarded-Host request header. <code>false</code> to use default domain. Default is <code>false</code>.
  name: clientAffinityProxyEnabled
  type: boolean
- description: <code>true</code> to enable client certificate authentication (TLS mutual authentication); otherwise, <code>false</code>. Default is <code>false</code>.
  name: clientCertEnabled
  type: boolean
- description: 'This composes with ClientCertEnabled setting. - ClientCertEnabled: false means ClientCert is ignored. - ClientCertEnabled: true and ClientCertMode: Required means ClientCert is required. - ClientCertE'
  name: clientCertMode
  type: object
- description: client certificate authentication comma-separated exclusion paths
  name: clientCertExclusionPaths
  type: string
- description: Specifies the IP mode of the app.
  name: ipMode
  type: object
- description: Whether to use end to end encryption between the FrontEnd and the Worker
  name: endToEndEncryptionEnabled
  type: boolean
- description: Whether to enable ssh access.
  name: sshEnabled
  type: boolean
- description: <code>true</code> to disable the public hostnames of the app; otherwise, <code>false</code>. If <code>true</code>, the app is only accessible via API management process.
  name: hostNamesDisabled
  type: boolean
- description: Unique identifier that verifies the custom domains assigned to the app. Customer will add this id to a txt record for verification.
  name: customDomainVerificationId
  type: string
- description: List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from tenants that site can be hosted with current settings. Read-only.
  name: outboundIpAddresses
  type: string
- description: List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from all tenants except dataComponent. Read-only.
  name: possibleOutboundIpAddresses
  type: string
- description: Size of the function container.
  name: containerSize
  type: integer
- description: Maximum allowed daily memory-time quota (applicable on dynamic apps only).
  name: dailyMemoryTimeQuota
  type: integer
- description: App suspended till in case memory-time quota is exceeded.
  name: suspendedTill
  type: string
- description: Maximum number of workers. This only applies to Functions container.
  name: maxNumberOfWorkers
  type: integer
- description: If specified during app creation, the app is cloned from a source app.
  name: cloningInfo
  type: object
- description: Name of the resource group the app belongs to. Read-only.
  name: resourceGroup
  type: string
- description: <code>true</code> if the app is a default container; otherwise, <code>false</code>.
  name: isDefaultContainer
  type: boolean
- description: Default hostname of the app. Read-only.
  name: defaultHostName
  type: string
- description: Status of the last deployment slot swap operation.
  name: slotSwapStatus
  type: object
- description: 'HttpsOnly: configures a web site to accept only https requests. Issues redirect for http requests'
  name: httpsOnly
  type: boolean
- description: Site redundancy mode
  name: redundancyMode
  type: object
- description: Specifies an operation id if this site has a pending operation.
  name: inProgressOperationId
  type: string
- description: 'Property to allow or block all public traffic. Allowed Values: ''Enabled'', ''Disabled'' or an empty string.'
  name: publicNetworkAccess
  type: string
- description: Checks if Customer provided storage account is required
  name: storageAccountRequired
  type: boolean
- description: Identity to use for Key Vault Reference authentication.
  name: keyVaultReferenceIdentity
  type: string
- description: Specifies the scope of uniqueness for the default hostname during resource creation
  name: autoGeneratedDomainNameLabelScope
  type: object
- description: Azure Resource Manager ID of the Virtual network and subnet to be joined by Regional VNET Integration. This must be of the form /subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/pro
  name: virtualNetworkSubnetId
  type: string
- description: Azure Resource Manager ID of the customer's selected Managed Environment on which to host this app. This must be of the form /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Mi
  name: managedEnvironmentId
  type: string
- description: Current SKU of application based on associated App Service Plan. Some valid SKU values are Free, Shared, Basic, Dynamic, FlexConsumption, Standard, Premium, PremiumV2, PremiumV3, Isolated, IsolatedV2
  name: sku
  type: string
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
schema_file: json-schema/azure-functions-site-properties-schema.json
slug: azure-functions-site-properties
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
title: SiteProperties
---

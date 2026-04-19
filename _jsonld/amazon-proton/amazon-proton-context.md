---
class_count: 211
classes:
- CreateEnvironmentTemplateOutput
- CreateServiceSyncConfigOutput
- RepositorySyncDefinition
- DeleteEnvironmentAccountConnectionInput
- ServiceInstance
- name
- ServiceTemplateVersionSummary
- description
- GetEnvironmentTemplateInput
- ResourceCountsSummary
- ListEnvironmentTemplateVersionsInput
- RejectEnvironmentAccountConnectionOutput
- DeleteEnvironmentTemplateVersionInput
- ServicePipeline
- CreateRepositoryInput
- CancelServiceInstanceDeploymentInput
- ListServiceInstanceOutputsOutput
- DeleteEnvironmentOutput
- DeleteComponentOutput
- GetEnvironmentTemplateOutput
- Output
- ListServiceInstanceProvisionedResourcesInput
- UpdateComponentOutput
- GetComponentInput
- DeleteServiceInput
- ResourceSyncAttempt
- UpdateComponentInput
- ListServicePipelineOutputsOutput
- GetServiceSyncBlockerSummaryOutput
- ListEnvironmentOutputsInput
- CreateEnvironmentAccountConnectionInput
- GetServiceOutput
- EnvironmentTemplateSummary
- ListServicePipelineOutputsInput
- ListServiceInstanceProvisionedResourcesOutput
- RepositorySyncAttempt
- UpdateServiceSyncConfigInput
- ListServiceTemplateVersionsInput
- UntagResourceInput
- UpdateServiceInput
- Tag
- GetEnvironmentTemplateVersionOutput
- DeleteRepositoryOutput
- UpdateServiceOutput
- CreateServiceInstanceOutput
- ListEnvironmentProvisionedResourcesInput
- ListEnvironmentAccountConnectionsOutput
- UpdateServiceTemplateInput
- UpdateEnvironmentAccountConnectionInput
- CompatibleEnvironmentTemplate
- ListRepositorySyncDefinitionsInput
- CreateTemplateSyncConfigInput
- GetAccountSettingsOutput
- GetServiceTemplateOutput
- SyncBlocker
- UpdateEnvironmentTemplateVersionInput
- DeleteEnvironmentTemplateInput
- RejectEnvironmentAccountConnectionInput
- ServiceSyncConfig
- ListServiceInstancesInput
- ListEnvironmentProvisionedResourcesOutput
- UpdateServiceSyncBlockerOutput
- ServiceSummary
- DeleteEnvironmentInput
- ComponentSummary
- EnvironmentAccountConnection
- ListServicePipelineProvisionedResourcesOutput
- ResourceSyncEvent
- CreateComponentInput
- ListRepositoriesOutput
- ListServicesOutput
- ListRepositorySyncDefinitionsOutput
- UpdateServiceTemplateVersionInput
- ListComponentsOutput
- CreateServiceSyncConfigInput
- CreateEnvironmentOutput
- UpdateServiceTemplateOutput
- UpdateAccountSettingsOutput
- CreateEnvironmentAccountConnectionOutput
- GetRepositoryInput
- AcceptEnvironmentAccountConnectionOutput
- UpdateEnvironmentTemplateInput
- GetRepositorySyncStatusInput
- GetRepositorySyncStatusOutput
- CancelEnvironmentDeploymentOutput
- DeleteTemplateSyncConfigOutput
- UpdateEnvironmentInput
- Service
- CreateServiceInput
- ListTagsForResourceInput
- UpdateEnvironmentTemplateOutput
- UpdateEnvironmentTemplateVersionOutput
- ListEnvironmentTemplatesOutput
- ServiceTemplateSummary
- ServiceInstanceSummary
- CancelEnvironmentDeploymentInput
- UpdateServiceInstanceInput
- GetServiceSyncBlockerSummaryInput
- CancelServicePipelineDeploymentOutput
- ListServiceInstancesFilter
- UpdateEnvironmentOutput
- ListEnvironmentOutputsOutput
- GetServiceInstanceSyncStatusOutput
- CompatibleEnvironmentTemplateInput
- ProvisionedResource
- ListServiceTemplateVersionsOutput
- DeleteServiceTemplateVersionOutput
- CancelComponentDeploymentInput
- UpdateServiceSyncConfigOutput
- UpdateAccountSettingsInput
- GetServiceSyncConfigInput
- ListRepositoriesInput
- EnvironmentAccountConnectionSummary
- CreateRepositoryOutput
- GetRepositoryOutput
- GetServiceInstanceInput
- GetServiceInstanceOutput
- GetTemplateSyncStatusInput
- EnvironmentTemplateVersion
- ListEnvironmentsInput
- ListComponentOutputsInput
- UpdateServiceSyncBlockerInput
- ServiceTemplate
- CancelComponentDeploymentOutput
- CreateServiceTemplateOutput
- UpdateServicePipelineOutput
- DeleteTemplateSyncConfigInput
- GetEnvironmentAccountConnectionOutput
- EnvironmentTemplate
- CreateServiceTemplateInput
- DeleteEnvironmentTemplateOutput
- ListComponentsInput
- DeleteServiceSyncConfigOutput
- UpdateTemplateSyncConfigOutput
- GetComponentOutput
- AccountSettings
- EnvironmentTemplateFilter
- S3ObjectSource
- TemplateSyncConfig
- SyncBlockerContext
- GetEnvironmentOutput
- Component
- RepositorySyncEvent
- GetEnvironmentTemplateVersionInput
- ListServicePipelineProvisionedResourcesInput
- ListComponentProvisionedResourcesOutput
- UpdateServiceTemplateVersionOutput
- RepositorySummary
- CreateServiceTemplateVersionInput
- ListEnvironmentTemplateVersionsOutput
- ListEnvironmentAccountConnectionsInput
- DeleteServiceTemplateInput
- DeleteServiceTemplateVersionInput
- ListComponentOutputsOutput
- ListTagsForResourceOutput
- AcceptEnvironmentAccountConnectionInput
- UpdateTemplateSyncConfigInput
- TemplateVersionSourceInput
- ListServiceInstanceOutputsInput
- ListEnvironmentTemplatesInput
- CountsSummary
- CreateTemplateSyncConfigOutput
- CreateComponentOutput
- ServiceSyncBlockerSummary
- DeleteComponentInput
- GetServiceTemplateInput
- UpdateServicePipelineInput
- GetServiceTemplateVersionOutput
- EnvironmentTemplateVersionSummary
- ListEnvironmentsOutput
- GetEnvironmentAccountConnectionInput
- DeleteServiceTemplateOutput
- RepositoryBranchInput
- GetServiceInput
- DeleteRepositoryInput
- CreateEnvironmentTemplateVersionInput
- Environment
- UpdateEnvironmentAccountConnectionOutput
- Repository
- TagResourceInput
- ListServiceTemplatesOutput
- ListServiceInstancesOutput
- GetTemplateSyncConfigOutput
- GetTemplateSyncConfigInput
- GetServiceTemplateVersionInput
- NotifyResourceDeploymentStatusChangeInput
- CreateServiceOutput
- ServiceTemplateVersion
- GetServiceSyncConfigOutput
- CreateServiceInstanceInput
- Revision
- CreateEnvironmentTemplateInput
- DeleteServiceSyncConfigInput
- ListServicesInput
- CreateEnvironmentTemplateVersionOutput
- CancelServiceInstanceDeploymentOutput
- GetEnvironmentInput
- GetResourcesSummaryOutput
- UpdateServiceInstanceOutput
- GetServiceInstanceSyncStatusInput
- CreateServiceTemplateVersionOutput
- CreateEnvironmentInput
- ListComponentProvisionedResourcesInput
- CancelServicePipelineDeploymentInput
- DeleteEnvironmentTemplateVersionOutput
- ListServiceTemplatesInput
- DeleteEnvironmentAccountConnectionOutput
- DeleteServiceOutput
- EnvironmentSummary
- GetTemplateSyncStatusOutput
- RepositoryBranch
context_file: json-ld/amazon-proton-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-proton/refs/heads/main/json-ld/amazon-proton-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Proton from Amazon Proton.
layout: jsonld
name: Amazon Proton Context
namespaces:
- prefix: proton
  uri: https://proton.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: environmentTemplate
  type: string
- container: ''
  name: serviceSyncConfig
  type: string
- container: ''
  name: branch
  type: string
- container: ''
  name: directory
  type: string
- container: ''
  name: parent
  type: string
- container: ''
  name: target
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: createdAt
  type: string
- container: ''
  name: deploymentStatus
  type: string
- container: ''
  name: deploymentStatusMessage
  type: string
- container: ''
  name: environmentName
  type: string
- container: ''
  name: lastClientRequestToken
  type: string
- container: ''
  name: lastDeploymentAttemptedAt
  type: string
- container: ''
  name: lastDeploymentSucceededAt
  type: string
- container: ''
  name: serviceName
  type: string
- container: ''
  name: spec
  type: string
- container: ''
  name: templateMajorVersion
  type: string
- container: ''
  name: templateMinorVersion
  type: string
- container: ''
  name: templateName
  type: string
- container: ''
  name: lastModifiedAt
  type: string
- container: ''
  name: majorVersion
  type: string
- container: ''
  name: minorVersion
  type: string
- container: ''
  name: recommendedMinorVersion
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusMessage
  type: string
- container: ''
  name: behindMajor
  type: string
- container: ''
  name: behindMinor
  type: string
- container: ''
  name: failed
  type: string
- container: ''
  name: total
  type: string
- container: ''
  name: upToDate
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: environmentAccountConnection
  type: string
- container: ''
  name: connectionArn
  type: string
- container: ''
  name: encryptionKey
  type: string
- container: ''
  name: provider
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: serviceInstanceName
  type: string
- container: ''
  name: outputs
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: component
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: valueString
  type: string
- container: ''
  name: events
  type: string
- container: ''
  name: initialRevision
  type: string
- container: ''
  name: startedAt
  type: string
- container: ''
  name: targetRevision
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: deploymentType
  type: string
- container: ''
  name: serviceSpec
  type: string
- container: ''
  name: templateFile
  type: string
- container: ''
  name: serviceSyncBlockerSummary
  type: string
- container: ''
  name: codebuildRoleArn
  type: string
- container: ''
  name: componentRoleArn
  type: string
- container: ''
  name: managementAccountId
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: service
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: provisioning
  type: string
- container: ''
  name: recommendedVersion
  type: string
- container: ''
  name: provisionedResources
  type: string
- container: ''
  name: filePath
  type: string
- container: ''
  name: repositoryName
  type: string
- container: ''
  name: repositoryProvider
  type: string
- container: ''
  name: resourceArn
  type: string
- container: ''
  name: tagKeys
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: environmentTemplateVersion
  type: string
- container: ''
  name: repository
  type: string
- container: ''
  name: serviceInstance
  type: string
- container: ''
  name: environmentAccountConnections
  type: string
- container: ''
  name: syncType
  type: string
- container: ''
  name: subdirectory
  type: string
- container: ''
  name: templateType
  type: string
- container: ''
  name: accountSettings
  type: string
- container: ''
  name: serviceTemplate
  type: string
- container: ''
  name: contexts
  type: string
- container: ''
  name: createdReason
  type: string
- container: ''
  name: resolvedAt
  type: string
- container: ''
  name: resolvedReason
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: filters
  type: string
- container: ''
  name: sortBy
  type: string
- container: ''
  name: sortOrder
  type: string
- container: ''
  name: serviceSyncBlocker
  type: string
- container: ''
  name: environmentAccountId
  type: string
- container: ''
  name: requestedAt
  type: string
- container: ''
  name: event
  type: string
- container: ''
  name: externalId
  type: string
- container: ''
  name: time
  type: string
- container: ''
  name: manifest
  type: string
- container: ''
  name: repositories
  type: string
- container: ''
  name: services
  type: string
- container: ''
  name: syncDefinitions
  type: string
- container: ''
  name: compatibleEnvironmentTemplates
  type: string
- container: ''
  name: supportedComponentSources
  type: string
- container: ''
  name: components
  type: string
- container: ''
  name: latestSync
  type: string
- container: ''
  name: templateSyncConfig
  type: string
- container: ''
  name: environmentAccountConnectionId
  type: string
- container: ''
  name: protonServiceRoleArn
  type: string
- container: ''
  name: provisioningRepository
  type: string
- container: ''
  name: branchName
  type: string
- container: ''
  name: pipeline
  type: string
- container: ''
  name: repositoryConnectionArn
  type: string
- container: ''
  name: repositoryId
  type: string
- container: ''
  name: templates
  type: string
- container: ''
  name: pipelineProvisioning
  type: string
- container: ''
  name: desiredState
  type: string
- container: ''
  name: latestSuccessfulSync
  type: string
- container: ''
  name: identifier
  type: string
- container: ''
  name: provisioningEngine
  type: string
- container: ''
  name: templateVersions
  type: string
- container: ''
  name: serviceTemplateVersion
  type: string
- container: ''
  name: componentName
  type: string
- container: ''
  name: deletePipelineProvisioningRepository
  type: string
- container: ''
  name: pipelineCodebuildRoleArn
  type: string
- container: ''
  name: pipelineProvisioningRepository
  type: string
- container: ''
  name: pipelineServiceRoleArn
  type: string
- container: ''
  name: templateVersion
  type: string
- container: ''
  name: environmentTemplates
  type: string
- container: ''
  name: bucket
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: requestedBy
  type: string
- container: ''
  name: statuses
  type: string
- container: ''
  name: s3
  type: string
- container: ''
  name: environments
  type: string
- container: ''
  name: pipelines
  type: string
- container: ''
  name: serviceInstances
  type: string
- container: ''
  name: serviceTemplates
  type: string
- container: ''
  name: latestBlockers
  type: string
- container: ''
  name: deploymentId
  type: string
- container: ''
  name: sha
  type: string
- container: ''
  name: counts
  type: string
property_count: 135
provider_name: Amazon Proton
provider_slug: amazon-proton
slug: amazon-proton-context
tags:
- AWS
- DevOps
- Infrastructure as Code
- Platform Engineering
- Serverless
- Templates
- Self-Service
- CI/CD
- JSON-LD
- Linked Data
- Semantic Web
---

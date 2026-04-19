---
class_count: 50
classes:
- AccountAggregation
- AdditionalInstanceConfiguration
- Ami
- AmiDistributionConfiguration
- CancelImageCreationRequest
- CancelImageCreationResponse
- Component
- ComponentConfiguration
- ComponentParameter
- ComponentParameterDetail
- ComponentState
- ComponentSummary
- ComponentVersion
- Container
- ContainerDistributionConfiguration
- ContainerRecipe
- ContainerRecipeSummary
- CreateComponentRequest
- CreateComponentResponse
- CreateContainerRecipeRequest
- CreateContainerRecipeResponse
- CreateDistributionConfigurationRequest
- CreateDistributionConfigurationResponse
- CreateImagePipelineRequest
- CreateImagePipelineResponse
- CreateImageRecipeRequest
- CreateImageRecipeResponse
- CreateImageRequest
- CreateImageResponse
- CreateInfrastructureConfigurationRequest
- CreateInfrastructureConfigurationResponse
- CvssScore
- CvssScoreAdjustment
- CvssScoreDetails
- DeleteComponentRequest
- DeleteComponentResponse
- DeleteContainerRecipeRequest
- DeleteContainerRecipeResponse
- DeleteDistributionConfigurationRequest
- DeleteDistributionConfigurationResponse
- DeleteImagePipelineRequest
- DeleteImagePipelineResponse
- DeleteImageRecipeRequest
- DeleteImageRecipeResponse
- DeleteImageRequest
- DeleteImageResponse
- DeleteInfrastructureConfigurationRequest
- DeleteInfrastructureConfigurationResponse
- Distribution
- DistributionConfiguration
context_file: json-ld/amazon-ec2-image-builder-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-ec2-image-builder/refs/heads/main/json-ld/amazon-ec2-image-builder-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Ec2 Image Builder from Amazon EC2 Image Builder.
layout: jsonld
name: Amazon Ec2 Image Builder Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: pan
  uri: https://aws.amazon.com/schema/
properties:
- container: ''
  name: filters
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: s3Logs
  type: string
- container: ''
  name: launchTemplateId
  type: string
- container: ''
  name: accountId
  type: string
- container: ''
  name: setDefaultVersion
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: imageRecipeArn
  type: string
- container: ''
  name: containerRecipeArn
  type: string
- container: ''
  name: distributionConfigurationArn
  type: string
- container: ''
  name: infrastructureConfigurationArn
  type: string
- container: ''
  name: imageTestsConfiguration
  type: string
- container: ''
  name: enhancedImageMetadataEnabled
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: clientToken
  type: string
- container: ''
  name: imageScanningConfiguration
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: changeDescription
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: platform
  type: string
- container: ''
  name: supportedOsVersions
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: parameters
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: kmsKeyId
  type: string
- container: ''
  name: encrypted
  type: string
- container: ''
  name: dateCreated
  type: string
- container: ''
  name: publisher
  type: string
- container: ''
  name: obfuscate
  type: string
- container: ''
  name: awsAccountId
  type: string
- container: ''
  name: imageBuildVersionArn
  type: string
- container: ''
  name: imagePipelineArn
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: remediation
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: firstObservedAt
  type: string
- container: ''
  name: updatedAt
  type: string
- container: ''
  name: inspectorScore
  type: string
- container: ''
  name: inspectorScoreDetails
  type: string
- container: ''
  name: packageVulnerabilityDetails
  type: string
- container: ''
  name: fixAvailable
  type: string
- container: ''
  name: vulnerabilityId
  type: string
- container: ''
  name: vulnerablePackages
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: cvss
  type: string
- container: ''
  name: relatedVulnerabilities
  type: string
- container: ''
  name: sourceUrl
  type: string
- container: ''
  name: vendorSeverity
  type: string
- container: ''
  name: vendorCreatedAt
  type: string
- container: ''
  name: vendorUpdatedAt
  type: string
- container: ''
  name: referenceUrls
  type: string
- container: ''
  name: scheduleExpression
  type: string
- container: ''
  name: timezone
  type: string
- container: ''
  name: pipelineExecutionStartCondition
  type: string
- container: ''
  name: deviceName
  type: string
- container: ''
  name: ebs
  type: string
- container: ''
  name: virtualName
  type: string
- container: ''
  name: noDevice
  type: string
- container: ''
  name: launchTemplateName
  type: string
- container: ''
  name: launchTemplateVersion
  type: string
- container: ''
  name: components
  type: string
- container: ''
  name: parentImage
  type: string
- container: ''
  name: blockDeviceMappings
  type: string
- container: ''
  name: workingDirectory
  type: string
- container: ''
  name: additionalInstanceConfiguration
  type: string
- container: ''
  name: policy
  type: string
- container: ''
  name: schedule
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: dateUpdated
  type: string
- container: ''
  name: dateLastRun
  type: string
- container: ''
  name: dateNextRun
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: imageVersionList
  type: string
- container: ''
  name: componentVersionArn
  type: string
- container: ''
  name: aggregationType
  type: string
- container: ''
  name: responses
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: targetResourceCount
  type: string
- container: ''
  name: imageScanningEnabled
  type: string
- container: ''
  name: ecrConfiguration
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: imagePackageList
  type: string
- container: ''
  name: defaultValue
  type: string
- container: ''
  name: distributions
  type: string
- container: ''
  name: timeoutMinutes
  type: string
- container: ''
  name: adjustedCvss
  type: string
- container: ''
  name: severityCounts
  type: string
- container: ''
  name: sourceLayerHash
  type: string
- container: ''
  name: epoch
  type: string
- container: ''
  name: release
  type: string
- container: ''
  name: arch
  type: string
- container: ''
  name: packageManager
  type: string
- container: ''
  name: filePath
  type: string
- container: ''
  name: fixedInVersion
  type: string
- container: ''
  name: values
  type: string
- container: ''
  name: accountAggregation
  type: string
- container: ''
  name: imageAggregation
  type: string
- container: ''
  name: imagePipelineAggregation
  type: string
- container: ''
  name: vulnerabilityIdAggregation
  type: string
- container: ''
  name: componentSummaryList
  type: string
- container: ''
  name: semanticVersion
  type: string
- container: ''
  name: workflowBuildVersionArn
  type: string
- container: ''
  name: workflowExecutionId
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: totalStepCount
  type: string
- container: ''
  name: totalStepsSucceeded
  type: string
- container: ''
  name: totalStepsFailed
  type: string
- container: ''
  name: totalStepsSkipped
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: s3BucketName
  type: string
- container: ''
  name: s3KeyPrefix
  type: string
- container: ''
  name: osVersion
  type: string
- container: ''
  name: buildType
  type: string
- container: ''
  name: imageSource
  type: string
- container: ''
  name: imageRecipeSummaryList
  type: string
- container: ''
  name: distributionConfiguration
  type: string
- container: ''
  name: targetAccountIds
  type: string
- container: ''
  name: amiTags
  type: string
- container: ''
  name: launchPermission
  type: string
- container: ''
  name: imageArn
  type: string
- container: ''
  name: instanceTypes
  type: string
- container: ''
  name: instanceProfileName
  type: string
- container: ''
  name: securityGroupIds
  type: string
- container: ''
  name: subnetId
  type: string
- container: ''
  name: logging
  type: string
- container: ''
  name: keyPair
  type: string
- container: ''
  name: terminateInstanceOnFailure
  type: string
- container: ''
  name: snsTopicArn
  type: string
- container: ''
  name: resourceTags
  type: string
- container: ''
  name: instanceMetadataOptions
  type: string
- container: ''
  name: workflowExecutions
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: amiDistributionConfiguration
  type: string
- container: ''
  name: containerDistributionConfiguration
  type: string
- container: ''
  name: licenseConfigurationArns
  type: string
- container: ''
  name: launchTemplateConfigurations
  type: string
- container: ''
  name: s3ExportConfiguration
  type: string
- container: ''
  name: fastLaunchConfigurations
  type: string
- container: ''
  name: containerRecipe
  type: string
- container: ''
  name: steps
  type: string
- container: ''
  name: httpTokens
  type: string
- container: ''
  name: httpPutResponseHopLimit
  type: string
- container: ''
  name: roleName
  type: string
- container: ''
  name: diskImageFormat
  type: string
- container: ''
  name: s3Bucket
  type: string
- container: ''
  name: s3Prefix
  type: string
- container: ''
  name: byName
  type: string
- container: ''
  name: includeDeprecated
  type: string
- container: ''
  name: imageRecipe
  type: string
- container: ''
  name: sourcePipelineName
  type: string
- container: ''
  name: sourcePipelineArn
  type: string
- container: ''
  name: infrastructureConfiguration
  type: string
- container: ''
  name: outputResources
  type: string
- container: ''
  name: scanState
  type: string
- container: ''
  name: imageTestsEnabled
  type: string
- container: ''
  name: component
  type: string
- container: ''
  name: recommendation
  type: string
- container: ''
  name: containerTags
  type: string
- container: ''
  name: targetRepository
  type: string
- container: ''
  name: containerType
  type: string
- container: ''
  name: instanceConfiguration
  type: string
- container: ''
  name: dockerfileTemplateData
  type: string
- container: ''
  name: stepExecutionId
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: rollbackStatus
  type: string
- container: ''
  name: inputs
  type: string
- container: ''
  name: outputs
  type: string
- container: ''
  name: onFailure
  type: string
- container: ''
  name: timeoutSeconds
  type: string
- container: ''
  name: findings
  type: string
- container: ''
  name: componentBuildVersionArn
  type: string
- container: ''
  name: infrastructureConfigurationSummaryList
  type: string
- container: ''
  name: enabled
  type: string
- container: ''
  name: snapshotConfiguration
  type: string
- container: ''
  name: maxParallelLaunches
  type: string
- container: ''
  name: launchTemplate
  type: string
- container: ''
  name: filter
  type: string
- container: ''
  name: imageVersionArn
  type: string
- container: ''
  name: amis
  type: string
- container: ''
  name: containers
  type: string
- container: ''
  name: userIds
  type: string
- container: ''
  name: userGroups
  type: string
- container: ''
  name: organizationArns
  type: string
- container: ''
  name: organizationalUnitArns
  type: string
- container: ''
  name: imagePipelineList
  type: string
- container: ''
  name: uri
  type: string
- container: ''
  name: containerRecipeSummaryList
  type: string
- container: ''
  name: componentVersionList
  type: string
- container: ''
  name: uninstallAfterBuild
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: distributionConfigurationSummaryList
  type: string
- container: ''
  name: deleteOnTermination
  type: string
- container: ''
  name: iops
  type: string
- container: ''
  name: snapshotId
  type: string
- container: ''
  name: volumeSize
  type: string
property_count: 200
provider_name: Amazon EC2 Image Builder
provider_slug: amazon-ec2-image-builder
slug: amazon-ec2-image-builder-context
tags:
- Amazon Web Services
- Automation
- AWS
- Container Images
- EC2
- Image Building
- Virtual Machine Images
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 30
classes:
- Addon
- Amazon EKS Cluster
- Cluster
- CreateAddonRequest
- CreateAddonResponse
- CreateClusterRequest
- CreateClusterResponse
- CreateFargateProfileRequest
- CreateFargateProfileResponse
- CreateNodegroupRequest
- CreateNodegroupResponse
- DeleteAddonResponse
- DeleteClusterResponse
- DeleteFargateProfileResponse
- DeleteNodegroupResponse
- DescribeAddonResponse
- DescribeClusterResponse
- DescribeFargateProfileResponse
- DescribeNodegroupResponse
- FargateProfile
- FargateProfileSelector
- KubernetesNetworkConfigResponse
- ListAddonsResponse
- ListClustersResponse
- ListFargateProfilesResponse
- ListNodegroupsResponse
- Logging
- Nodegroup
- NodegroupScalingConfig
- VpcConfigResponse
context_file: json-ld/amazon-eks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-eks/refs/heads/main/json-ld/amazon-eks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Eks from Amazon EKS.
layout: jsonld
name: Amazon Eks Context
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
  name: fargateProfile
  type: string
- container: set
  name: clusters
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: endpoint
  type: reference
- container: ''
  name: roleArn
  type: string
- container: ''
  name: resourcesVpcConfig
  type: reference
- container: set
  name: subnetIds
  type: string
- container: set
  name: securityGroupIds
  type: string
- container: ''
  name: clusterSecurityGroupId
  type: string
- container: ''
  name: vpcId
  type: string
- container: ''
  name: endpointPublicAccess
  type: boolean
- container: ''
  name: endpointPrivateAccess
  type: boolean
- container: set
  name: publicAccessCidrs
  type: string
- container: ''
  name: kubernetesNetworkConfig
  type: reference
- container: ''
  name: serviceIpv4Cidr
  type: string
- container: ''
  name: serviceIpv6Cidr
  type: string
- container: ''
  name: ipFamily
  type: string
- container: ''
  name: logging
  type: reference
- container: set
  name: clusterLogging
  type: string
- container: set
  name: types
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: status
  type: string
- container: ''
  name: certificateAuthority
  type: reference
- container: ''
  name: data
  type: string
- container: ''
  name: platformVersion
  type: string
- container: ''
  name: tags
  type: reference
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: cluster
  type: string
- container: set
  name: fargateProfileNames
  type: string
- container: ''
  name: addon
  type: string
- container: ''
  name: nodegroup
  type: string
- container: set
  name: addons
  type: string
- container: ''
  name: minSize
  type: integer
- container: ''
  name: maxSize
  type: integer
- container: ''
  name: desiredSize
  type: integer
- container: ''
  name: addonName
  type: string
- container: ''
  name: addonVersion
  type: string
- container: ''
  name: addonArn
  type: string
- container: ''
  name: clusterName
  type: string
- container: ''
  name: serviceAccountRoleArn
  type: string
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: fargateProfileName
  type: string
- container: ''
  name: fargateProfileArn
  type: string
- container: ''
  name: podExecutionRoleArn
  type: string
- container: set
  name: subnets
  type: string
- container: set
  name: selectors
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: labels
  type: reference
- container: ''
  name: nodegroupName
  type: string
- container: ''
  name: nodeRole
  type: string
- container: ''
  name: scalingConfig
  type: string
- container: set
  name: instanceTypes
  type: string
- container: ''
  name: amiType
  type: string
- container: ''
  name: capacityType
  type: string
- container: set
  name: nodegroups
  type: string
- container: ''
  name: nodegroupArn
  type: string
- container: ''
  name: releaseVersion
  type: string
- container: ''
  name: resolveConflicts
  type: string
property_count: 61
provider_name: Amazon EKS
provider_slug: amazon-eks
slug: amazon-eks-context
tags:
- AWS
- Container Orchestration
- Containers
- EKS
- Kubernetes
- JSON-LD
- Linked Data
- Semantic Web
---

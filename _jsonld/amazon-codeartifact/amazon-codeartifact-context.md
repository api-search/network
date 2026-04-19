---
class_count: 106
classes:
- UpdateRepositoryResult
- RepositoryExternalConnectionInfo
- AssetSummary
- Tag
- PackageOriginConfiguration
- ListPackageVersionAssetsResult
- DescribeDomainRequest
- DeleteRepositoryPermissionsPolicyResult
- DescribePackageResult
- ListPackageVersionDependenciesResult
- UpdatePackageVersionsStatusResult
- TagResourceRequest
- DeleteRepositoryResult
- DeletePackageVersionsRequest
- DescribePackageVersionRequest
- GetAuthorizationTokenResult
- PackageVersionError
- DeleteRepositoryRequest
- GetPackageVersionAssetResult
- PutRepositoryPermissionsPolicyResult
- GetDomainPermissionsPolicyResult
- RepositoryDescription
- DomainSummary
- RepositorySummary
- DomainEntryPoint
- GetPackageVersionReadmeResult
- UntagResourceRequest
- ResourcePolicy
- DomainDescription
- PackageVersionDescription
- UpdateRepositoryRequest
- SuccessfulPackageVersionInfoMap
- DeletePackageVersionsResult
- AssetHashes
- ListRepositoriesInDomainResult
- DescribePackageRequest
- UpdatePackageVersionsStatusRequest
- ListRepositoriesResult
- PublishPackageVersionRequest
- DeleteRepositoryPermissionsPolicyRequest
- CreateRepositoryRequest
- DeletePackageRequest
- ListPackagesRequest
- ListRepositoriesInDomainRequest
- PackageOriginRestrictions
- SuccessfulPackageVersionInfo
- DescribeDomainResult
- DisposePackageVersionsResult
- LicenseInfo
- GetAuthorizationTokenRequest
- GetDomainPermissionsPolicyRequest
- AssociateExternalConnectionRequest
- PackageVersionRevisionMap
- DeleteDomainPermissionsPolicyRequest
- ListPackageVersionDependenciesRequest
- CreateRepositoryResult
- GetPackageVersionReadmeRequest
- DisassociateExternalConnectionResult
- UpstreamRepositoryInfo
- DisposePackageVersionsRequest
- PackageVersionErrorMap
- GetRepositoryEndpointResult
- PublishPackageVersionResult
- DescribeRepositoryResult
- UpstreamRepository
- CreateDomainRequest
- ListDomainsResult
- AssociateExternalConnectionResult
- GetRepositoryPermissionsPolicyResult
- PackageDescription
- DescribePackageVersionResult
- DeleteDomainResult
- ListPackageVersionsResult
- ListPackageVersionsRequest
- GetRepositoryPermissionsPolicyRequest
- UntagResourceResult
- PutDomainPermissionsPolicyResult
- ListRepositoriesRequest
- PutRepositoryPermissionsPolicyRequest
- PutDomainPermissionsPolicyRequest
- DeletePackageResult
- CopyPackageVersionsResult
- PackageDependency
- DeleteDomainPermissionsPolicyResult
- PackageSummary
- DeleteDomainRequest
- PutPackageOriginConfigurationResult
- ListPackageVersionAssetsRequest
- PutPackageOriginConfigurationRequest
- GetPackageVersionAssetRequest
- DisassociateExternalConnectionRequest
- ListTagsForResourceRequest
- CreateDomainResult
- ListDomainsRequest
- PackageVersionOrigin
- ListTagsForResourceResult
- PackageVersionSummary
- DescribeRepositoryRequest
- GetRepositoryEndpointRequest
- ListPackagesResult
- TagResourceResult
- CopyPackageVersionsRequest
- name
- version
- description
- url
context_file: json-ld/amazon-codeartifact-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-codeartifact/refs/heads/main/json-ld/amazon-codeartifact-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Codeartifact from Amazon CodeArtifact.
layout: jsonld
name: Amazon Codeartifact Context
namespaces:
- prefix: amz
  uri: https://codeartifact.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: repository
  type: string
- container: ''
  name: externalConnectionName
  type: string
- container: ''
  name: packageFormat
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: size
  type: string
- container: ''
  name: hashes
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: restrictions
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: namespace
  type: string
- container: ''
  name: package
  type: string
- container: ''
  name: versionRevision
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: assets
  type: string
- container: ''
  name: policy
  type: string
- container: ''
  name: dependencies
  type: string
- container: ''
  name: successfulVersions
  type: string
- container: ''
  name: failedVersions
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: versions
  type: string
- container: ''
  name: expectedStatus
  type: string
- container: ''
  name: authorizationToken
  type: string
- container: ''
  name: expiration
  type: string
- container: ''
  name: errorCode
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: asset
  type: string
- container: ''
  name: administratorAccount
  type: string
- container: ''
  name: domainName
  type: string
- container: ''
  name: domainOwner
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: upstreams
  type: string
- container: ''
  name: externalConnections
  type: string
- container: ''
  name: createdTime
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: encryptionKey
  type: string
- container: ''
  name: repositoryName
  type: string
- container: ''
  name: readme
  type: string
- container: ''
  name: tagKeys
  type: string
- container: ''
  name: resourceArn
  type: string
- container: ''
  name: revision
  type: string
- container: ''
  name: document
  type: string
- container: ''
  name: repositoryCount
  type: string
- container: ''
  name: assetSizeBytes
  type: string
- container: ''
  name: s3BucketArn
  type: string
- container: ''
  name: packageName
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: summary
  type: string
- container: ''
  name: homePage
  type: string
- container: ''
  name: sourceCodeRepository
  type: string
- container: ''
  name: publishedTime
  type: string
- container: ''
  name: licenses
  type: string
- container: ''
  name: origin
  type: string
- container: ''
  name: repositories
  type: string
- container: ''
  name: versionRevisions
  type: string
- container: ''
  name: targetStatus
  type: string
- container: ''
  name: assetContent
  type: string
- container: ''
  name: publish
  type: string
- container: ''
  name: upstream
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: repositoryEndpoint
  type: string
- container: ''
  name: domains
  type: string
- container: ''
  name: originConfiguration
  type: string
- container: ''
  name: packageVersion
  type: string
- container: ''
  name: defaultDisplayVersion
  type: string
- container: ''
  name: policyRevision
  type: string
- container: ''
  name: policyDocument
  type: string
- container: ''
  name: deletedPackage
  type: string
- container: ''
  name: dependencyType
  type: string
- container: ''
  name: versionRequirement
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: domainEntryPoint
  type: string
- container: ''
  name: originType
  type: string
- container: ''
  name: packages
  type: string
- container: ''
  name: allowOverwrite
  type: string
- container: ''
  name: includeFromUpstream
  type: string
property_count: 76
provider_name: Amazon CodeArtifact
provider_slug: amazon-codeartifact
slug: amazon-codeartifact-context
tags:
- Amazon
- AWS
- Artifact Repository
- Package Management
- DevOps
- Software Supply Chain
- npm
- Maven
- PyPI
- NuGet
- JSON-LD
- Linked Data
- Semantic Web
---

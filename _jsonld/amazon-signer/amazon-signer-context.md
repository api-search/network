---
class_count: 60
classes:
- AddProfilePermissionRequest
- AddProfilePermissionResponse
- CancelSigningProfileRequest
- DescribeSigningJobRequest
- DescribeSigningJobResponse
- Destination
- EncryptionAlgorithmOptions
- GetRevocationStatusRequest
- GetRevocationStatusResponse
- GetSigningPlatformRequest
- GetSigningPlatformResponse
- GetSigningProfileRequest
- GetSigningProfileResponse
- HashAlgorithmOptions
- ListProfilePermissionsRequest
- ListProfilePermissionsResponse
- ListSigningJobsRequest
- ListSigningJobsResponse
- ListSigningPlatformsRequest
- ListSigningPlatformsResponse
- ListSigningProfilesRequest
- ListSigningProfilesResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- Metadata
- Permission
- PutSigningProfileRequest
- PutSigningProfileResponse
- RemoveProfilePermissionRequest
- RemoveProfilePermissionResponse
- RevokeSignatureRequest
- RevokeSigningProfileRequest
- S3Destination
- S3SignedObject
- S3Source
- SignPayloadRequest
- SignPayloadResponse
- SignatureValidityPeriod
- SignedObject
- SigningConfigurationOverrides
- SigningConfiguration
- SigningImageFormat
- SigningJobRevocationRecord
- SigningJob
- SigningMaterial
- SigningParameters
- SigningPlatformOverrides
- SigningPlatform
- SigningProfileRevocationRecord
- SigningProfile
- Source
- StartSigningJobRequest
- StartSigningJobResponse
- TagMap
- TagResourceRequest
- TagResourceResponse
- UntagResourceRequest
- UntagResourceResponse
- createdAt
- version
context_file: json-ld/amazon-signer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-signer/refs/heads/main/json-ld/amazon-signer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Signer from Amazon Signer.
layout: jsonld
name: Amazon Signer Context
namespaces:
- prefix: amazon
  uri: https://amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: profileVersion
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: principal
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: statementId
  type: string
- container: ''
  name: jobId
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: signingMaterial
  type: string
- container: ''
  name: platformId
  type: string
- container: ''
  name: platformDisplayName
  type: string
- container: ''
  name: profileName
  type: string
- container: ''
  name: overrides
  type: string
- container: ''
  name: signingParameters
  type: string
- container: ''
  name: completedAt
  type: string
- container: ''
  name: signatureExpiresAt
  type: string
- container: ''
  name: requestedBy
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: string
- container: ''
  name: revocationRecord
  type: string
- container: ''
  name: signedObject
  type: string
- container: ''
  name: jobOwner
  type: string
- container: ''
  name: jobInvoker
  type: string
- container: ''
  name: s3
  type: string
- container: ''
  name: allowedValues
  type: string
- container: ''
  name: defaultValue
  type: string
- container: ''
  name: revokedEntities
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: partner
  type: string
- container: ''
  name: target
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: signingConfiguration
  type: string
- container: ''
  name: signingImageFormat
  type: string
- container: ''
  name: maxSizeInMB
  type: string
- container: ''
  name: revocationSupported
  type: string
- container: ''
  name: profileVersionArn
  type: string
- container: ''
  name: revocationEffectiveFrom
  type: string
- container: ''
  name: revokedAt
  type: string
- container: ''
  name: revokedBy
  type: string
- container: ''
  name: signatureValidityPeriod
  type: reference
- container: ''
  name: value
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: policySizeBytes
  type: string
- container: ''
  name: permissions
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: jobs
  type: string
- container: ''
  name: platforms
  type: string
- container: ''
  name: profiles
  type: string
- container: ''
  name: reason
  type: string
- container: ''
  name: effectiveTime
  type: string
- container: ''
  name: bucketName
  type: string
- container: ''
  name: prefix
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: profileOwner
  type: string
- container: ''
  name: payload
  type: string
- container: ''
  name: payloadFormat
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: signature
  type: string
- container: ''
  name: encryptionAlgorithm
  type: string
- container: ''
  name: hashAlgorithm
  type: string
- container: ''
  name: encryptionAlgorithmOptions
  type: string
- container: ''
  name: hashAlgorithmOptions
  type: string
- container: ''
  name: supportedFormats
  type: string
- container: ''
  name: defaultFormat
  type: string
- container: ''
  name: isRevoked
  type: string
- container: ''
  name: certificateArn
  type: string
- container: ''
  name: destination
  type: string
- container: ''
  name: clientRequestToken
  type: string
property_count: 69
provider_name: Amazon Signer
provider_slug: amazon-signer
slug: amazon-signer-context
tags:
- AWS
- Code Signing
- IoT
- Lambda
- Security
- JSON-LD
- Linked Data
- Semantic Web
---

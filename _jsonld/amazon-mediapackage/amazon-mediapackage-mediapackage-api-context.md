---
class_count: 79
classes:
- ListTagsForResourceRequest
- AdMarkers
- ConfigureLogsResponse
- IngestEndpoint
- DescribeOriginEndpointRequest
- HlsPackage
- CmafEncryption
- HlsManifest
- UpdateChannelRequest
- Authorization
- RotateIngestEndpointCredentialsResponse
- ListChannelsResponse
- DescribeHarvestJobResponse
- CmafPackage
- Channel
- AdsOnDeliveryRestrictions
- CmafPackageCreateOrUpdateParameters
- DescribeChannelRequest
- MaxResults
- MssEncryption
- DeleteOriginEndpointRequest
- SpekeKeyProvider
- CreateOriginEndpointResponse
- DeleteChannelResponse
- Status
- UpdateChannelResponse
- StreamSelection
- HarvestJob
- DeleteOriginEndpointResponse
- CmafEncryptionMethod
- StreamOrder
- ListChannelsRequest
- CreateChannelRequest
- IngressAccessLogs
- ListTagsForResourceResponse
- CreateHarvestJobResponse
- UntagResourceRequest
- Profile
- HlsIngest
- ListOriginEndpointsResponse
- UpdateOriginEndpointResponse
- CreateOriginEndpointRequest
- ListHarvestJobsResponse
- DashEncryption
- CreateHarvestJobRequest
- TagResourceRequest
- AdTriggers
- EncryptionContractConfiguration
- DescribeHarvestJobRequest
- CreateChannelResponse
- DescribeChannelResponse
- ListOriginEndpointsRequest
- PresetSpeke20Audio
- S3Destination
- UpdateOriginEndpointRequest
- MssPackage
- SegmentTemplateFormat
- RotateIngestEndpointCredentialsRequest
- ConfigureLogsRequest
- DashPackage
- ManifestLayout
- OriginEndpoint
- DeleteChannelRequest
- PlaylistType
- EncryptionMethod
- RotateChannelCredentialsRequest
- UtcTiming
- PresetSpeke20Video
- RotateChannelCredentialsResponse
- Tags
- DescribeOriginEndpointResponse
- HlsManifestCreateOrUpdateParameters
- Origination
- HlsEncryption
- EgressAccessLogs
- ListHarvestJobsRequest
- createdAt
- description
- url
context_file: json-ld/amazon-mediapackage-mediapackage-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-mediapackage/refs/heads/main/json-ld/amazon-mediapackage-mediapackage-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Mediapackage Mediapackage Api from Amazon MediaPackage.
layout: jsonld
name: Amazon Mediapackage Mediapackage Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: arn
  type: string
- container: ''
  name: egressAccessLogs
  type: string
- container: ''
  name: hlsIngest
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: ingressAccessLogs
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: username
  type: string
- container: ''
  name: adMarkers
  type: string
- container: ''
  name: adTriggers
  type: string
- container: ''
  name: adsOnDeliveryRestrictions
  type: string
- container: ''
  name: encryption
  type: string
- container: ''
  name: includeDvbSubtitles
  type: string
- container: ''
  name: includeIframeOnlyStream
  type: string
- container: ''
  name: playlistType
  type: string
- container: ''
  name: playlistWindowSeconds
  type: string
- container: ''
  name: programDateTimeIntervalSeconds
  type: string
- container: ''
  name: segmentDurationSeconds
  type: string
- container: ''
  name: streamSelection
  type: string
- container: ''
  name: useAudioRenditionGroup
  type: string
- container: ''
  name: constantInitializationVector
  type: string
- container: ''
  name: encryptionMethod
  type: string
- container: ''
  name: keyRotationIntervalSeconds
  type: string
- container: ''
  name: spekeKeyProvider
  type: string
- container: ''
  name: manifestName
  type: string
- container: ''
  name: cdnIdentifierSecret
  type: string
- container: ''
  name: secretsRoleArn
  type: string
- container: ''
  name: channels
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: channelId
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: originEndpointId
  type: string
- container: ''
  name: s3Destination
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: hlsManifests
  type: string
- container: ''
  name: segmentPrefix
  type: string
- container: ''
  name: certificateArn
  type: string
- container: ''
  name: encryptionContractConfiguration
  type: string
- container: ''
  name: resourceId
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: systemIds
  type: string
- container: ''
  name: authorization
  type: string
- container: ''
  name: cmafPackage
  type: string
- container: ''
  name: dashPackage
  type: string
- container: ''
  name: hlsPackage
  type: string
- container: ''
  name: mssPackage
  type: string
- container: ''
  name: origination
  type: string
- container: ''
  name: startoverWindowSeconds
  type: string
- container: ''
  name: timeDelaySeconds
  type: string
- container: ''
  name: whitelist
  type: string
- container: ''
  name: maxVideoBitsPerSecond
  type: string
- container: ''
  name: minVideoBitsPerSecond
  type: string
- container: ''
  name: streamOrder
  type: string
- container: ''
  name: logGroupName
  type: string
- container: ''
  name: ingestEndpoints
  type: string
- container: ''
  name: originEndpoints
  type: string
- container: ''
  name: harvestJobs
  type: string
- container: ''
  name: presetSpeke20Audio
  type: string
- container: ''
  name: presetSpeke20Video
  type: string
- container: ''
  name: bucketName
  type: string
- container: ''
  name: manifestKey
  type: string
- container: ''
  name: manifestWindowSeconds
  type: string
- container: ''
  name: manifestLayout
  type: string
- container: ''
  name: minBufferTimeSeconds
  type: string
- container: ''
  name: minUpdatePeriodSeconds
  type: string
- container: ''
  name: periodTriggers
  type: string
- container: ''
  name: profile
  type: string
- container: ''
  name: segmentTemplateFormat
  type: string
- container: ''
  name: suggestedPresentationDelaySeconds
  type: string
- container: ''
  name: utcTiming
  type: string
- container: ''
  name: utcTimingUri
  type: string
- container: ''
  name: repeatExtXKey
  type: string
property_count: 73
provider_name: Amazon MediaPackage
provider_slug: amazon-mediapackage
slug: amazon-mediapackage-mediapackage-api-context
tags:
- AWS
- Broadcasting
- Media Processing
- Media
- JSON-LD
- Linked Data
- Semantic Web
---

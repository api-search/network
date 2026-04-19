---
class_count: 82
classes:
- AudioConfiguration
- BatchError
- BatchGetChannelRequest
- BatchGetChannelResponse
- BatchGetStreamKeyRequest
- BatchGetStreamKeyResponse
- BatchStartViewerSessionRevocationError
- BatchStartViewerSessionRevocationRequest
- BatchStartViewerSessionRevocationResponse
- BatchStartViewerSessionRevocationViewerSession
- Channel
- ChannelSummary
- CreateChannelRequest
- CreateChannelResponse
- CreateRecordingConfigurationRequest
- CreateRecordingConfigurationResponse
- CreateStreamKeyRequest
- CreateStreamKeyResponse
- DeleteChannelRequest
- DeletePlaybackKeyPairRequest
- DeletePlaybackKeyPairResponse
- DeleteRecordingConfigurationRequest
- DeleteStreamKeyRequest
- DestinationConfiguration
- GetChannelRequest
- GetChannelResponse
- GetPlaybackKeyPairRequest
- GetPlaybackKeyPairResponse
- GetRecordingConfigurationRequest
- GetRecordingConfigurationResponse
- GetStreamKeyRequest
- GetStreamKeyResponse
- GetStreamRequest
- GetStreamResponse
- GetStreamSessionRequest
- GetStreamSessionResponse
- ImportPlaybackKeyPairRequest
- ImportPlaybackKeyPairResponse
- IngestConfiguration
- ListChannelsRequest
- ListChannelsResponse
- ListPlaybackKeyPairsRequest
- ListPlaybackKeyPairsResponse
- ListRecordingConfigurationsRequest
- ListRecordingConfigurationsResponse
- ListStreamKeysRequest
- ListStreamKeysResponse
- ListStreamSessionsRequest
- ListStreamSessionsResponse
- ListStreamsRequest
- ListStreamsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- PlaybackKeyPair
- PlaybackKeyPairSummary
- PutMetadataRequest
- RecordingConfiguration
- RecordingConfigurationSummary
- RenditionConfiguration
- S3DestinationConfiguration
- StartViewerSessionRevocationRequest
- StartViewerSessionRevocationResponse
- StopStreamRequest
- StopStreamResponse
- Stream
- StreamEvent
- StreamFilters
- StreamKey
- StreamKeySummary
- StreamSession
- StreamSessionSummary
- StreamSummary
- TagResourceRequest
- TagResourceResponse
- Tags
- ThumbnailConfiguration
- UntagResourceRequest
- UntagResourceResponse
- UpdateChannelRequest
- UpdateChannelResponse
- VideoConfiguration
- name
context_file: json-ld/amazon-interactive-video-service-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-interactive-video-service/refs/heads/main/json-ld/amazon-interactive-video-service-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Interactive Video Service from Amazon Interactive Video Service.
layout: jsonld
name: Amazon Interactive Video Service Context
namespaces:
- prefix: amzn
  uri: https://amazonaws.com/schema/
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
  name: arns
  type: string
- container: ''
  name: audio
  type: string
- container: ''
  name: authorized
  type: string
- container: ''
  name: avcLevel
  type: string
- container: ''
  name: avcProfile
  type: string
- container: ''
  name: bucketName
  type: string
- container: ''
  name: channel
  type: string
- container: ''
  name: channelArn
  type: string
- container: ''
  name: channels
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: codec
  type: string
- container: ''
  name: destinationConfiguration
  type: string
- container: ''
  name: encoder
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: errors
  type: string
- container: ''
  name: eventTime
  type: string
- container: ''
  name: filterBy
  type: string
- container: ''
  name: filterByName
  type: string
- container: ''
  name: filterByRecordingConfigurationArn
  type: string
- container: ''
  name: fingerprint
  type: string
- container: ''
  name: hasErrorEvent
  type: string
- container: ''
  name: health
  type: string
- container: ''
  name: ingestConfiguration
  type: string
- container: ''
  name: ingestEndpoint
  type: string
- container: ''
  name: insecureIngest
  type: string
- container: ''
  name: keyPair
  type: string
- container: ''
  name: keyPairs
  type: string
- container: ''
  name: latencyMode
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: playbackUrl
  type: string
- container: ''
  name: preset
  type: string
- container: ''
  name: publicKeyMaterial
  type: string
- container: ''
  name: recordingConfiguration
  type: string
- container: ''
  name: recordingConfigurationArn
  type: string
- container: ''
  name: recordingConfigurations
  type: string
- container: ''
  name: recordingMode
  type: string
- container: ''
  name: recordingReconnectWindowSeconds
  type: string
- container: ''
  name: renditionConfiguration
  type: string
- container: ''
  name: renditionSelection
  type: string
- container: ''
  name: renditions
  type: string
- container: ''
  name: resolution
  type: string
- container: ''
  name: s3
  type: string
- container: ''
  name: sampleRate
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: storage
  type: string
- container: ''
  name: stream
  type: string
- container: ''
  name: streamId
  type: string
- container: ''
  name: streamKey
  type: string
- container: ''
  name: streamKeys
  type: string
- container: ''
  name: streamSession
  type: string
- container: ''
  name: streamSessions
  type: string
- container: ''
  name: streams
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: targetBitrate
  type: string
- container: ''
  name: targetFramerate
  type: string
- container: ''
  name: targetIntervalSeconds
  type: string
- container: ''
  name: thumbnailConfiguration
  type: string
- container: ''
  name: truncatedEvents
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: video
  type: string
- container: ''
  name: videoHeight
  type: string
- container: ''
  name: videoWidth
  type: string
- container: ''
  name: viewerCount
  type: string
- container: ''
  name: viewerId
  type: string
- container: ''
  name: viewerSessionVersionsLessThanOrEqualTo
  type: string
- container: ''
  name: viewerSessions
  type: string
property_count: 72
provider_name: Amazon Interactive Video Service
provider_slug: amazon-interactive-video-service
slug: amazon-interactive-video-service-context
tags:
- AWS
- Live Streaming
- Media
- Video
- Real-Time
- JSON-LD
- Linked Data
- Semantic Web
---

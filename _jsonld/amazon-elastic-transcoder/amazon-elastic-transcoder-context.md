---
class_count: 67
classes:
- Artwork
- Encryption
- AudioCodecOptions
- AudioParameters
- CodecOptions
- CancelJobRequest
- CancelJobResponse
- CaptionFormat
- CaptionSource
- Captions
- Clip
- TimeSpan
- CreateJobOutput
- CreateJobPlaylist
- HlsContentProtection
- PlayReadyDrm
- CreateJobRequest
- UserMetadata
- CreateJobResponse
- Job
- CreatePipelineRequest
- Notifications
- CreatePipelineResponse
- Pipeline
- CreatePresetRequest
- Thumbnails
- CreatePresetResponse
- Preset
- Warning
- DeletePipelineRequest
- DeletePipelineResponse
- DeletePresetRequest
- DeletePresetResponse
- DetectedProperties
- InputCaptions
- JobAlbumArt
- JobInput
- JobOutput
- Timing
- JobWatermark
- ListJobsByPipelineRequest
- ListJobsByPipelineResponse
- ListJobsByStatusRequest
- ListJobsByStatusResponse
- ListPipelinesRequest
- ListPipelinesResponse
- ListPresetsRequest
- ListPresetsResponse
- Permission
- PipelineOutputConfig
- Playlist
- PresetWatermark
- ReadJobRequest
- ReadJobResponse
- ReadPipelineRequest
- ReadPipelineResponse
- ReadPresetRequest
- ReadPresetResponse
- TestRoleRequest
- TestRoleResponse
- UpdatePipelineNotificationsRequest
- UpdatePipelineNotificationsResponse
- UpdatePipelineRequest
- UpdatePipelineResponse
- UpdatePipelineStatusRequest
- UpdatePipelineStatusResponse
- VideoParameters
context_file: json-ld/amazon-elastic-transcoder-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-transcoder/refs/heads/main/json-ld/amazon-elastic-transcoder-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Elastic Transcoder from Amazon Elastic Transcoder.
layout: jsonld
name: Amazon Elastic Transcoder Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: InputKey
  type: string
- container: ''
  name: MaxWidth
  type: string
- container: ''
  name: MaxHeight
  type: string
- container: ''
  name: SizingPolicy
  type: string
- container: ''
  name: PaddingPolicy
  type: string
- container: ''
  name: AlbumArtFormat
  type: string
- container: ''
  name: Profile
  type: string
- container: ''
  name: BitDepth
  type: string
- container: ''
  name: BitOrder
  type: string
- container: ''
  name: Signed
  type: string
- container: ''
  name: Codec
  type: string
- container: ''
  name: SampleRate
  type: string
- container: ''
  name: BitRate
  type: string
- container: ''
  name: Channels
  type: string
- container: ''
  name: AudioPackingMode
  type: string
- container: ''
  name: Format
  type: string
- container: ''
  name: Pattern
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: Language
  type: string
- container: ''
  name: TimeOffset
  type: string
- container: ''
  name: Label
  type: string
- container: ''
  name: MergePolicy
  type: string
- container: ''
  name: CaptionSources
  type: string
- container: ''
  name: CaptionFormats
  type: string
- container: ''
  name: ThumbnailPattern
  type: string
- container: ''
  name: ThumbnailEncryption
  type: string
- container: ''
  name: Rotate
  type: string
- container: ''
  name: PresetId
  type: string
- container: ''
  name: SegmentDuration
  type: string
- container: ''
  name: Watermarks
  type: string
- container: ''
  name: AlbumArt
  type: string
- container: ''
  name: Composition
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: OutputKeys
  type: string
- container: ''
  name: PipelineId
  type: string
- container: ''
  name: Input
  type: string
- container: ''
  name: Inputs
  type: string
- container: ''
  name: Output
  type: string
- container: ''
  name: Outputs
  type: string
- container: ''
  name: OutputKeyPrefix
  type: string
- container: ''
  name: Playlists
  type: string
- container: ''
  name: InputBucket
  type: string
- container: ''
  name: OutputBucket
  type: string
- container: ''
  name: Role
  type: string
- container: ''
  name: AwsKmsKeyArn
  type: string
- container: ''
  name: ContentConfig
  type: string
- container: ''
  name: ThumbnailConfig
  type: string
- container: ''
  name: Warnings
  type: string
- container: ''
  name: Description
  type: string
- container: ''
  name: Container
  type: string
- container: ''
  name: Video
  type: string
- container: ''
  name: Audio
  type: string
- container: ''
  name: Width
  type: string
- container: ''
  name: Height
  type: string
- container: ''
  name: FrameRate
  type: string
- container: ''
  name: FileSize
  type: string
- container: ''
  name: DurationMillis
  type: string
- container: ''
  name: Mode
  type: string
- container: ''
  name: KeyMd5
  type: string
- container: ''
  name: InitializationVector
  type: string
- container: ''
  name: Method
  type: string
- container: ''
  name: LicenseAcquisitionUrl
  type: string
- container: ''
  name: KeyStoragePolicy
  type: string
- container: ''
  name: Resolution
  type: string
- container: ''
  name: AspectRatio
  type: string
- container: ''
  name: Interlaced
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: StatusDetail
  type: string
- container: ''
  name: Duration
  type: string
- container: ''
  name: AppliedColorSpaceConversion
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: PresetWatermarkId
  type: string
- container: ''
  name: Jobs
  type: string
- container: ''
  name: NextPageToken
  type: string
- container: ''
  name: Pipelines
  type: string
- container: ''
  name: Presets
  type: string
- container: ''
  name: Progressing
  type: string
- container: ''
  name: Completed
  type: string
- container: ''
  name: Error
  type: string
- container: ''
  name: GranteeType
  type: string
- container: ''
  name: Grantee
  type: string
- container: ''
  name: Access
  type: string
- container: ''
  name: Bucket
  type: string
- container: ''
  name: StorageClass
  type: string
- container: ''
  name: Permissions
  type: string
- container: ''
  name: KeyId
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: HorizontalAlign
  type: string
- container: ''
  name: HorizontalOffset
  type: string
- container: ''
  name: VerticalAlign
  type: string
- container: ''
  name: VerticalOffset
  type: string
- container: ''
  name: Opacity
  type: string
- container: ''
  name: Target
  type: string
- container: ''
  name: Topics
  type: string
- container: ''
  name: Success
  type: string
- container: ''
  name: Messages
  type: string
- container: ''
  name: Interval
  type: string
- container: ''
  name: StartTime
  type: string
- container: ''
  name: SubmitTimeMillis
  type: string
- container: ''
  name: StartTimeMillis
  type: string
- container: ''
  name: FinishTimeMillis
  type: string
- container: ''
  name: KeyframesMaxDist
  type: string
- container: ''
  name: FixedGOP
  type: string
- container: ''
  name: MaxFrameRate
  type: string
- container: ''
  name: DisplayAspectRatio
  type: string
- container: ''
  name: Code
  type: string
- container: ''
  name: Message
  type: string
property_count: 108
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
slug: amazon-elastic-transcoder-context
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
- JSON-LD
- Linked Data
- Semantic Web
---

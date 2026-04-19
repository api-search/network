---
class_count: 30
classes:
- CompareFacesResponse
- DetectLabelsResponse
- DetectModerationLabelsRequest
- ListCollectionsResponse
- CreateFaceLivenessSessionRequest
- DetectModerationLabelsResponse
- DetectTextResponse
- IndexFacesResponse
- GetFaceLivenessSessionResultsRequest
- StartLabelDetectionRequest
- DetectFacesRequest
- SearchFacesByImageResponse
- StartVideoJobResponse
- DetectLabelsRequest
- DetectCustomLabelsRequest
- CreateFaceLivenessSessionResponse
- CreateCollectionResponse
- CompareFacesRequest
- FaceDetail
- SearchFacesByImageRequest
- Label
- CreateCollectionRequest
- GetVideoJobResultRequest
- DetectCustomLabelsResponse
- IndexFacesRequest
- RecognizeCelebritiesResponse
- GetLabelDetectionResponse
- GetFaceLivenessSessionResultsResponse
- DetectFacesResponse
- ImageOnlyRequest
context_file: json-ld/amazon-rekognition-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-rekognition/refs/heads/main/json-ld/amazon-rekognition-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Rekognition from Amazon Rekognition.
layout: jsonld
name: Amazon Rekognition Context
namespaces:
- prefix: rekognition
  uri: https://rekognition.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Video
  type: string
- container: ''
  name: BoundingBox
  type: string
- container: ''
  name: S3Object
  type: string
- container: ''
  name: Image
  type: string
- container: ''
  name: NotificationChannel
  type: string
- container: ''
  name: SourceImageFace
  type: reference
- container: ''
  name: Confidence
  type: float
- container: set
  name: FaceMatches
  type: reference
- container: ''
  name: Similarity
  type: float
- container: ''
  name: Face
  type: reference
- container: set
  name: UnmatchedFaces
  type: reference
- container: set
  name: Labels
  type: reference
- container: ''
  name: Name
  type: string
- container: set
  name: Instances
  type: reference
- container: set
  name: Parents
  type: reference
- container: set
  name: Aliases
  type: reference
- container: set
  name: Categories
  type: reference
- container: ''
  name: LabelModelVersion
  type: string
- container: ''
  name: ImageProperties
  type: reference
- container: ''
  name: Quality
  type: reference
- container: ''
  name: Brightness
  type: decimal
- container: ''
  name: Sharpness
  type: decimal
- container: ''
  name: Contrast
  type: decimal
- container: set
  name: DominantColors
  type: reference
- container: ''
  name: Red
  type: integer
- container: ''
  name: Green
  type: integer
- container: ''
  name: Blue
  type: integer
- container: ''
  name: HexCode
  type: string
- container: ''
  name: SimplifiedColor
  type: string
- container: ''
  name: CSSColor
  type: string
- container: ''
  name: PixelPercent
  type: decimal
- container: ''
  name: MinConfidence
  type: float
- container: ''
  name: HumanLoopConfig
  type: reference
- container: ''
  name: ProjectVersion
  type: string
- container: set
  name: CollectionIds
  type: string
- container: ''
  name: NextToken
  type: string
- container: set
  name: FaceModelVersions
  type: string
- container: ''
  name: KmsKeyId
  type: string
- container: ''
  name: Settings
  type: reference
- container: ''
  name: ClientRequestToken
  type: string
- container: ''
  name: Width
  type: float
- container: ''
  name: Height
  type: float
- container: ''
  name: Left
  type: float
- container: ''
  name: Top
  type: float
- container: set
  name: ModerationLabels
  type: reference
- container: ''
  name: ParentName
  type: string
- container: ''
  name: ModerationModelVersion
  type: string
- container: ''
  name: HumanLoopActivationOutput
  type: reference
- container: set
  name: TextDetections
  type: reference
- container: ''
  name: DetectedText
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: Id
  type: integer
- container: ''
  name: ParentId
  type: integer
- container: ''
  name: Geometry
  type: reference
- container: ''
  name: TextModelVersion
  type: string
- container: set
  name: FaceRecords
  type: reference
- container: ''
  name: OrientationCorrection
  type: string
- container: ''
  name: FaceModelVersion
  type: string
- container: set
  name: UnindexedFaces
  type: reference
- container: ''
  name: SessionId
  type: string
- container: ''
  name: JobTag
  type: string
- container: set
  name: Features
  type: string
- container: set
  name: Attributes
  type: string
- container: ''
  name: SearchedFaceBoundingBox
  type: string
- container: ''
  name: SearchedFaceConfidence
  type: float
- container: ''
  name: JobId
  type: string
- container: ''
  name: MaxLabels
  type: integer
- container: ''
  name: ProjectVersionArn
  type: string
- container: ''
  name: MaxResults
  type: integer
- container: ''
  name: StatusCode
  type: integer
- container: ''
  name: CollectionArn
  type: string
- container: ''
  name: SourceImage
  type: string
- container: ''
  name: TargetImage
  type: string
- container: ''
  name: SimilarityThreshold
  type: float
- container: ''
  name: QualityFilter
  type: string
- container: ''
  name: AgeRange
  type: reference
- container: ''
  name: Low
  type: integer
- container: ''
  name: High
  type: integer
- container: ''
  name: Smile
  type: reference
- container: ''
  name: Value
  type: boolean
- container: ''
  name: Gender
  type: reference
- container: set
  name: Emotions
  type: reference
- container: ''
  name: CollectionId
  type: string
- container: ''
  name: MaxFaces
  type: integer
- container: ''
  name: FaceMatchThreshold
  type: float
- container: ''
  name: Tags
  type: reference
- container: ''
  name: Bucket
  type: string
- container: ''
  name: Version
  type: string
- container: ''
  name: SortBy
  type: string
- container: ''
  name: AggregateBy
  type: string
- container: ''
  name: Bytes
  type: string
- container: set
  name: CustomLabels
  type: reference
- container: ''
  name: SNSTopicArn
  type: string
- container: ''
  name: RoleArn
  type: string
- container: ''
  name: ExternalImageId
  type: string
- container: set
  name: DetectionAttributes
  type: string
- container: set
  name: CelebrityFaces
  type: reference
- container: set
  name: Urls
  type: string
- container: ''
  name: MatchConfidence
  type: float
- container: ''
  name: KnownGender
  type: reference
- container: set
  name: UnrecognizedFaces
  type: reference
- container: ''
  name: JobStatus
  type: string
- container: ''
  name: StatusMessage
  type: string
- container: ''
  name: VideoMetadata
  type: reference
- container: ''
  name: Status
  type: string
- container: ''
  name: ReferenceImage
  type: reference
- container: set
  name: AuditImages
  type: reference
- container: set
  name: FaceDetails
  type: string
property_count: 108
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
slug: amazon-rekognition-context
tags:
- AWS
- Celebrity Recognition
- Computer Vision
- Content Moderation
- Custom Labels
- Deep Learning
- Face Liveness
- Facial Recognition
- Image Analysis
- Machine Learning
- Object Detection
- Text Detection
- Video Analysis
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 33
classes:
- S3EncryptionConfiguration
- ValueHolder
- ListJournalS3ExportsResponse
- CreateLedgerResponse
- GetDigestResponse
- UpdateLedgerRequest
- LedgerSummary
- KinesisConfiguration
- ListJournalS3ExportsForLedgerResponse
- StreamJournalToKinesisResponse
- GetRevisionResponse
- GetRevisionRequest
- JournalKinesisStreamDescription
- DescribeJournalS3ExportResponse
- StreamJournalToKinesisRequest
- UpdateLedgerResponse
- UpdateLedgerPermissionsModeResponse
- GetBlockResponse
- ListTagsForResourceResponse
- ExportJournalToS3Response
- DescribeLedgerResponse
- GetBlockRequest
- DescribeJournalKinesisStreamResponse
- ExportJournalToS3Request
- S3ExportConfiguration
- JournalS3ExportDescription
- ListLedgersResponse
- LedgerEncryptionDescription
- TagResourceRequest
- ListJournalKinesisStreamsForLedgerResponse
- CreateLedgerRequest
- UpdateLedgerPermissionsModeRequest
- CancelJournalKinesisStreamResponse
context_file: json-ld/amazon-qldb-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-qldb/refs/heads/main/json-ld/amazon-qldb-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Qldb from Amazon QLDB.
layout: jsonld
name: Amazon Qldb Context
namespaces:
- prefix: qldb
  uri: https://qldb.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ObjectEncryptionType
  type: string
- container: ''
  name: KmsKeyArn
  type: string
- container: ''
  name: IonText
  type: string
- container: ''
  name: JournalS3Exports
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: CreationDateTime
  type: string
- container: ''
  name: PermissionsMode
  type: string
- container: ''
  name: DeletionProtection
  type: string
- container: ''
  name: Digest
  type: string
- container: ''
  name: DigestTipAddress
  type: string
- container: ''
  name: KmsKey
  type: string
- container: ''
  name: StreamArn
  type: string
- container: ''
  name: AggregationEnabled
  type: string
- container: ''
  name: StreamId
  type: string
- container: ''
  name: Proof
  type: string
- container: ''
  name: Revision
  type: string
- container: ''
  name: BlockAddress
  type: string
- container: ''
  name: DocumentId
  type: string
- container: ''
  name: LedgerName
  type: string
- container: ''
  name: CreationTime
  type: string
- container: ''
  name: InclusiveStartTime
  type: string
- container: ''
  name: ExclusiveEndTime
  type: string
- container: ''
  name: RoleArn
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: ErrorCause
  type: string
- container: ''
  name: StreamName
  type: string
- container: ''
  name: ExportDescription
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: EncryptionDescription
  type: string
- container: ''
  name: Block
  type: string
- container: ''
  name: ExportId
  type: string
- container: ''
  name: Stream
  type: string
- container: ''
  name: OutputFormat
  type: string
- container: ''
  name: ExportCreationTime
  type: string
- container: ''
  name: Ledgers
  type: string
- container: ''
  name: EncryptionStatus
  type: string
- container: ''
  name: InaccessibleKmsKeyDateTime
  type: string
- container: ''
  name: Streams
  type: string
- container: ''
  name: Bucket
  type: string
- container: ''
  name: Prefix
  type: string
- container: ''
  name: EncryptionConfiguration
  type: string
property_count: 44
provider_name: Amazon QLDB
provider_slug: amazon-qldb
slug: amazon-qldb-context
tags:
- AWS
- Blockchain
- Database
- Ledger
- JSON-LD
- Linked Data
- Semantic Web
---

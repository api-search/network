---
class_count: 32
classes:
- Amazon DynamoDB Table
- AttributeDefinition
- AttributeValue
- BatchGetItemInput
- BatchGetItemOutput
- BatchWriteItemInput
- BatchWriteItemOutput
- CreateTableInput
- CreateTableOutput
- DeleteItemInput
- DeleteItemOutput
- DescribeTableOutput
- GetItemInput
- GetItemOutput
- GlobalSecondaryIndex
- KeySchemaElement
- LocalSecondaryIndex
- ProvisionedThroughputDescription
- PutItemInput
- PutItemOutput
- QueryInput
- QueryOutput
- ScanInput
- ScanOutput
- Tag
- TransactGetItemsInput
- TransactGetItemsOutput
- TransactWriteItemsInput
- TransactWriteItemsOutput
- UpdateItemInput
- UpdateItemOutput
- UpdateTableInput
context_file: json-ld/amazon-dynamodb-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-dynamodb/refs/heads/main/json-ld/amazon-dynamodb-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Dynamodb from Amazon DynamoDB.
layout: jsonld
name: Amazon Dynamodb Context
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
  name: Projection
  type: string
- container: ''
  name: ProvisionedThroughput
  type: string
- container: ''
  name: TableDescription
  type: string
- container: ''
  name: TableName
  type: string
- container: ''
  name: Key
  type: reference
- container: ''
  name: ProjectionExpression
  type: string
- container: ''
  name: ConsistentRead
  type: boolean
- container: ''
  name: ExpressionAttributeNames
  type: reference
- container: ''
  name: Responses
  type: reference
- container: ''
  name: UnprocessedKeys
  type: reference
- container: ''
  name: UnprocessedItems
  type: reference
- container: ''
  name: UpdateExpression
  type: string
- container: ''
  name: ConditionExpression
  type: string
- container: ''
  name: ExpressionAttributeValues
  type: reference
- container: ''
  name: ReturnValues
  type: string
- container: set
  name: TransactItems
  type: string
- container: ''
  name: ClientRequestToken
  type: string
- container: ''
  name: ConditionCheck
  type: reference
- container: ''
  name: Put
  type: reference
- container: ''
  name: Delete
  type: reference
- container: ''
  name: Update
  type: reference
- container: ''
  name: IndexName
  type: string
- container: set
  name: KeySchema
  type: string
- container: ''
  name: AttributeName
  type: string
- container: ''
  name: KeyType
  type: string
- container: ''
  name: Item
  type: reference
- container: ''
  name: S
  type: string
- container: ''
  name: N
  type: string
- container: ''
  name: B
  type: string
- container: set
  name: SS
  type: string
- container: set
  name: NS
  type: string
- container: set
  name: BS
  type: string
- container: ''
  name: M
  type: reference
- container: set
  name: L
  type: string
- container: ''
  name: 'NULL'
  type: boolean
- container: ''
  name: BOOL
  type: boolean
- container: ''
  name: Table
  type: string
- container: ''
  name: ReadCapacityUnits
  type: integer
- container: ''
  name: WriteCapacityUnits
  type: integer
- container: ''
  name: Get
  type: reference
- container: ''
  name: Attributes
  type: reference
- container: ''
  name: tableName
  type: string
- container: ''
  name: tableArn
  type: string
- container: ''
  name: tableId
  type: string
- container: ''
  name: tableStatus
  type: string
- container: ''
  name: creationDateTime
  type: dateTime
- container: set
  name: keySchema
  type: string
- container: set
  name: attributeDefinitions
  type: string
- container: ''
  name: provisionedThroughput
  type: string
- container: ''
  name: billingMode
  type: string
- container: ''
  name: itemCount
  type: integer
- container: ''
  name: tableSizeBytes
  type: integer
- container: set
  name: globalSecondaryIndexes
  type: string
- container: set
  name: localSecondaryIndexes
  type: string
- container: ''
  name: streamSpecification
  type: string
- container: ''
  name: sseDescription
  type: string
- container: set
  name: tags
  type: string
- container: set
  name: Items
  type: string
- container: ''
  name: Count
  type: integer
- container: ''
  name: ScannedCount
  type: integer
- container: ''
  name: LastEvaluatedKey
  type: reference
- container: ''
  name: ProjectionType
  type: string
- container: set
  name: NonKeyAttributes
  type: string
- container: ''
  name: BillingMode
  type: string
- container: set
  name: GlobalSecondaryIndexUpdates
  type: string
- container: ''
  name: FilterExpression
  type: string
- container: ''
  name: Limit
  type: integer
- container: ''
  name: ExclusiveStartKey
  type: reference
- container: ''
  name: Segment
  type: integer
- container: ''
  name: TotalSegments
  type: integer
- container: ''
  name: Select
  type: string
- container: ''
  name: AttributeType
  type: string
- container: ''
  name: ItemCollectionMetrics
  type: reference
- container: ''
  name: RequestItems
  type: reference
- container: ''
  name: Value
  type: string
- container: ''
  name: LastIncreaseDateTime
  type: decimal
- container: ''
  name: LastDecreaseDateTime
  type: decimal
- container: ''
  name: NumberOfDecreasesToday
  type: integer
- container: set
  name: AttributeDefinitions
  type: string
- container: set
  name: GlobalSecondaryIndexes
  type: string
- container: set
  name: LocalSecondaryIndexes
  type: string
- container: set
  name: Tags
  type: string
- container: ''
  name: KeyConditionExpression
  type: string
- container: ''
  name: ScanIndexForward
  type: boolean
- container: ''
  name: TableStatus
  type: string
- container: ''
  name: TableArn
  type: string
- container: ''
  name: TableId
  type: string
- container: ''
  name: CreationDateTime
  type: decimal
- container: ''
  name: TableSizeBytes
  type: integer
- container: ''
  name: ItemCount
  type: integer
- container: ''
  name: BillingModeSummary
  type: reference
- container: ''
  name: LastUpdateToPayPerRequestDateTime
  type: decimal
property_count: 92
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
slug: amazon-dynamodb-context
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
- JSON-LD
- Linked Data
- Semantic Web
---

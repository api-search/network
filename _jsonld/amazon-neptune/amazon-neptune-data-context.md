---
class_count: 26
classes:
- CreateMLEndpointInput
- EngineStatusOutput
- ExecuteGremlinProfileInput
- ExecuteGremlinQueryInput
- ExecuteGremlinQueryOutput
- ExecuteOpenCypherExplainInput
- ExecuteOpenCypherQueryInput
- ExecuteOpenCypherQueryOutput
- ExecuteSparqlQueryInput
- GremlinQueryStatus
- GremlinQueryStatusOutput
- LoaderJobStatusOutput
- MLEndpointStatusOutput
- MLJobStatusOutput
- OpenCypherQueryStatusOutput
- PropertygraphStatisticsOutput
- PropertygraphStreamOutput
- PropertygraphStreamRecord
- SparqlQueryOutput
- SparqlStatisticsOutput
- SparqlStreamOutput
- StartLoaderJobInput
- StartLoaderJobOutput
- StartMLDataProcessingJobInput
- StartMLModelTrainingJobInput
- StartMLModelTransformJobInput
context_file: json-ld/amazon-neptune-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Data from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Data Context
namespaces:
- prefix: neptune
  uri: https://neptune.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: acceptedQueryCount
  type: integer
- container: ''
  name: allowEmptyStrings
  type: boolean
- container: ''
  name: arn
  type: string
- container: ''
  name: baseProcessingInstanceType
  type: string
- container: ''
  name: baseProcessingInstanceVolumeSizeInGB
  type: integer
- container: ''
  name: baseUri
  type: string
- container: ''
  name: cancelled
  type: boolean
- container: ''
  name: chop
  type: integer
- container: ''
  name: commitNum
  type: integer
- container: ''
  name: commitTimestampInMillis
  type: integer
- container: ''
  name: configFileName
  type: string
- container: ''
  name: customModelTrainingParameters
  type: reference
- container: ''
  name: customModelTransformParameters
  type: reference
- container: ''
  name: data
  type: reference
- container: ''
  name: dataProcessingJobId
  type: string
- container: ''
  name: dataType
  type: string
- container: ''
  name: datatypeMismatchErrors
  type: integer
- container: ''
  name: dbEngineVersion
  type: string
- container: set
  name: dependencies
  type: string
- container: ''
  name: dfeQueryEngine
  type: string
- container: ''
  name: elapsed
  type: integer
- container: ''
  name: enableInterContainerTrafficEncryption
  type: boolean
- container: ''
  name: enableManagedSpotTraining
  type: boolean
- container: ''
  name: endpoint
  type: reference
- container: ''
  name: endpointConfig
  type: reference
- container: ''
  name: eventId
  type: reference
- container: ''
  name: explainMode
  type: string
- container: ''
  name: failOnError
  type: string
- container: ''
  name: features
  type: reference
- container: set
  name: feedCount
  type: reference
- container: ''
  name: format
  type: string
- container: ''
  name: from
  type: string
- container: ''
  name: fullUri
  type: string
- container: ''
  name: gremlin
  type: reference
- container: ''
  name: head
  type: reference
- container: ''
  name: iamRoleArn
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: indexOps
  type: boolean
- container: ''
  name: inputDataS3Location
  type: string
- container: ''
  name: insertErrors
  type: integer
- container: ''
  name: instanceCount
  type: integer
- container: ''
  name: instanceType
  type: string
- container: ''
  name: isLastOp
  type: boolean
- container: ''
  name: key
  type: string
- container: ''
  name: labMode
  type: reference
- container: ''
  name: lastEventId
  type: reference
- container: ''
  name: lastTrxTimestampInMillis
  type: integer
- container: ''
  name: maxHPONumberOfTrainingJobs
  type: integer
- container: ''
  name: maxHPOParallelTrainingJobs
  type: integer
- container: ''
  name: mlModelTrainingJobId
  type: string
- container: ''
  name: mlModelTransformJobId
  type: string
- container: ''
  name: mode
  type: string
- container: ''
  name: modelName
  type: string
- container: ''
  name: modelTransformOutputS3Location
  type: string
- container: ''
  name: modelType
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: namedGraphUri
  type: string
- container: ''
  name: neptuneIamRoleArn
  type: string
- container: ''
  name: op
  type: string
- container: ''
  name: opNum
  type: integer
- container: ''
  name: opencypher
  type: reference
- container: ''
  name: outputLocation
  type: string
- container: ''
  name: overallStatus
  type: reference
- container: ''
  name: parallelism
  type: string
- container: ''
  name: parameters
  type: string
- container: ''
  name: parserConfiguration
  type: reference
- container: ''
  name: parsingErrors
  type: integer
- container: ''
  name: payload
  type: reference
- container: ''
  name: previousDataProcessingJobId
  type: string
- container: ''
  name: previousModelTrainingJobId
  type: string
- container: ''
  name: processedDataS3Location
  type: string
- container: ''
  name: processingInstanceType
  type: string
- container: ''
  name: processingInstanceVolumeSizeInGB
  type: integer
- container: ''
  name: processingJob
  type: reference
- container: ''
  name: processingTimeOutInSeconds
  type: integer
- container: set
  name: queries
  type: reference
- container: ''
  name: query
  type: string
- container: ''
  name: queryEvalStats
  type: reference
- container: ''
  name: queryId
  type: string
- container: ''
  name: queryString
  type: string
- container: ''
  name: queueRequest
  type: string
- container: set
  name: records
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: result
  type: reference
- container: set
  name: results
  type: reference
- container: ''
  name: retryNumber
  type: integer
- container: ''
  name: role
  type: string
- container: ''
  name: runNumber
  type: integer
- container: ''
  name: runningQueryCount
  type: integer
- container: ''
  name: s3OutputEncryptionKMSKey
  type: string
- container: ''
  name: sagemakerIamRoleArn
  type: string
- container: set
  name: securityGroupIds
  type: string
- container: ''
  name: serializer
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: sourceS3DirectoryPath
  type: string
- container: ''
  name: sparql
  type: reference
- container: ''
  name: startTime
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: subnets
  type: string
- container: ''
  name: to
  type: string
- container: ''
  name: totalDuplicates
  type: integer
- container: ''
  name: totalRecords
  type: integer
- container: ''
  name: totalTimeSpent
  type: integer
- container: ''
  name: trainModelS3Location
  type: string
- container: ''
  name: trainingEntryPointScript
  type: string
- container: ''
  name: trainingInstanceType
  type: string
- container: ''
  name: trainingInstanceVolumeSizeInGB
  type: integer
- container: ''
  name: trainingJobName
  type: string
- container: ''
  name: trainingTimeOutInSeconds
  type: integer
- container: ''
  name: transformEntryPointScript
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: update
  type: string
- container: ''
  name: updateSingleCardinalityProperties
  type: string
- container: ''
  name: userProvidedEdgeIds
  type: string
- container: ''
  name: value
  type: reference
- container: set
  name: vars
  type: string
- container: ''
  name: version
  type: ''
- container: ''
  name: volumeEncryptionKMSKey
  type: string
- container: ''
  name: waited
  type: integer
property_count: 120
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-data-context
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
- JSON-LD
- Linked Data
- Semantic Web
---

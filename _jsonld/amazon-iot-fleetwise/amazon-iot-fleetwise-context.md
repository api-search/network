---
class_count: 102
classes:
- Actuator
- AssociateVehicleFleetRequest
- AssociateVehicleFleetResponse
- Attribute
- BatchCreateVehicleRequest
- BatchCreateVehicleResponse
- BatchUpdateVehicleRequest
- BatchUpdateVehicleResponse
- Branch
- CampaignSummary
- CanDbcDefinition
- CanInterface
- CanSignal
- CloudWatchLogDeliveryOptions
- CollectionScheme
- ConditionBasedCollectionScheme
- CreateCampaignRequest
- CreateCampaignResponse
- CreateDecoderManifestRequest
- CreateDecoderManifestResponse
- CreateFleetRequest
- CreateFleetResponse
- CreateModelManifestRequest
- CreateModelManifestResponse
- CreateSignalCatalogRequest
- CreateSignalCatalogResponse
- CreateVehicleError
- CreateVehicleRequest
- CreateVehicleRequestItem
- CreateVehicleResponse
- CreateVehicleResponseItem
- DataDestinationConfig
- DecoderManifestSummary
- DeleteCampaignRequest
- DeleteCampaignResponse
- DeleteDecoderManifestRequest
- DeleteDecoderManifestResponse
- DeleteFleetRequest
- DeleteFleetResponse
- DeleteModelManifestRequest
- DeleteModelManifestResponse
- DeleteSignalCatalogRequest
- DeleteSignalCatalogResponse
- DeleteVehicleRequest
- DeleteVehicleResponse
- DisassociateVehicleFleetRequest
- DisassociateVehicleFleetResponse
- FleetSummary
- FormattedVss
- GetCampaignRequest
- GetCampaignResponse
- GetDecoderManifestRequest
- GetDecoderManifestResponse
- GetFleetRequest
- GetFleetResponse
- GetLoggingOptionsRequest
- GetLoggingOptionsResponse
- GetModelManifestRequest
- GetModelManifestResponse
- GetRegisterAccountStatusRequest
- GetRegisterAccountStatusResponse
- GetSignalCatalogRequest
- GetSignalCatalogResponse
- GetVehicleRequest
- GetVehicleResponse
- GetVehicleStatusRequest
- GetVehicleStatusResponse
- IamRegistrationResponse
- IamResources
- ImportDecoderManifestRequest
- ImportDecoderManifestResponse
- ImportSignalCatalogRequest
- ImportSignalCatalogResponse
- ListCampaignsRequest
- ListCampaignsResponse
- ListDecoderManifestNetworkInterfacesRequest
- ListDecoderManifestNetworkInterfacesResponse
- ListDecoderManifestSignalsRequest
- ListDecoderManifestSignalsResponse
- ListDecoderManifestsRequest
- ListDecoderManifestsResponse
- ListFleetsForVehicleRequest
- ListFleetsForVehicleResponse
- ListFleetsRequest
- ListFleetsResponse
- ListModelManifestNodesRequest
- ListModelManifestNodesResponse
- ListModelManifestsRequest
- ListModelManifestsResponse
- ListSignalCatalogNodesRequest
- ListSignalCatalogNodesResponse
- ListSignalCatalogsRequest
- ListSignalCatalogsResponse
- ListTagsForResourceRequest
- ListTagsForResourceResponse
- ListVehiclesInFleetRequest
- ListVehiclesInFleetResponse
- ListVehiclesRequest
- ListVehiclesResponse
- ModelManifestSummary
- description
- name
context_file: json-ld/amazon-iot-fleetwise-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-fleetwise/refs/heads/main/json-ld/amazon-iot-fleetwise-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Iot Fleetwise from Amazon IoT FleetWise.
layout: jsonld
name: Amazon Iot Fleetwise Context
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
  name: Key
  type: string
- container: ''
  name: ResourceARN
  type: string
- container: ''
  name: TagKeys
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: accountStatus
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: actuator
  type: string
- container: ''
  name: allowedValues
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: assignedValue
  type: string
- container: ''
  name: associationBehavior
  type: string
- container: ''
  name: attribute
  type: string
- container: ''
  name: attributeUpdateMode
  type: string
- container: ''
  name: attributes
  type: string
- container: ''
  name: bitMaskLength
  type: string
- container: ''
  name: bitRightShift
  type: string
- container: ''
  name: branch
  type: string
- container: ''
  name: bucketArn
  type: string
- container: ''
  name: byteLength
  type: string
- container: ''
  name: campaignName
  type: string
- container: ''
  name: campaignSummaries
  type: string
- container: ''
  name: campaigns
  type: string
- container: ''
  name: canDbc
  type: string
- container: ''
  name: canDbcFiles
  type: string
- container: ''
  name: canInterface
  type: string
- container: ''
  name: canSignal
  type: string
- container: ''
  name: cloudWatchLogDelivery
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: collectionScheme
  type: string
- container: ''
  name: comment
  type: string
- container: ''
  name: compression
  type: string
- container: ''
  name: conditionBasedCollectionScheme
  type: string
- container: ''
  name: conditionLanguageVersion
  type: string
- container: ''
  name: creationTime
  type: string
- container: ''
  name: customerAccountId
  type: string
- container: ''
  name: dataDestinationConfigs
  type: string
- container: ''
  name: dataExtraDimensions
  type: string
- container: ''
  name: dataFormat
  type: string
- container: ''
  name: dataType
  type: string
- container: ''
  name: decoderManifestArn
  type: string
- container: ''
  name: defaultValue
  type: string
- container: ''
  name: deprecationMessage
  type: string
- container: ''
  name: diagnosticsMode
  type: string
- container: ''
  name: dtcRequestIntervalSeconds
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: errors
  type: string
- container: ''
  name: executionRoleArn
  type: string
- container: ''
  name: expiryTime
  type: string
- container: ''
  name: expression
  type: string
- container: ''
  name: factor
  type: string
- container: ''
  name: fleetId
  type: string
- container: ''
  name: fleetSummaries
  type: string
- container: ''
  name: fleets
  type: string
- container: ''
  name: fullyQualifiedName
  type: string
- container: ''
  name: hasTransmissionEcu
  type: string
- container: ''
  name: iamRegistrationResponse
  type: string
- container: ''
  name: iamResources
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: interfaceId
  type: string
- container: ''
  name: isBigEndian
  type: string
- container: ''
  name: isSigned
  type: string
- container: ''
  name: lastModificationTime
  type: string
- container: ''
  name: length
  type: string
- container: ''
  name: logGroupName
  type: string
- container: ''
  name: logType
  type: string
- container: ''
  name: max
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: maxSampleCount
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: messageId
  type: string
- container: ''
  name: min
  type: string
- container: ''
  name: minimumSamplingIntervalMs
  type: string
- container: ''
  name: minimumTriggerIntervalMs
  type: string
- container: ''
  name: modelManifestArn
  type: string
- container: ''
  name: networkFileDefinitions
  type: string
- container: ''
  name: networkInterface
  type: string
- container: ''
  name: networkInterfaces
  type: string
- container: ''
  name: networkInterfacesToAdd
  type: string
- container: ''
  name: networkInterfacesToRemove
  type: string
- container: ''
  name: networkInterfacesToUpdate
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: nodeCounts
  type: string
- container: ''
  name: nodes
  type: string
- container: ''
  name: nodesToAdd
  type: string
- container: ''
  name: nodesToRemove
  type: string
- container: ''
  name: nodesToUpdate
  type: string
- container: ''
  name: obdInterface
  type: string
- container: ''
  name: obdSignal
  type: string
- container: ''
  name: obdStandard
  type: string
- container: ''
  name: offset
  type: string
- container: ''
  name: periodMs
  type: string
- container: ''
  name: pid
  type: string
- container: ''
  name: pidRequestIntervalSeconds
  type: string
- container: ''
  name: pidResponseLength
  type: string
- container: ''
  name: postTriggerCollectionDuration
  type: string
- container: ''
  name: prefix
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: protocolName
  type: string
- container: ''
  name: protocolVersion
  type: string
- container: ''
  name: registerAccountStatus
  type: string
- container: ''
  name: registrationStatus
  type: string
- container: ''
  name: requestMessageId
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: s3Config
  type: string
- container: ''
  name: scaling
  type: string
- container: ''
  name: sensor
  type: string
- container: ''
  name: serviceMode
  type: string
- container: ''
  name: signalCatalogArn
  type: string
- container: ''
  name: signalDecoders
  type: string
- container: ''
  name: signalDecodersToAdd
  type: string
- container: ''
  name: signalDecodersToRemove
  type: string
- container: ''
  name: signalDecodersToUpdate
  type: string
- container: ''
  name: signalsMap
  type: string
- container: ''
  name: signalsToCollect
  type: string
- container: ''
  name: spoolingMode
  type: string
- container: ''
  name: startBit
  type: string
- container: ''
  name: startByte
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: storageCompressionFormat
  type: string
- container: ''
  name: summaries
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: targetArn
  type: string
- container: ''
  name: thingArn
  type: string
- container: ''
  name: timeBasedCollectionScheme
  type: string
- container: ''
  name: timestreamConfig
  type: string
- container: ''
  name: timestreamDatabaseArn
  type: string
- container: ''
  name: timestreamDatabaseName
  type: string
- container: ''
  name: timestreamRegistrationResponse
  type: string
- container: ''
  name: timestreamResources
  type: string
- container: ''
  name: timestreamTableArn
  type: string
- container: ''
  name: timestreamTableName
  type: string
- container: ''
  name: totalActuators
  type: string
- container: ''
  name: totalAttributes
  type: string
- container: ''
  name: totalBranches
  type: string
- container: ''
  name: totalNodes
  type: string
- container: ''
  name: totalSensors
  type: string
- container: ''
  name: triggerMode
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: useExtendedIds
  type: string
- container: ''
  name: vehicleName
  type: string
- container: ''
  name: vehicleSummaries
  type: string
- container: ''
  name: vehicles
  type: string
- container: ''
  name: vss
  type: string
- container: ''
  name: vssJson
  type: string
property_count: 147
provider_name: Amazon IoT FleetWise
provider_slug: amazon-iot-fleetwise
slug: amazon-iot-fleetwise-context
tags:
- Automotive
- AWS
- Connected Vehicles
- IoT
- Telematics
- Vehicle Data
- JSON-LD
- Linked Data
- Semantic Web
---

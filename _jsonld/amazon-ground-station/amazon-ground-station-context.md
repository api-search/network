---
class_count: 114
classes:
- TagsMap
- GetMinuteUsageRequest
- ComponentVersion
- DemodulationConfig
- DescribeContactRequest
- ListEphemeridesResponse
- EphemerisMetaData
- ListSatellitesRequest
- UplinkEchoConfig
- CreateEphemerisRequest
- EndpointDetails
- GetAgentConfigurationResponse
- GetMissionProfileResponse
- Frequency
- RangedConnectionDetails
- AgentDetails
- ComponentStatusData
- DataflowEndpointGroupIdResponse
- UpdateAgentStatusResponse
- MissionProfileListItem
- GroundStationData
- Source
- CreateDataflowEndpointGroupRequest
- ContactIdResponse
- DeleteConfigRequest
- Elevation
- EphemerisItem
- ConfigIdResponse
- GetSatelliteResponse
- DataflowEndpointConfig
- ListContactsRequest
- ListGroundStationsResponse
- DescribeEphemerisResponse
- MissionProfileIdResponse
- OEMEphemeris
- DeleteDataflowEndpointGroupRequest
- ListTagsForResourceRequest
- ListDataflowEndpointGroupsRequest
- S3RecordingConfig
- SecurityDetails
- CreateConfigRequest
- GetAgentConfigurationRequest
- FrequencyBandwidth
- GetDataflowEndpointGroupResponse
- GetConfigRequest
- SocketAddress
- DescribeContactResponse
- RangedSocketAddress
- ListGroundStationsRequest
- UpdateMissionProfileRequest
- DecodeConfig
- ReserveContactRequest
- AntennaDownlinkDemodDecodeConfig
- EphemerisIdResponse
- GetSatelliteRequest
- SpectrumConfig
- TimeRange
- ConfigDetails
- AntennaDownlinkConfig
- UpdateConfigRequest
- RegisterAgentRequest
- Eirp
- UpdateEphemerisRequest
- EphemerisDescription
- UplinkSpectrumConfig
- RegisterAgentResponse
- ListConfigsRequest
- SatelliteListItem
- EphemerisTypeDescription
- TagResourceResponse
- DataflowEndpoint
- UntagResourceRequest
- AggregateStatus
- EphemerisData
- DeleteEphemerisRequest
- GetMinuteUsageResponse
- ListTagsForResourceResponse
- UntagResourceResponse
- UpdateAgentStatusRequest
- CreateMissionProfileRequest
- ListMissionProfilesRequest
- DescribeEphemerisRequest
- SignatureMap
- KmsKey
- S3Object
- ListEphemeridesRequest
- ListDataflowEndpointGroupsResponse
- GetDataflowEndpointGroupRequest
- AwsGroundStationAgentEndpoint
- TrackingConfig
- ListMissionProfilesResponse
- GetMissionProfileRequest
- CancelContactRequest
- S3RecordingDetails
- DataflowEndpointListItem
- ListConfigsResponse
- ConfigTypeData
- GetConfigResponse
- Destination
- ConnectionDetails
- ListContactsResponse
- ListSatellitesResponse
- TagResourceRequest
- DataflowDetail
- AntennaDemodDecodeDetails
- DeleteMissionProfileRequest
- IntegerRange
- DiscoveryData
- ConfigListItem
- TLEData
- ContactData
- AntennaUplinkConfig
- TLEEphemeris
- name
context_file: json-ld/amazon-ground-station-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-ground-station/refs/heads/main/json-ld/amazon-ground-station-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Ground Station from Amazon Ground Station.
layout: jsonld
name: Amazon Ground Station Context
namespaces:
- prefix: gs
  uri: https://aws.amazon.com/ground-station/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: month
  type: string
- container: ''
  name: year
  type: string
- container: ''
  name: componentType
  type: string
- container: ''
  name: versions
  type: string
- container: ''
  name: unvalidatedJSON
  type: string
- container: ''
  name: ephemerides
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: ephemerisId
  type: string
- container: ''
  name: epoch
  type: string
- container: ''
  name: source
  type: string
- container: ''
  name: antennaUplinkConfigArn
  type: string
- container: ''
  name: enabled
  type: string
- container: ''
  name: ephemeris
  type: string
- container: ''
  name: expirationTime
  type: string
- container: ''
  name: kmsKeyArn
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: satelliteId
  type: string
- container: ''
  name: tags
  type: string
- container: ''
  name: awsGroundStationAgentEndpoint
  type: string
- container: ''
  name: endpoint
  type: string
- container: ''
  name: healthReasons
  type: string
- container: ''
  name: healthStatus
  type: string
- container: ''
  name: securityDetails
  type: string
- container: ''
  name: agentId
  type: string
- container: ''
  name: taskingDocument
  type: string
- container: ''
  name: contactPostPassDurationSeconds
  type: string
- container: ''
  name: contactPrePassDurationSeconds
  type: string
- container: ''
  name: dataflowEdges
  type: string
- container: ''
  name: minimumViableContactDurationSeconds
  type: string
- container: ''
  name: missionProfileArn
  type: string
- container: ''
  name: missionProfileId
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: streamsKmsKey
  type: string
- container: ''
  name: streamsKmsRole
  type: string
- container: ''
  name: trackingConfigArn
  type: string
- container: ''
  name: units
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: mtu
  type: string
- container: ''
  name: socketAddress
  type: string
- container: ''
  name: agentCpuCores
  type: string
- container: ''
  name: agentVersion
  type: string
- container: ''
  name: componentVersions
  type: string
- container: ''
  name: instanceId
  type: string
- container: ''
  name: instanceType
  type: string
- container: ''
  name: reservedCpuCores
  type: string
- container: ''
  name: bytesReceived
  type: string
- container: ''
  name: bytesSent
  type: string
- container: ''
  name: capabilityArn
  type: string
- container: ''
  name: dataflowId
  type: string
- container: ''
  name: packetsDropped
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: dataflowEndpointGroupId
  type: string
- container: ''
  name: groundStationId
  type: string
- container: ''
  name: groundStationName
  type: string
- container: ''
  name: configDetails
  type: string
- container: ''
  name: configId
  type: string
- container: ''
  name: configType
  type: string
- container: ''
  name: dataflowSourceRegion
  type: string
- container: ''
  name: endpointDetails
  type: string
- container: ''
  name: contactId
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: creationTime
  type: string
- container: ''
  name: sourceS3Object
  type: string
- container: ''
  name: configArn
  type: string
- container: ''
  name: currentEphemeris
  type: string
- container: ''
  name: groundStations
  type: string
- container: ''
  name: noradSatelliteID
  type: string
- container: ''
  name: satelliteArn
  type: string
- container: ''
  name: dataflowEndpointName
  type: string
- container: ''
  name: dataflowEndpointRegion
  type: string
- container: ''
  name: endTime
  type: string
- container: ''
  name: groundStation
  type: string
- container: ''
  name: maxResults
  type: string
- container: ''
  name: startTime
  type: string
- container: ''
  name: statusList
  type: string
- container: ''
  name: groundStationList
  type: string
- container: ''
  name: invalidReason
  type: string
- container: ''
  name: suppliedData
  type: string
- container: ''
  name: oemData
  type: string
- container: ''
  name: s3Object
  type: string
- container: ''
  name: bucketArn
  type: string
- container: ''
  name: prefix
  type: string
- container: ''
  name: roleArn
  type: string
- container: ''
  name: securityGroupIds
  type: string
- container: ''
  name: subnetIds
  type: string
- container: ''
  name: configData
  type: string
- container: ''
  name: dataflowEndpointGroupArn
  type: string
- container: ''
  name: endpointsDetails
  type: string
- container: ''
  name: port
  type: string
- container: ''
  name: contactStatus
  type: string
- container: ''
  name: dataflowList
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: maximumElevation
  type: string
- container: ''
  name: postPassEndTime
  type: string
- container: ''
  name: prePassStartTime
  type: string
- container: ''
  name: portRange
  type: string
- container: ''
  name: decodeConfig
  type: string
- container: ''
  name: demodulationConfig
  type: string
- container: ''
  name: spectrumConfig
  type: string
- container: ''
  name: bandwidth
  type: string
- container: ''
  name: centerFrequency
  type: string
- container: ''
  name: polarization
  type: string
- container: ''
  name: antennaDemodDecodeDetails
  type: string
- container: ''
  name: s3RecordingDetails
  type: string
- container: ''
  name: agentDetails
  type: string
- container: ''
  name: discoveryData
  type: string
- container: ''
  name: ephemerisData
  type: string
- container: ''
  name: oem
  type: string
- container: ''
  name: tle
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: signatureMap
  type: string
- container: ''
  name: estimatedMinutesRemaining
  type: string
- container: ''
  name: isReservedMinutesCustomer
  type: string
- container: ''
  name: totalReservedMinuteAllocation
  type: string
- container: ''
  name: totalScheduledMinutes
  type: string
- container: ''
  name: upcomingMinutesScheduled
  type: string
- container: ''
  name: aggregateStatus
  type: string
- container: ''
  name: componentStatuses
  type: string
- container: ''
  name: taskId
  type: string
- container: ''
  name: kmsAliasArn
  type: string
- container: ''
  name: bucket
  type: string
- container: ''
  name: key
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: dataflowEndpointGroupList
  type: string
- container: ''
  name: agentStatus
  type: string
- container: ''
  name: auditResults
  type: string
- container: ''
  name: egressAddress
  type: string
- container: ''
  name: ingressAddress
  type: string
- container: ''
  name: autotrack
  type: string
- container: ''
  name: missionProfileList
  type: string
- container: ''
  name: keyTemplate
  type: string
- container: ''
  name: configList
  type: string
- container: ''
  name: antennaDownlinkConfig
  type: string
- container: ''
  name: antennaDownlinkDemodDecodeConfig
  type: string
- container: ''
  name: antennaUplinkConfig
  type: string
- container: ''
  name: dataflowEndpointConfig
  type: string
- container: ''
  name: s3RecordingConfig
  type: string
- container: ''
  name: trackingConfig
  type: string
- container: ''
  name: uplinkEchoConfig
  type: string
- container: ''
  name: dataflowDestinationRegion
  type: string
- container: ''
  name: contactList
  type: string
- container: ''
  name: satellites
  type: string
- container: ''
  name: destination
  type: string
- container: ''
  name: outputNode
  type: string
- container: ''
  name: maximum
  type: string
- container: ''
  name: minimum
  type: string
- container: ''
  name: capabilityArns
  type: string
- container: ''
  name: privateIpAddresses
  type: string
- container: ''
  name: publicIpAddresses
  type: string
- container: ''
  name: tleLine1
  type: string
- container: ''
  name: tleLine2
  type: string
- container: ''
  name: validTimeRange
  type: string
- container: ''
  name: targetEirp
  type: string
- container: ''
  name: transmitDisabled
  type: string
- container: ''
  name: tleData
  type: string
property_count: 155
provider_name: Amazon Ground Station
provider_slug: amazon-ground-station
slug: amazon-ground-station-context
tags:
- AWS
- Data Processing
- IoT
- Satellite Communications
- Space Technology
- JSON-LD
- Linked Data
- Semantic Web
---

---
class_count: 29
classes:
- AccountSettings
- Artifact
- Device
- DeviceFilter
- DeviceInstance
- DevicePool
- IncompatibilityMessage
- InstanceProfile
- Job
- NetworkProfile
- Offering
- OfferingTransaction
- Problem
- Project
- RemoteAccessSession
- Rule
- Run
- Sample
- Suite
- Test
- TestGridProject
- TestGridSession
- TestGridSessionAction
- TestGridSessionArtifact
- Upload
- VPCEConfiguration
- description
- name
- url
context_file: json-ld/amazon-device-farm-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-device-farm/refs/heads/main/json-ld/amazon-device-farm-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Device Farm from Amazon Device Farm.
layout: jsonld
name: Amazon Device Farm Context
namespaces:
- prefix: amz
  uri: https://amazonaws.com/device-farm/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: action
  type: string
- container: ''
  name: appUpload
  type: string
- container: ''
  name: arn
  type: string
- container: ''
  name: attribute
  type: string
- container: ''
  name: availability
  type: string
- container: ''
  name: awsAccountNumber
  type: string
- container: ''
  name: billingMethod
  type: string
- container: ''
  name: billingMinutes
  type: string
- container: ''
  name: carrier
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: clientId
  type: string
- container: ''
  name: completedJobs
  type: string
- container: ''
  name: contentType
  type: string
- container: ''
  name: cost
  type: string
- container: ''
  name: counters
  type: string
- container: ''
  name: cpu
  type: string
- container: ''
  name: created
  type: string
- container: ''
  name: createdOn
  type: string
- container: ''
  name: customerArtifactPaths
  type: string
- container: ''
  name: defaultJobTimeoutMinutes
  type: string
- container: ''
  name: device
  type: string
- container: ''
  name: deviceArn
  type: string
- container: ''
  name: deviceMinutes
  type: string
- container: ''
  name: devicePoolArn
  type: string
- container: ''
  name: deviceSelectionResult
  type: string
- container: ''
  name: deviceUdid
  type: string
- container: ''
  name: downlinkBandwidthBits
  type: string
- container: ''
  name: downlinkDelayMs
  type: string
- container: ''
  name: downlinkJitterMs
  type: string
- container: ''
  name: downlinkLossPercent
  type: string
- container: ''
  name: duration
  type: string
- container: ''
  name: ended
  type: string
- container: ''
  name: endpoint
  type: string
- container: ''
  name: eventCount
  type: string
- container: ''
  name: excludeAppPackagesFromCleanup
  type: string
- container: ''
  name: extension
  type: string
- container: ''
  name: filename
  type: string
- container: ''
  name: fleetName
  type: string
- container: ''
  name: fleetType
  type: string
- container: ''
  name: formFactor
  type: string
- container: ''
  name: heapSize
  type: string
- container: ''
  name: hostAddress
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: instanceArn
  type: string
- container: ''
  name: instanceProfile
  type: string
- container: ''
  name: instances
  type: string
- container: ''
  name: interactionMode
  type: string
- container: ''
  name: job
  type: string
- container: ''
  name: jobTimeoutMinutes
  type: string
- container: ''
  name: labels
  type: string
- container: ''
  name: locale
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: manufacturer
  type: string
- container: ''
  name: maxDevices
  type: string
- container: ''
  name: maxJobTimeoutMinutes
  type: string
- container: ''
  name: maxSlots
  type: string
- container: ''
  name: memory
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: model
  type: string
- container: ''
  name: modelId
  type: string
- container: ''
  name: networkProfile
  type: string
- container: ''
  name: offeringPromotionId
  type: string
- container: ''
  name: offeringStatus
  type: string
- container: ''
  name: operator
  type: string
- container: ''
  name: os
  type: string
- container: ''
  name: packageCleanup
  type: string
- container: ''
  name: parsingResultUrl
  type: string
- container: ''
  name: platform
  type: string
- container: ''
  name: radio
  type: string
- container: ''
  name: radios
  type: string
- container: ''
  name: rebootAfterUse
  type: string
- container: ''
  name: recurringCharges
  type: string
- container: ''
  name: remoteAccessEnabled
  type: string
- container: ''
  name: remoteDebugEnabled
  type: string
- container: ''
  name: remoteRecordAppArn
  type: string
- container: ''
  name: remoteRecordEnabled
  type: string
- container: ''
  name: requestMethod
  type: string
- container: ''
  name: resolution
  type: string
- container: ''
  name: result
  type: string
- container: ''
  name: resultCode
  type: string
- container: ''
  name: rules
  type: string
- container: ''
  name: run
  type: string
- container: ''
  name: seed
  type: string
- container: ''
  name: seleniumProperties
  type: string
- container: ''
  name: serviceDnsName
  type: string
- container: ''
  name: skipAppResign
  type: string
- container: ''
  name: started
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusCode
  type: string
- container: ''
  name: stopped
  type: string
- container: ''
  name: suite
  type: string
- container: ''
  name: test
  type: string
- container: ''
  name: testSpecArn
  type: string
- container: ''
  name: totalJobs
  type: string
- container: ''
  name: transactionId
  type: string
- container: ''
  name: trialMinutes
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: udid
  type: string
- container: ''
  name: unmeteredDevices
  type: string
- container: ''
  name: unmeteredRemoteAccessDevices
  type: string
- container: ''
  name: uplinkBandwidthBits
  type: string
- container: ''
  name: uplinkDelayMs
  type: string
- container: ''
  name: uplinkJitterMs
  type: string
- container: ''
  name: uplinkLossPercent
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: values
  type: string
- container: ''
  name: videoCapture
  type: string
- container: ''
  name: videoEndpoint
  type: string
- container: ''
  name: vpcConfig
  type: string
- container: ''
  name: vpceConfigurationDescription
  type: string
- container: ''
  name: vpceConfigurationName
  type: string
- container: ''
  name: vpceServiceName
  type: string
- container: ''
  name: webUrl
  type: string
property_count: 115
provider_name: Amazon Device Farm
provider_slug: amazon-device-farm
slug: amazon-device-farm-context
tags:
- Application Testing
- AWS
- Device Testing
- Mobile Testing
- Quality Assurance
- JSON-LD
- Linked Data
- Semantic Web
---

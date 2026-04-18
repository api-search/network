---
class_count: 6
classes:
- Classification
- DSPMPolicy
- DataAsset
- DataRisk
- DataSecurityAlert
- DataStore
context_file: json-ld/palo-alto-prisma-cloud-dspm-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-cloud-dspm-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Cloud Dspm Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Cloud Dspm Api Context
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
- container: set
  name: affectedClassifications
  type: string
- container: ''
  name: affectedDataAssetCount
  type: integer
- container: ''
  name: alertType
  type: string
- container: ''
  name: assetType
  type: string
- container: ''
  name: automatedRemediationAvailable
  type: boolean
- container: ''
  name: category
  type: string
- container: ''
  name: classification
  type: string
- container: ''
  name: classificationLabel
  type: string
- container: set
  name: classificationLabels
  type: string
- container: ''
  name: cloudAccountId
  type: string
- container: ''
  name: cloudProvider
  type: string
- container: set
  name: cloudProviders
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: dataAssetCount
  type: integer
- container: ''
  name: dataStoreCount
  type: integer
- container: ''
  name: dataStoreId
  type: string
- container: ''
  name: dataStoreName
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: detectedAt
  type: dateTime
- container: ''
  name: discoveredAt
  type: dateTime
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: encryptionEnabled
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: isBuiltIn
  type: boolean
- container: ''
  name: isPubliclyAccessible
  type: boolean
- container: ''
  name: lastEvaluatedAt
  type: dateTime
- container: ''
  name: lastScannedAt
  type: dateTime
- container: ''
  name: name
  type: string
- container: ''
  name: path
  type: string
- container: ''
  name: pattern
  type: string
- container: ''
  name: recordCount
  type: integer
- container: ''
  name: region
  type: string
- container: set
  name: regulatoryFrameworks
  type: string
- container: ''
  name: remediation
  type: reference
- container: set
  name: requiredControls
  type: string
- container: ''
  name: resolvedAt
  type: dateTime
- container: ''
  name: riskCategory
  type: string
- container: ''
  name: riskLevel
  type: string
- container: set
  name: sampleFindings
  type: reference
- container: ''
  name: sampleValue
  type: string
- container: ''
  name: sensitiveDataCount
  type: integer
- container: ''
  name: sensitivityLevel
  type: string
- container: ''
  name: serviceName
  type: string
- container: ''
  name: serviceType
  type: string
- container: ''
  name: severity
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: steps
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: updatedAt
  type: dateTime
property_count: 50
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-cloud-dspm-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---

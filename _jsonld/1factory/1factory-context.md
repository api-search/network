---
class_count: 29
classes:
- Address
- AssemblyEntry
- Assembly
- Capa
- Certification
- Complaint
- FaiDetail
- Fai
- InspectionDetail
- Inspection
- Issue
- Ncr
- NewFai
- NewInspection
- NewPartMaster
- PartData
- PartMaster
- PlanDetail
- Plan
- Qualification
- SpecInspectionType
- Specification
- SuperInspection
- Supplier
- User
- description
- email
- name
- version
context_file: json-ld/1factory-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/1factory/refs/heads/main/json-ld/1factory-context.jsonld
description: JSON-LD context defining the semantic vocabulary for 1Factory from 1Factory.
layout: jsonld
name: 1Factory Context
namespaces:
- prefix: factory
  uri: https://1factory.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ID
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: altPartNumber
  type: string
- container: ''
  name: altPartNumber2
  type: string
- container: ''
  name: altRev
  type: string
- container: ''
  name: altRev2
  type: string
- container: ''
  name: approvalStatus
  type: string
- container: ''
  name: blnNo
  type: string
- container: ''
  name: bonus
  type: decimal
- container: ''
  name: bonusTolerance
  type: string
- container: ''
  name: causedBy
  type: string
- container: ''
  name: certification
  type: string
- container: set
  name: certifications
  type: string
- container: ''
  name: characteristic
  type: string
- container: ''
  name: characteristicType
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: closedOn
  type: string
- container: ''
  name: comments
  type: string
- container: set
  name: commodityCodes
  type: string
- container: set
  name: componentParts
  type: string
- container: ''
  name: cost
  type: double
- container: ''
  name: country
  type: string
- container: ''
  name: createdByName
  type: string
- container: ''
  name: createdOn
  type: string
- container: ''
  name: customerIdent
  type: string
- container: ''
  name: customerName
  type: string
- container: ''
  name: dataType
  type: string
- container: ''
  name: date
  type: dateTime
- container: ''
  name: defectiveQuantity
  type: decimal
- container: ''
  name: descriptorDatum
  type: string
- container: ''
  name: detectedAt
  type: string
- container: ''
  name: dimensionType
  type: string
- container: ''
  name: direct
  type: boolean
- container: ''
  name: expirationDate
  type: dateTime
- container: ''
  name: faiType
  type: string
- container: ''
  name: frequency
  type: integer
- container: ''
  name: grpIdent
  type: string
- container: ''
  name: hasPpap
  type: boolean
- container: ''
  name: id
  type: integer
- container: ''
  name: impact
  type: string
- container: ''
  name: inSpecPct
  type: double
- container: ''
  name: indirect
  type: boolean
- container: ''
  name: inspIdent1
  type: string
- container: ''
  name: inspIdent2
  type: string
- container: ''
  name: inspIdent3
  type: string
- container: ''
  name: inspectedByName
  type: string
- container: ''
  name: inspectedOn
  type: dateTime
- container: ''
  name: inspectionMethod
  type: string
- container: ''
  name: inspectionQuantity
  type: decimal
- container: ''
  name: inspectionStatus
  type: string
- container: ''
  name: inspectionType
  type: string
- container: ''
  name: isAssembly
  type: boolean
- container: ''
  name: isBuy
  type: boolean
- container: ''
  name: isItar
  type: boolean
- container: ''
  name: isKey
  type: boolean
- container: ''
  name: isLibrary
  type: boolean
- container: ''
  name: isSpecLib
  type: boolean
- container: ''
  name: isTabulated
  type: boolean
- container: ''
  name: label
  type: string
- container: ''
  name: lastQualificationDate
  type: dateTime
- container: ''
  name: lotQuantity
  type: decimal
- container: ''
  name: lotSize
  type: string
- container: ''
  name: lowerSpecLimit
  type: decimal
- container: ''
  name: machines
  type: string
- container: set
  name: measurements
  type: reference
- container: ''
  name: mfgInspIdent1
  type: string
- container: ''
  name: mfgInspIdent2
  type: string
- container: ''
  name: ncrCount
  type: decimal
- container: set
  name: ncrs
  type: string
- container: ''
  name: nominal
  type: decimal
- container: ''
  name: notes
  type: string
- container: ''
  name: number
  type: decimal
- container: ''
  name: numberOfParts
  type: string
- container: ''
  name: operation
  type: string
- container: set
  name: organizationCodes
  type: string
- container: ''
  name: owner
  type: string
- container: ''
  name: parentPartNumber
  type: string
- container: ''
  name: parentRev
  type: string
- container: ''
  name: partDescription
  type: string
- container: ''
  name: partNumber
  type: string
- container: ''
  name: partsFailed
  type: string
- container: ''
  name: partsPassed
  type: string
- container: ''
  name: place
  type: integer
- container: ''
  name: planCount
  type: decimal
- container: ''
  name: postalCode
  type: string
- container: ''
  name: problemSummary
  type: string
- container: ''
  name: problemType
  type: string
- container: ''
  name: projectIdentifier
  type: string
- container: ''
  name: purchasing
  type: string
- container: ''
  name: qualificationStatus
  type: string
- container: set
  name: qualifications
  type: string
- container: ''
  name: quantity
  type: decimal
- container: ''
  name: reQualificationDate
  type: dateTime
- container: ''
  name: recInspIdent1
  type: string
- container: ''
  name: recInspIdent2
  type: string
- container: ''
  name: referencedFeature
  type: string
- container: ''
  name: rev
  type: string
- container: ''
  name: reviewStatus
  type: string
- container: ''
  name: reviewedByName
  type: string
- container: ''
  name: reviewedOn
  type: dateTime
- container: ''
  name: rootCause
  type: string
- container: ''
  name: rowIdent
  type: string
- container: ''
  name: samplingRule
  type: string
- container: ''
  name: sheetZone
  type: string
- container: ''
  name: site
  type: string
- container: ''
  name: smallBusiness
  type: boolean
- container: set
  name: specifications
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: strategic
  type: boolean
- container: ''
  name: street
  type: string
- container: ''
  name: subParts
  type: string
- container: ''
  name: supplierIdent
  type: string
- container: ''
  name: supplierName
  type: string
- container: ''
  name: supplierNumber
  type: string
- container: ''
  name: supplierQualityManager
  type: string
- container: ''
  name: supplyChainManager
  type: string
- container: ''
  name: taskCount
  type: decimal
- container: ''
  name: taskStatus
  type: string
- container: ''
  name: totalCost
  type: decimal
- container: ''
  name: type
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: updatedOn
  type: string
- container: ''
  name: upperSpecLimit
  type: decimal
- container: ''
  name: value
  type: decimal
- container: ''
  name: vendorCode
  type: string
- container: ''
  name: versionStatus
  type: string
property_count: 127
provider_name: 1Factory
provider_slug: 1factory
slug: 1factory-context
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
- JSON-LD
- Linked Data
- Semantic Web
---

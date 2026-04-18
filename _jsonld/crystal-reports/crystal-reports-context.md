---
class_count: 22
classes:
- DataSource
- Error
- FileFormatVersion
- Formula
- GrandTotalCollection
- GroupCondition
- InfostoreEntry
- InfostoreEntryList
- InstanceForm
- LogonRequest
- LogonResponse
- ODataFieldValue
- ODataRowCollection
- ODataServiceDocument
- ReportInstance
- ReportParameter
- ReportStructure
- ReportSummary
- RunningTotal
- Subreport
- SummaryField
- UsedField
context_file: json-ld/crystal-reports-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/crystal-reports/refs/heads/main/json-ld/crystal-reports-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Crystal Reports from Crystal Reports.
layout: jsonld
name: Crystal Reports Context
namespaces:
- prefix: cr
  uri: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ConnectionInfo
  type: string
- container: set
  name: EntitySets
  type: string
- container: ''
  name: SuppressData
  type: boolean
- container: ''
  name: __count
  type: string
- container: ''
  name: __next
  type: string
- container: ''
  name: auth
  type: string
- container: ''
  name: author
  type: string
- container: ''
  name: comments
  type: string
- container: ''
  name: cuid
  type: string
- container: ''
  name: databaseName
  type: string
- container: set
  name: datasources
  type: string
- container: ''
  name: default_value
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: direction
  type: string
- container: ''
  name: edit_uri
  type: string
- container: set
  name: entries
  type: string
- container: ''
  name: error_code
  type: integer
- container: ''
  name: export_uri
  type: string
- container: ''
  name: field
  type: string
- container: ''
  name: fieldName
  type: string
- container: ''
  name: file_format_version
  type: string
- container: set
  name: formulas
  type: string
- container: set
  name: groupconditions
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: keywords
  type: string
- container: ''
  name: last_data_refresh_date
  type: dateTime
- container: ''
  name: logonToken
  type: string
- container: ''
  name: major_version
  type: integer
- container: ''
  name: message
  type: string
- container: ''
  name: minor_version
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: operation
  type: string
- container: set
  name: parameters
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: prompt
  type: string
- container: ''
  name: report_name
  type: string
- container: ''
  name: report_title
  type: string
- container: ''
  name: required
  type: boolean
- container: ''
  name: reset_condition
  type: string
- container: ''
  name: resource
  type: string
- container: set
  name: runningtotals
  type: string
- container: ''
  name: serverName
  type: string
- container: ''
  name: service_uri
  type: string
- container: ''
  name: subject
  type: string
- container: set
  name: subreports
  type: string
- container: set
  name: summary
  type: string
- container: ''
  name: table
  type: string
- container: set
  name: tables
  type: string
- container: ''
  name: text
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: uri
  type: string
- container: set
  name: usedfields
  type: string
- container: ''
  name: userName
  type: string
- container: set
  name: value
  type: string
property_count: 54
provider_name: Crystal Reports
provider_slug: crystal-reports
slug: crystal-reports-context
tags:
- Business Intelligence
- Crystal Reports
- Data Analytics
- Enterprise Software
- Reporting
- SAP
- JSON-LD
- Linked Data
- Semantic Web
---

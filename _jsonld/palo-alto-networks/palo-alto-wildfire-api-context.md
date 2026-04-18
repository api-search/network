---
class_count: 6
classes:
- AnalysisReport
- BulkVerdictResponse
- SandboxReport
- SubmitResponse
- VerdictResponse
- report
context_file: json-ld/palo-alto-wildfire-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-wildfire-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Wildfire Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Wildfire Api Context
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
- container: ''
  name: createTime
  type: dateTime
- container: set
  name: dns
  type: reference
- container: set
  name: entry
  type: reference
- container: ''
  name: fileInfo
  type: reference
- container: ''
  name: fileStype
  type: string
- container: ''
  name: filename
  type: string
- container: ''
  name: filetype
  type: string
- container: ''
  name: fileurl
  type: string
- container: ''
  name: get-verdict-info
  type: reference
- container: ''
  name: get-verdicts-info
  type: reference
- container: set
  name: http
  type: reference
- container: ''
  name: md5
  type: string
- container: ''
  name: network
  type: reference
- container: ''
  name: platform
  type: string
- container: set
  name: process
  type: reference
- container: ''
  name: processList
  type: reference
- container: ''
  name: sha256
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: software
  type: string
- container: ''
  name: summary
  type: reference
- container: ''
  name: taskInfo
  type: reference
- container: set
  name: tcp
  type: reference
- container: ''
  name: upload-file-info
  type: reference
- container: ''
  name: url
  type: string
- container: ''
  name: verdict
  type: integer
- container: ''
  name: version
  type: string
- container: ''
  name: wildfire
  type: reference
property_count: 27
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-wildfire-api-context
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

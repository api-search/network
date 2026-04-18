---
class_count: 17
classes:
- Address
- AddressGroup
- AddressGroupList
- AddressGroupRequest
- AddressList
- AddressRequest
- DeleteResponse
- Job
- NatRule
- NatRuleList
- NatRuleRequest
- SecurityRule
- SecurityRuleList
- SecurityRuleRequest
- Service
- ServiceList
- ServiceRequest
context_file: json-ld/palo-alto-strata-cloud-manager-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-strata-cloud-manager-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Strata Cloud Manager Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Strata Cloud Manager Api Context
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
  name: action
  type: string
- container: set
  name: application
  type: string
- container: ''
  name: biDirectional
  type: boolean
- container: set
  name: category
  type: string
- container: set
  name: data
  type: reference
- container: ''
  name: description
  type: string
- container: set
  name: destination
  type: string
- container: ''
  name: destinationTranslation
  type: reference
- container: ''
  name: details
  type: reference
- container: ''
  name: disabled
  type: boolean
- container: ''
  name: dynamic
  type: reference
- container: ''
  name: dynamicIpAndPort
  type: reference
- container: ''
  name: endTs
  type: dateTime
- container: ''
  name: filter
  type: string
- container: ''
  name: folder
  type: string
- container: ''
  name: fqdn
  type: string
- container: set
  name: from
  type: string
- container: set
  name: group
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: ipNetmask
  type: string
- container: ''
  name: ipRange
  type: string
- container: ''
  name: ipWildcard
  type: string
- container: ''
  name: limit
  type: integer
- container: ''
  name: logSetting
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: natType
  type: string
- container: ''
  name: offset
  type: integer
- container: ''
  name: percent
  type: integer
- container: ''
  name: port
  type: string
- container: ''
  name: position
  type: string
- container: ''
  name: profileSetting
  type: reference
- container: ''
  name: protocol
  type: reference
- container: ''
  name: result
  type: string
- container: ''
  name: service
  type: string
- container: ''
  name: snippet
  type: string
- container: set
  name: source
  type: string
- container: ''
  name: sourcePort
  type: string
- container: ''
  name: sourceTranslation
  type: reference
- container: set
  name: sourceUser
  type: string
- container: ''
  name: startTs
  type: dateTime
- container: set
  name: static
  type: string
- container: ''
  name: staticIp
  type: reference
- container: ''
  name: status
  type: string
- container: set
  name: tag
  type: string
- container: ''
  name: tcp
  type: reference
- container: set
  name: to
  type: string
- container: ''
  name: total
  type: integer
- container: set
  name: translatedAddress
  type: string
- container: ''
  name: translatedPort
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: udp
  type: reference
property_count: 51
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-strata-cloud-manager-api-context
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

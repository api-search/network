---
class_count: 6
classes:
- GetStoresUnderAccountRequest
- GetStoresUnderAccountResponse
- GetTerminalDetailsRequest
- GetTerminalDetailsResponse
- GetTerminalsUnderAccountRequest
- GetTerminalsUnderAccountResponse
context_file: json-ld/adyen-pos-terminal-get-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-pos-terminal-get-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Pos Terminal Get from Adyen.
layout: jsonld
name: Adyen Pos Terminal Get Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: companyAccount
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: set
  name: stores
  type: string
- container: ''
  name: terminal
  type: string
- container: ''
  name: bluetoothIp
  type: string
- container: ''
  name: bluetoothMac
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: deviceModel
  type: string
- container: ''
  name: dhcpEnabled
  type: boolean
- container: ''
  name: displayLabel
  type: string
- container: ''
  name: ethernetIp
  type: string
- container: ''
  name: ethernetMac
  type: string
- container: ''
  name: firmwareVersion
  type: string
- container: ''
  name: iccid
  type: string
- container: ''
  name: lastActivityDateTime
  type: dateTime
- container: ''
  name: lastTransactionDateTime
  type: dateTime
- container: ''
  name: linkNegotiation
  type: string
- container: ''
  name: merchantInventory
  type: boolean
- container: ''
  name: permanentTerminalId
  type: string
- container: ''
  name: serialNumber
  type: string
- container: ''
  name: simStatus
  type: string
- container: ''
  name: store
  type: string
- container: ''
  name: storeDetails
  type: string
- container: ''
  name: terminalStatus
  type: string
- container: ''
  name: wifiIp
  type: string
- container: ''
  name: wifiMac
  type: string
- container: set
  name: inventoryTerminals
  type: string
- container: set
  name: merchantAccounts
  type: string
property_count: 28
provider_name: Adyen
provider_slug: adyen
slug: adyen-pos-terminal-get-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---

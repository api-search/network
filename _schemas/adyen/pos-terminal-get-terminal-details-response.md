---
description: GetTerminalDetailsResponse schema from Adyen API
layout: schema
name: GetTerminalDetailsResponse
properties_list:
- description: The Bluetooth IP address of the terminal.
  name: bluetoothIp
  type: string
- description: The Bluetooth MAC address of the terminal.
  name: bluetoothMac
  type: string
- description: The company account that the terminal is associated with. If this is the only account level shown in the response, the terminal is assigned to the inventory of the company account.
  name: companyAccount
  type: string
- description: The country where the terminal is used.
  name: country
  type: string
- description: The model name of the terminal.
  name: deviceModel
  type: string
- description: Indicates whether assigning IP addresses through a DHCP server is enabled on the terminal.
  name: dhcpEnabled
  type: boolean
- description: The label shown on the status bar of the display. This label (if any) is specified in your Customer Area.
  name: displayLabel
  type: string
- description: The terminal's IP address in your Ethernet network.
  name: ethernetIp
  type: string
- description: The terminal's MAC address in your Ethernet network.
  name: ethernetMac
  type: string
- description: The software release currently in use on the terminal.
  name: firmwareVersion
  type: string
- description: The integrated circuit card identifier (ICCID) of the SIM card in the terminal.
  name: iccid
  type: string
- description: Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago.
  name: lastActivityDateTime
  type: string
- description: Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago.
  name: lastTransactionDateTime
  type: string
- description: 'The Ethernet link negotiation that the terminal uses: - `auto`: Auto-negotiation - `100full`: 100 Mbps full duplex'
  name: linkNegotiation
  type: string
- description: The merchant account that the terminal is associated with. If the response doesn't contain a `store` the terminal is assigned to this merchant account.
  name: merchantAccount
  type: string
- description: Boolean that indicates if the terminal is assigned to the merchant inventory. This is returned when the terminal is assigned to a merchant account. - If **true**, this indicates that the terminal is i
  name: merchantInventory
  type: boolean
- description: The permanent terminal ID.
  name: permanentTerminalId
  type: string
- description: The serial number of the terminal.
  name: serialNumber
  type: string
- description: 'On a terminal that supports 3G or 4G connectivity, indicates the status of the SIM card in the terminal: ACTIVE or INVENTORY.'
  name: simStatus
  type: string
- description: The store code of the store that the terminal is assigned to.
  name: store
  type: string
- description: The store that the terminal is assigned to.
  name: storeDetails
  type: object
- description: The unique terminal ID.
  name: terminal
  type: string
- description: 'The status of the terminal: - `OnlineToday`, `OnlineLast1Day`, `OnlineLast2Days` etcetera to `OnlineLast7Days`: Indicates when in the past week the terminal was last online. - `SwitchedOff`: Indicates'
  name: terminalStatus
  type: string
- description: The terminal's IP address in your Wi-Fi network.
  name: wifiIp
  type: string
- description: The terminal's MAC address in your Wi-Fi network.
  name: wifiMac
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-get-terminal-details-response-schema.json
slug: pos-terminal-get-terminal-details-response
tags:
- Payments
- Financial Services
- Fintech
title: GetTerminalDetailsResponse
---

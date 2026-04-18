---
description: NetScaler appliance configuration including network settings, system parameters, and operational options.
layout: schema
name: NsConfig
properties_list:
- description: The NetScaler IP (NSIP) address of the appliance. This is the primary management IP address.
  name: ipaddress
  type: string
- description: Subnet mask associated with the NSIP address.
  name: netmask
  type: string
- description: VLAN ID for the NSIP address. Range 2-4094.
  name: nsvlan
  type: integer
- description: Network interfaces bound to the NSVLAN. Format is slot/port (e.g., 1/1).
  name: ifnum
  type: string
- description: Whether the NSVLAN is tagged or untagged.
  name: tagged
  type: string
- description: HTTP port(s) on the appliance. Default is 80.
  name: httpport
  type: array
- description: Maximum number of connections per service. Zero means unlimited.
  name: maxconn
  type: integer
- description: Maximum number of requests per connection. Zero means unlimited.
  name: maxreq
  type: integer
- description: Whether to insert the client IP address into the HTTP header of requests forwarded to the service.
  name: cip
  type: string
- description: Name of the HTTP header used to insert the client IP address when CIP is enabled.
  name: cipheader
  type: string
- description: Version of the cookie inserted by the NetScaler for persistence.
  name: cookieversion
  type: string
- description: Whether the secure flag is set on persistence cookies.
  name: securecookie
  type: string
- description: Minimum path MTU value. Range 168-1500.
  name: pmtumin
  type: integer
- description: Timeout in minutes for path MTU discovery. Range 1-1440.
  name: pmtutimeout
  type: integer
- description: Port range for FTP data connections (e.g., 1024-65535).
  name: ftpportrange
  type: string
- description: Time zone setting for the appliance (e.g., GMT+05:30-IST-Asia/Kolkata).
  name: timezone
  type: string
- description: Percentage of shared quota to be granted at a time for max client connections.
  name: grantquotamaxclient
  type: integer
- description: Percentage of shared quota to be granted at a time for spillover threshold.
  name: grantquotaspillover
  type: integer
- description: Port range for cache redirection.
  name: crportrange
  type: string
- description: The type of the NetScaler appliance.
  name: systemtype
  type: string
- description: Primary IP address of the HA pair.
  name: primaryip
  type: string
- description: Primary IPv6 address of the HA pair.
  name: primaryip6
  type: string
- description: Internal flags for the configuration.
  name: flags
  type: integer
- description: Timestamp of the last configuration change.
  name: lastconfigchangedtime
  type: string
- description: Timestamp of the last configuration save.
  name: lastconfigsavetime
  type: string
- description: Current system time on the appliance.
  name: currentsytemtime
  type: string
- description: Current system time as epoch seconds.
  name: systemtime
  type: integer
- description: Whether the running configuration has unsaved changes.
  name: configchanged
  type: boolean
- description: Mapped IP address for the NSIP.
  name: mappedip
  type: string
- description: Number of consecutive IP addresses in the range beginning with the mapped IP.
  name: range
  type: integer
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-ns-config-schema.json
slug: citrix-netscaler-nitro-ns-config
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: NsConfig
---

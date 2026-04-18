---
description: A system file on the NetScaler appliance.
layout: schema
name: SystemFile
properties_list:
- description: Name of the file.
  name: filename
  type: string
- description: Location of the file on the appliance filesystem (e.g., /nsconfig/ssl).
  name: filelocation
  type: string
- description: Base64-encoded file content. Used when uploading files.
  name: filecontent
  type: string
- description: Encoding of the file content.
  name: fileencoding
  type: string
- description: Last access time of the file.
  name: fileaccesstime
  type: string
- description: Last modification time of the file.
  name: filemodifiedtime
  type: string
- description: File permissions mode.
  name: filemode
  type: string
- description: Size of the file in bytes.
  name: filesize
  type: integer
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-system-file-schema.json
slug: citrix-netscaler-nitro-system-file
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: SystemFile
---

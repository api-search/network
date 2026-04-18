---
description: Schema for the integration YAML manifest file used by Cortex XSOAR (formerly Demisto) and Cortex XSIAM content packs. The manifest defines the integration identity, configuration parameters, commands, arguments, outputs, and execution runtime settings. Integration packs are published to the Cortex Marketplace and can be developed using the demisto-sdk CLI toolchain. Each integration enables XSOAR playbooks and automation scripts to interact with third-party security products and services.
layout: schema
name: Cortex XSOAR Integration Manifest
properties_list:
- description: Internal name of the integration used as a unique identifier within the content pack. Must match the filename of the integration Python or JavaScript file and be consistent across all related pack fil
  name: name
  type: string
- description: Human-readable display name shown in the XSOAR UI integration list, War Room context, and Cortex Marketplace listing. Should clearly identify the product or service the integration connects to.
  name: display
  type: string
- description: Integration category used for Cortex Marketplace classification, filtering, and discovery. Determines which Marketplace category page the integration appears under.
  name: category
  type: string
- description: 'Short description of the integration''s purpose and primary capabilities. Displayed in the integration list and Marketplace search results. Should summarize what the integration does and which product '
  name: description
  type: string
- description: Detailed markdown-formatted description displayed on the Cortex Marketplace product page. Should include prerequisites, authentication setup instructions, API version compatibility, and notable limita
  name: detaileddescription
  type: string
- description: Base64-encoded PNG image used as the integration icon in the XSOAR UI and Marketplace. Should be a square image, typically 120x120 pixels, representing the integrated product or vendor logo.
  name: image
  type: string
- description: Execution runtime type for the integration script. 'python2' uses Python 2.7 (deprecated). 'python3' uses Python 3.x in a Docker container. 'javascript' runs natively in the XSOAR engine without Docke
  name: type
  type: string
- description: 'List of instance configuration parameters displayed in the XSOAR integration settings UI. Each parameter corresponds to a field the user must fill in when configuring an integration instance, such as '
  name: configuration
  type: array
- description: Script execution settings, runtime configuration, and command definitions exposed by this integration. Defines the integration's behavioral capabilities and available actions.
  name: script
  type: object
- description: Minimum XSOAR or XSIAM platform version required to use this integration (e.g., '6.0.0', '8.4.0'). The integration will not be available on older platform versions.
  name: fromversion
  type: string
- description: Maximum XSOAR or XSIAM platform version this integration is compatible with. Used to deprecate integrations that are superseded by newer versions targeting later platforms.
  name: toversion
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-integration-manifest-schema.json
slug: cortex-xsoar-integration-manifest
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Cortex XSOAR Integration Manifest
---

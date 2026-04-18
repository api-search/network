---
description: A ServiceNow CMDB configuration item record representing a hardware, software, or service component tracked in the Configuration Management Database.
layout: schema
name: ServiceNow Configuration Item
properties_list:
- description: The unique 32-character system identifier for the configuration item.
  name: sys_id
  type: string
- description: The display name of the configuration item.
  name: name
  type: string
- description: The CMDB class name identifying the type of CI, such as cmdb_ci_server, cmdb_ci_appl, or cmdb_ci_service.
  name: sys_class_name
  type: string
- description: The category of the configuration item.
  name: category
  type:
  - string
  - 'null'
- description: The subcategory of the configuration item.
  name: subcategory
  type:
  - string
  - 'null'
- description: A brief description of the configuration item.
  name: short_description
  type:
  - string
  - 'null'
- description: 'The operational status: 1=Operational, 2=Non-Operational, 3=Repair in Progress, 4=DR Standby, 5=Ready, 6=Retired.'
  name: operational_status
  type: string
- description: 'The install status: 1=Installed, 2=In Maintenance, 3=Pending Install, 4=Pending Repair, 5=In Stock, 6=Retired, 7=Stolen, 8=Absent, 100=On Order.'
  name: install_status
  type: string
- description: The serial number of the hardware asset.
  name: serial_number
  type:
  - string
  - 'null'
- description: The asset tag identifier.
  name: asset_tag
  type:
  - string
  - 'null'
- description: The IP address of the CI.
  name: ip_address
  type:
  - string
  - 'null'
- description: The MAC address of the CI.
  name: mac_address
  type:
  - string
  - 'null'
- description: The DNS domain of the CI.
  name: dns_domain
  type:
  - string
  - 'null'
- description: The fully qualified domain name.
  name: fqdn
  type:
  - string
  - 'null'
- description: The operating system installed on the CI.
  name: os
  type:
  - string
  - 'null'
- description: The version of the operating system.
  name: os_version
  type:
  - string
  - 'null'
- description: The OS domain.
  name: os_domain
  type:
  - string
  - 'null'
- description: The CPU type.
  name: cpu_type
  type:
  - string
  - 'null'
- description: The number of CPUs.
  name: cpu_count
  type:
  - integer
  - 'null'
- description: The CPU speed in MHz.
  name: cpu_speed
  type:
  - number
  - 'null'
- description: The amount of RAM in MB.
  name: ram
  type:
  - integer
  - 'null'
- description: The total disk space in GB.
  name: disk_space
  type:
  - number
  - 'null'
- description: The manufacturer of the CI.
  name: manufacturer
  type: object
- description: The model of the CI.
  name: model_id
  type: object
- description: The model number.
  name: model_number
  type:
  - string
  - 'null'
- description: The vendor of the CI.
  name: vendor
  type: object
- description: The physical location of the CI.
  name: location
  type: object
- description: The department that owns the CI.
  name: department
  type: object
- description: The company that owns the CI.
  name: company
  type: object
- description: The user assigned to the CI.
  name: assigned_to
  type: object
- description: The user managing the CI.
  name: managed_by
  type: object
- description: The user who owns the CI.
  name: owned_by
  type: object
- description: The group responsible for supporting the CI.
  name: support_group
  type: object
- description: The user providing primary support for the CI.
  name: supported_by
  type: object
- description: The source that discovered or populated this CI.
  name: discovery_source
  type:
  - string
  - 'null'
- description: When the CI was first discovered.
  name: first_discovered
  type:
  - string
  - 'null'
- description: When the CI was last discovered.
  name: last_discovered
  type:
  - string
  - 'null'
- description: Whether the CI can print.
  name: can_print
  type: boolean
- description: Whether the CI is unverified.
  name: unverified
  type: boolean
- description: The date and time the record was created.
  name: sys_created_on
  type: string
- description: The user who created the record.
  name: sys_created_by
  type: string
- description: The date and time the record was last updated.
  name: sys_updated_on
  type: string
- description: The user who last updated the record.
  name: sys_updated_by
  type: string
- description: The number of times the record has been modified.
  name: sys_mod_count
  type: integer
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-configuration-item-schema.json
slug: servicenow-configuration-item
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: ServiceNow Configuration Item
---

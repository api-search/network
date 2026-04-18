---
description: A full CMDB configuration item record. Fields vary by CI class but common attributes are included below.
layout: schema
name: CmdbInstance
properties_list:
- description: Unique identifier for the configuration item.
  name: sys_id
  type: string
- description: The display name of the configuration item.
  name: name
  type: string
- description: The CMDB class name for this CI.
  name: sys_class_name
  type: string
- description: The category of the CI.
  name: category
  type: string
- description: The subcategory of the CI.
  name: subcategory
  type: string
- description: The operational status of the CI.
  name: operational_status
  type: string
- description: The installation status of the CI.
  name: install_status
  type: string
- description: The serial number of the hardware asset.
  name: serial_number
  type: string
- description: The asset tag identifier.
  name: asset_tag
  type: string
- description: The IP address of the CI.
  name: ip_address
  type: string
- description: The MAC address of the CI.
  name: mac_address
  type: string
- description: The DNS domain of the CI.
  name: dns_domain
  type: string
- description: The fully qualified domain name.
  name: fqdn
  type: string
- description: The operating system.
  name: os
  type: string
- description: The operating system version.
  name: os_version
  type: string
- description: The sys_id of the manufacturer.
  name: manufacturer
  type: string
- description: The sys_id of the model.
  name: model_id
  type: string
- description: The sys_id of the CI location.
  name: location
  type: string
- description: The sys_id of the department.
  name: department
  type: string
- description: The sys_id of the owning company.
  name: company
  type: string
- description: The sys_id of the assigned user.
  name: assigned_to
  type: string
- description: The sys_id of the managing user.
  name: managed_by
  type: string
- description: The sys_id of the owner.
  name: owned_by
  type: string
- description: The sys_id of the support group.
  name: support_group
  type: string
- description: The date and time when the CI was created.
  name: sys_created_on
  type: string
- description: The date and time when the CI was last updated.
  name: sys_updated_on
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-cmdb-instance-cmdb-instance-schema.json
slug: servicenow-cmdb-instance-cmdb-instance
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
title: CmdbInstance
---

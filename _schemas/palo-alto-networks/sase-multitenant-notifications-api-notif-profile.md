---
description: NotifProfile schema from Multi-Tenant Notifications API
layout: schema
name: NotifProfile
properties_list:
- description: Notification Profile Id
  name: id
  type: string
- description: Notification Profile Name
  name: profileName
  type: string
- description: Notification Profile Description
  name: description
  type: string
- description: Notification Profile Operational State
  name: opState
  type: string
- description: Notification Profile Status
  name: status
  type: string
- description: Input Tenant List
  name: tenantList
  type: array
- description: List of excluded tenants
  name: excludeTenantList
  type: array
- description: Notification Type Detail
  name: notifTypeDetails
  type: array
- description: Notification Channel List
  name: notifChannels
  type: array
- description: List of child tenants that got the incident profile
  name: successTenant
  type: array
- description: List of child tenants that didn't get the incident profile
  name: failureTenant
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-multitenant-notifications-api-notif-profile-schema.json
slug: sase-multitenant-notifications-api-notif-profile
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: NotifProfile
---

---
description: A Google Workspace organizational unit. JSON representation of an org unit resource from the Admin SDK Directory API. The hierarchy is limited to 35 levels of depth.
layout: schema
name: OrgUnit
properties_list:
- description: The type of the API resource.
  name: kind
  type: string
- description: ETag of the resource.
  name: etag
  type: string
- description: The organizational unit path name. For example, an organizational unit with parent path /corp and name sales is derived as /corp/sales.
  name: name
  type: string
- description: Description of the organizational unit.
  name: description
  type: string
- description: The full path to the organizational unit. The orgUnitPath is a derived property. When listed, it is derived from parentOrgUnitPath and the organizational unit name.
  name: orgUnitPath
  type: string
- description: The unique ID of the organizational unit.
  name: orgUnitId
  type: string
- description: The organizational unit path of the parent organizational unit. Required unless parentOrgUnitId is set.
  name: parentOrgUnitPath
  type: string
- description: The unique ID of the parent organizational unit. Required unless parentOrgUnitPath is set.
  name: parentOrgUnitId
  type: string
- description: Deprecated. Setting this field has no effect.
  name: blockInheritance
  type: boolean
provider_name: Google Workspace
provider_slug: google-workspace
schema_file: json-schema/admin-sdk-directory-org-unit-schema.json
slug: admin-sdk-directory-org-unit
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
title: OrgUnit
---

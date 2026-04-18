---
description: A protected range.
layout: schema
name: ProtectedRange
properties_list:
- description: The ID of the protected range.
  name: protectedRangeId
  type: integer
- description: The named range this protected range is backed by, if any.
  name: namedRangeId
  type: string
- description: The description of this protected range.
  name: description
  type: string
- description: True if this protected range will show a warning when editing.
  name: warningOnly
  type: boolean
- description: True if the user who requested this protected range can edit the protected area.
  name: requestingUserCanEdit
  type: boolean
- description: The list of unprotected ranges within a protected sheet.
  name: unprotectedRanges
  type: array
- description: The users and groups with edit access to the protected range.
  name: editors
  type: object
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-protected-range-schema.json
slug: google-sheets-protected-range
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: ProtectedRange
---

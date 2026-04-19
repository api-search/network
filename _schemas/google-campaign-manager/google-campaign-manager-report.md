---
description: A Campaign Manager 360 report configuration. Reports provide performance data and analytics for campaigns, ads, placements, and other advertising dimensions.
layout: schema
name: Report
properties_list:
- description: Report ID. Read-only, auto-generated field.
  name: id
  type: string
- description: The user profile ID of the owner of this report.
  name: ownerProfileId
  type: string
- description: The account ID this report belongs to.
  name: accountId
  type: string
- description: The subaccount ID this report belongs to.
  name: subAccountId
  type: string
- description: The name of the report.
  name: name
  type: string
- description: The filename used when generating report files for this report.
  name: fileName
  type: string
- description: The type of report.
  name: type
  type: string
- description: The output format of the report.
  name: format
  type: string
- description: Etag of this resource.
  name: etag
  type: string
- description: The timestamp (in milliseconds since epoch) of when this report was last modified.
  name: lastModifiedTime
  type: string
- description: Identifies what kind of resource this is. Value is always dfareporting#report.
  name: kind
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-report-schema.json
slug: google-campaign-manager-report
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: Report
---

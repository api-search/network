---
description: An audience export is a list of users in an audience at the time of the list's creation. One audience may have multiple audience exports created for different days.
layout: schema
name: AudienceExport
properties_list:
- description: 'Required. The audience resource name. This resource name identifies the audience being listed and is shared between the Analytics Data & Admin APIs. Format: `properties/{property}/audiences/{audience}'
  name: audience
  type: string
- description: Output only. The descriptive display name for this audience. For example, "Purchasers".
  name: audienceDisplayName
  type: string
- description: Output only. The time when CreateAudienceExport was called and the AudienceExport began the `CREATING` state.
  name: beginCreatingTime
  type: string
- description: Output only. The total quota tokens charged during creation of the AudienceExport. Because this token count is based on activity from the `CREATING` state, this tokens charged will be fixed once an Au
  name: creationQuotaTokensCharged
  type: integer
- description: Required. The dimensions requested and displayed in the query response.
  name: dimensions
  type: array
- description: Output only. Error message is populated when an audience export fails during creation. A common reason for such a failure is quota exhaustion.
  name: errorMessage
  type: string
- description: 'Output only. Identifier. The audience export resource name assigned during creation. This resource name identifies this `AudienceExport`. Format: `properties/{property}/audienceExports/{audience_expor'
  name: name
  type: string
- description: Output only. The percentage completed for this audience export ranging between 0 to 100.
  name: percentageCompleted
  type: number
- description: Output only. The total number of rows in the AudienceExport result.
  name: rowCount
  type: integer
- description: Output only. The current state for this AudienceExport.
  name: state
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-audience-export-schema.json
slug: data-api-audience-export
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: AudienceExport
---

---
description: A Power BI dataset representing a data model
layout: schema
name: Dataset
properties_list:
- description: The unique identifier of the dataset
  name: id
  type: string
- description: The display name of the dataset
  name: name
  type: string
- description: Whether the push API is enabled for this dataset
  name: addRowsAPIEnabled
  type: boolean
- description: The user who configured the dataset
  name: configuredBy
  type: string
- description: Whether the dataset can be refreshed
  name: isRefreshable
  type: boolean
- description: Whether effective identity is required for embedding
  name: isEffectiveIdentityRequired
  type: boolean
- description: Whether RLS roles are required for embedding
  name: isEffectiveIdentityRolesRequired
  type: boolean
- description: Whether an on-premises gateway is required
  name: isOnPremGatewayRequired
  type: boolean
- description: The storage mode of the dataset
  name: targetStorageMode
  type: string
- description: URL to create an embedded report on this dataset
  name: createReportEmbedURL
  type: string
- description: URL for the Q&A embedded experience
  name: qnaEmbedURL
  type: string
- description: The web URL of the dataset
  name: webUrl
  type: string
- description: The date and time the dataset was created
  name: createdDate
  type: string
- description: The content provider type
  name: contentProviderType
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-dataset-schema.json
slug: power-bi-rest-dataset
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Dataset
---

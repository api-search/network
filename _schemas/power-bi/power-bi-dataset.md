---
description: Schema for a Power BI dataset resource as returned by the Power BI REST API. A dataset represents the data model that underpins reports and dashboards, including tables, columns, measures, relationships, and data source configuration.
layout: schema
name: Power BI Dataset
properties_list:
- description: The unique identifier of the dataset, assigned by the Power BI service
  name: id
  type: string
- description: The display name of the dataset
  name: name
  type: string
- description: Whether the dataset supports the push rows API for real-time data ingestion
  name: addRowsAPIEnabled
  type: boolean
- description: The email address of the user who configured or last modified the dataset
  name: configuredBy
  type: string
- description: Whether the dataset supports scheduled or on-demand refresh
  name: isRefreshable
  type: boolean
- description: Whether an effective identity (row-level security identity) is required when generating embed tokens
  name: isEffectiveIdentityRequired
  type: boolean
- description: Whether RLS role specification is required in effective identity for embed tokens
  name: isEffectiveIdentityRolesRequired
  type: boolean
- description: Whether the dataset requires an on-premises data gateway to connect to its data sources
  name: isOnPremGatewayRequired
  type: boolean
- description: The storage mode that determines how data is stored and queried
  name: targetStorageMode
  type: string
- description: The default mode for push datasets
  name: defaultMode
  type: string
- description: The UTC date and time when the dataset was first created
  name: createdDate
  type: string
- description: The type of content provider that generated this dataset
  name: contentProviderType
  type: string
- description: The URL to create an embedded report connected to this dataset
  name: createReportEmbedURL
  type: string
- description: The URL for the Q&A natural language embedded experience
  name: qnaEmbedURL
  type: string
- description: The web URL for accessing the dataset in the Power BI service
  name: webUrl
  type: string
- description: The tables that make up the dataset schema
  name: tables
  type: array
- description: The relationships between tables in the dataset model
  name: relationships
  type: array
- description: The data sources used by the dataset
  name: datasources
  type: array
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-dataset-schema.json
slug: power-bi-dataset
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Power BI Dataset
---

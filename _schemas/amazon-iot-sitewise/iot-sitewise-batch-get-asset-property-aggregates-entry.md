---
description: <p>Contains information for an asset property aggregate entry that is associated with the <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html">BatchGetAssetPropertyAggregates</a> API.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html">UpdateAssetProperty</a>.</p> </li> </ul>
layout: schema
name: BatchGetAssetPropertyAggregatesEntry
properties_list:
- description: ''
  name: entryId
  type: object
- description: ''
  name: assetId
  type: object
- description: ''
  name: propertyId
  type: object
- description: ''
  name: propertyAlias
  type: object
- description: ''
  name: aggregateTypes
  type: object
- description: ''
  name: resolution
  type: object
- description: ''
  name: startDate
  type: object
- description: ''
  name: endDate
  type: object
- description: ''
  name: qualities
  type: object
- description: ''
  name: timeOrdering
  type: object
provider_name: Amazon IoT SiteWise
provider_slug: amazon-iot-sitewise
schema_file: json-schema/iot-sitewise-batch-get-asset-property-aggregates-entry-schema.json
slug: iot-sitewise-batch-get-asset-property-aggregates-entry
tags:
- AWS
- Asset Management
- Industrial IoT
- IoT
- Time Series Data
title: BatchGetAssetPropertyAggregatesEntry
---

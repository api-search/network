---
description: The `result` attribute in the Time-Series Non-Flattened Response Object will be a TIMESERIES object. A TIMESERIES object has a values attribute and a dates attribute that contain arrays of equal length so that the values and dates can be align to form a time series.
layout: schema
name: time_series_timeseries_object
properties_list:
- description: Representing the data returned from the requested FQL formula for the requestId
  name: values
  type: array
- description: Representing the dates corresponding the requested FQL formula for the requestId
  name: dates
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-formula-time_series_timeseries_object-schema.json
slug: factset-formula-time_series_timeseries_object
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: time_series_timeseries_object
---

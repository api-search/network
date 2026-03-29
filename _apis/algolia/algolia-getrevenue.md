---
aid: algolia:algolia-getrevenue
name: Retrieve revenue data
tags:
- analytics
- - Conversions
  - Revenue
  - Analytics
humanURL: 
properties: []
description: >-
  Retrieves revenue-related metrics, such as the total revenue or the average order value.  To retrieve revenue-related metrics, send purchase events. By default, the analyzed period includes the last eight days including the current day.  Revenue is based on purchase conversion events (a conversion event with an `eventSubtype` attribute of `purchase`). The revenue is the `price` attribute multiplied by the `quantity` attribute for each object in the event's `objectData` array.

---

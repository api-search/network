---
aid: algolia:algolia-getconversionrate
name: Retrieve conversion rate
tags:
- analytics
- - Conversions
  - Rates
  - Analytics
humanURL: 
properties: []
description: >-
  Retrieves the conversion rate (CR) for all your searches with at least one conversion event, including a daily breakdown.  By default, the analyzed period includes the last eight days including the current day.  **There's a difference between a 0 and null CR when `clickAnalytics` is enabled:**  - **Null** means there were no queries: since Algolia didn't receive any events, CR is null. - **0** mean there _were_ queries but no [conversion events](https://www.algolia.com/doc/guides/sending-even...

---

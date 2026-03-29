---
aid: bigcommerce:bigcommerce-upsertpricelistrecords
name: Upsert Price List Records
tags:
- Price Lists Records
humanURL: 
properties: []
description: >-
  Creates or updates *Price List Records*.   **Required Fields** * currency  **Notes** * Batch requests support up to 1,000 items per request. * Up to 2 concurrent batch upsert requests are supported with this API. Running more than the allowed concurrent requests in parallel on the **same store** will cause a `429` error, and your additional requests will fail. You are encouraged to run requests sequentially with as many records per request as possible to maximize performance. * When updating ...

---

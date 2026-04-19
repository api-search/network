---
description: 'Enables the ability to asynchronously "batch" the request, supporting a long-running request up to 10 minutes. Upon requesting batch=Y, the service will respond back with an HTTP Status Code of 202. Once a batch request is submitted, use the `batch/v1/status` to see if the job has completed. Once completed, retrieve the results of the request via `batch/v1/result`. <p>**Additional Access Required. To gain access to this feature, reach out to your FactSet Account team or "Report Issue" above and our support teams can assist.** Upon requesting "batch": "Y", the service will respond back with an HTTP Status Code of 202.'
layout: schema
name: batch
properties_list: []
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-batch-schema.json
slug: factset-prices-batch
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: batch
---

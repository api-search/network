---
description: Enables the ability to asynchronously "batch" the request, supporting a long-running request for up to 20 minutes. Upon requesting batch=Y, the service will respond back with an HTTP Status Code of 202. Once a batch request is submitted, use batch status to see if the job has been completed. Once completed, retrieve the results of the request via batch-result. When using Batch, ids limit is increased to 10000 ids per request, though limits on query string via GET method still apply. It's advised to submit large lists of ids via POST method. Please note that the number of unique currencies present in the requested ids is limited to 50 per request.
layout: schema
name: batch
properties_list: []
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-global-prices-batch-schema.json
slug: factset-global-prices-batch
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: batch
---

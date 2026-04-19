---
description: The requested company identifier. FactSet Identifiers, tickers, CUSIP, SEDOL, and ISIN are accepted inputs. <p>***ids limit** = 1000 per request*</p> *<p>Make note, GET Method URL request lines are also limited to a total length of 8192 bytes (8KB). In cases where the service allows for thousands of ids, which may lead to exceeding this request line limit of 8KB, its advised for any requests with large request lines to be requested through the respective "POST" method.</p>*
layout: schema
name: companyIds
properties_list: []
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-people-company-ids-schema.json
slug: factset-people-company-ids
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: companyIds
---

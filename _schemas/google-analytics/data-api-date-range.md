---
description: 'A contiguous set of days: `startDate`, `startDate + 1`, ..., `endDate`. Requests are allowed up to 4 date ranges.'
layout: schema
name: DateRange
properties_list:
- description: 'The inclusive end date for the query in the format `YYYY-MM-DD`. Cannot be before `start_date`. The format `NdaysAgo`, `yesterday`, or `today` is also accepted, and in that case, the date is inferred '
  name: endDate
  type: string
- description: Assigns a name to this date range. The dimension `dateRange` is valued to this name in a report response. If set, cannot begin with `date_range_` or `RESERVED_`. If not set, date ranges are named by t
  name: name
  type: string
- description: The inclusive start date for the query in the format `YYYY-MM-DD`. Cannot be after `end_date`. The format `NdaysAgo`, `yesterday`, or `today` is also accepted, and in that case, the date is inferred b
  name: startDate
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-date-range-schema.json
slug: data-api-date-range
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: DateRange
---

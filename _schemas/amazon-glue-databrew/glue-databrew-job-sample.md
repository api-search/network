---
description: A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a <code>JobSample</code> value isn't provided, the default is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.
layout: schema
name: JobSample
properties_list:
- description: ''
  name: Mode
  type: object
- description: ''
  name: Size
  type: object
provider_name: Amazon Glue DataBrew
provider_slug: amazon-glue-databrew
schema_file: json-schema/glue-databrew-job-sample-schema.json
slug: glue-databrew-job-sample
tags:
- AWS
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
title: JobSample
---

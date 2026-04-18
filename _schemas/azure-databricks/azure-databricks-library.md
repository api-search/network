---
description: ''
layout: schema
name: Library
properties_list:
- description: URI of the JAR library to install
  name: jar
  type: string
- description: URI of the egg library to install
  name: egg
  type: string
- description: URI of the wheel library to install
  name: whl
  type: string
- description: ''
  name: pypi
  type: object
- description: ''
  name: maven
  type: object
- description: ''
  name: cran
  type: object
- description: Path to a requirements.txt file. Only supported on clusters running Databricks Runtime 15.0+.
  name: requirements
  type: string
provider_name: Azure Databricks
provider_slug: azure-databricks
schema_file: json-schema/azure-databricks-library-schema.json
slug: azure-databricks-library
tags:
- Analytics
- Apache Spark
- Big Data
- Data Engineering
- Machine Learning
title: Library
---

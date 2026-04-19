---
description: <p>Represents an individual condition that evaluates to true or false.</p> <p>Conditions are used with recipe actions. The action is only performed for column values where the condition evaluates to true.</p> <p>If a recipe requires more than one condition, then the recipe must specify multiple <code>ConditionExpression</code> elements. Each condition is applied to the rows in a dataset first, before the recipe action is performed.</p>
layout: schema
name: ConditionExpression
properties_list:
- description: ''
  name: Condition
  type: object
- description: ''
  name: Value
  type: object
- description: ''
  name: TargetColumn
  type: object
provider_name: Amazon Glue DataBrew
provider_slug: amazon-glue-databrew
schema_file: json-schema/glue-databrew-condition-expression-schema.json
slug: glue-databrew-condition-expression
tags:
- AWS
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
title: ConditionExpression
---

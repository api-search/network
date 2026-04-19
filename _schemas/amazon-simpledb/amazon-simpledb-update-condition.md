---
description: Specifies the conditions under which data should be updated. If an update condition is specified for a request, the data will only be updated if the condition is satisfied. For example, if an attribute with a specific name and value exists, or if a specific attribute doesn't exist.
layout: schema
name: UpdateCondition
properties_list:
- description: ''
  name: Name
  type: object
- description: ''
  name: Value
  type: object
- description: ''
  name: Exists
  type: object
provider_name: Amazon SimpleDB
provider_slug: amazon-simpledb
schema_file: json-schema/amazon-simpledb-update-condition-schema.json
slug: amazon-simpledb-update-condition
tags:
- AWS
- Cloud Storage
- Data Storage
- Database
- NoSQL
title: UpdateCondition
---

---
description: <p>Provides information about the limitations of target Amazon Web Services engines.</p> <p>Your source database might include features that the target Amazon Web Services engine doesn't support. Fleet Advisor lists these features as limitations. You should consider these limitations during database migration. For each limitation, Fleet Advisor recommends an action that you can take to address or avoid this limitation.</p>
layout: schema
name: Limitation
properties_list:
- description: ''
  name: DatabaseId
  type: object
- description: ''
  name: EngineName
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: Description
  type: object
- description: ''
  name: Impact
  type: object
- description: ''
  name: Type
  type: object
provider_name: Amazon DMS
provider_slug: amazon-dms
schema_file: json-schema/amazon-dms-limitation-schema.json
slug: amazon-dms-limitation
tags:
- AWS
- Data Replication
- Database
- Database Migration
- Migration
title: Limitation
---

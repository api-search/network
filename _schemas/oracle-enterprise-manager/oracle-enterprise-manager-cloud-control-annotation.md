---
description: A comment or note attached to an incident, providing investigation details or remediation notes.
layout: schema
name: Annotation
properties_list:
- description: Unique identifier of the annotation.
  name: annotationId
  type: string
- description: Summary text of the annotation.
  name: summary
  type: string
- description: Detailed content of the annotation.
  name: details
  type: string
- description: Username of the annotation author.
  name: author
  type: string
- description: Timestamp when the annotation was created.
  name: timeCreated
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-annotation-schema.json
slug: oracle-enterprise-manager-cloud-control-annotation
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: Annotation
---

---
class_count: 9
classes:
- targetId
- targetName
- targetType
- hostName
- lifecycleStatus
- availabilityStatus
- severity
- priority
- status
context_file: json-ld/oracle-enterprise-manager-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/oracle-enterprise-manager/refs/heads/main/json-ld/oracle-enterprise-manager-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Oracle Enterprise Manager from Oracle Enterprise Manager.
layout: jsonld
name: Oracle Enterprise Manager Context
namespaces:
- prefix: oem
  uri: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/vocab#
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
properties:
- container: ''
  name: Target
  type: ''
- container: ''
  name: Incident
  type: ''
- container: ''
  name: Event
  type: ''
- container: ''
  name: Blackout
  type: ''
- container: ''
  name: BlackoutSchedule
  type: ''
- container: ''
  name: MetricGroup
  type: ''
- container: ''
  name: MetricColumn
  type: ''
- container: ''
  name: MetricDataPoint
  type: ''
- container: ''
  name: Annotation
  type: ''
- container: ''
  name: GlobalTargetProperty
  type: ''
- container: ''
  name: canonicalLink
  type: reference
- container: ''
  name: timeCreated
  type: dateTime
- container: ''
  name: timeUpdated
  type: dateTime
property_count: 13
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
slug: oracle-enterprise-manager-context
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
- JSON-LD
- Linked Data
- Semantic Web
---

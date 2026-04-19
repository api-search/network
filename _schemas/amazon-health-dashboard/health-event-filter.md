---
description: The values to use to filter results from the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html">DescribeEvents</a> and <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventAggregates.html">DescribeEventAggregates</a> operations.
layout: schema
name: EventFilter
properties_list:
- description: ''
  name: eventArns
  type: object
- description: ''
  name: eventTypeCodes
  type: object
- description: ''
  name: services
  type: object
- description: ''
  name: regions
  type: object
- description: ''
  name: availabilityZones
  type: object
- description: ''
  name: startTimes
  type: object
- description: ''
  name: endTimes
  type: object
- description: ''
  name: lastUpdatedTimes
  type: object
- description: ''
  name: entityArns
  type: object
- description: ''
  name: entityValues
  type: object
- description: ''
  name: eventTypeCategories
  type: object
- description: ''
  name: tags
  type: object
- description: ''
  name: eventStatusCodes
  type: object
provider_name: Amazon Health Dashboard
provider_slug: amazon-health-dashboard
schema_file: json-schema/health-event-filter-schema.json
slug: health-event-filter
tags:
- AWS
- Health Monitoring
- Notifications
- Operations
- Service Status
title: EventFilter
---

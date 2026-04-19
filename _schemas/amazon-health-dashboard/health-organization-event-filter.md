---
description: The values to filter results from the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html">DescribeEventsForOrganization</a> operation.
layout: schema
name: OrganizationEventFilter
properties_list:
- description: ''
  name: eventTypeCodes
  type: object
- description: ''
  name: awsAccountIds
  type: object
- description: ''
  name: services
  type: object
- description: ''
  name: regions
  type: object
- description: ''
  name: startTime
  type: object
- description: ''
  name: endTime
  type: object
- description: ''
  name: lastUpdatedTime
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
  name: eventStatusCodes
  type: object
provider_name: Amazon Health Dashboard
provider_slug: amazon-health-dashboard
schema_file: json-schema/health-organization-event-filter-schema.json
slug: health-organization-event-filter
tags:
- AWS
- Health Monitoring
- Notifications
- Operations
- Service Status
title: OrganizationEventFilter
---

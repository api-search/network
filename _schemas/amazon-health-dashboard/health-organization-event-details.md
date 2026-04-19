---
description: Detailed information about an event. A combination of an <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html">Event</a> object, an <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_EventDescription.html">EventDescription</a> object, and additional metadata about the event. Returned by the <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html">DescribeEventDetailsForOrganization</a> operation.
layout: schema
name: OrganizationEventDetails
properties_list:
- description: ''
  name: awsAccountId
  type: object
- description: ''
  name: event
  type: object
- description: ''
  name: eventDescription
  type: object
- description: ''
  name: eventMetadata
  type: object
provider_name: Amazon Health Dashboard
provider_slug: amazon-health-dashboard
schema_file: json-schema/health-organization-event-details-schema.json
slug: health-organization-event-details
tags:
- AWS
- Health Monitoring
- Notifications
- Operations
- Service Status
title: OrganizationEventDetails
---

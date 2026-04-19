---
description: <p>Summary information about an Health event.</p> <p>Health events can be public or account-specific:</p> <ul> <li> <p> <i>Public events</i> might be service events that are not specific to an Amazon Web Services account. For example, if there is an issue with an Amazon Web Services Region, Health provides information about the event, even if you don't use services or resources in that Region.</p> </li> <li> <p> <i>Account-specific</i> events are specific to either your Amazon Web Services account or an account in your organization. For example, if there's an issue with Amazon Elastic Compute Cloud in a Region that you use, Health provides information about the event and the affected resources in the account.</p> </li> </ul> <p>You can determine if an event is public or account-specific by using the <code>eventScopeCode</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html#AWSHealth-Type-Event-eventScopeCode">eventScopeCode</a>.</p>
layout: schema
name: Event
properties_list:
- description: ''
  name: arn
  type: object
- description: ''
  name: service
  type: object
- description: ''
  name: eventTypeCode
  type: object
- description: ''
  name: eventTypeCategory
  type: object
- description: ''
  name: region
  type: object
- description: ''
  name: availabilityZone
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
  name: statusCode
  type: object
- description: ''
  name: eventScopeCode
  type: object
provider_name: Amazon Health Dashboard
provider_slug: amazon-health-dashboard
schema_file: json-schema/health-event-schema.json
slug: health-event
tags:
- AWS
- Health Monitoring
- Notifications
- Operations
- Service Status
title: Event
---

---
description: ComplianceEvent from LinkedIn API
layout: schema
name: ComplianceEvent
properties_list:
- description: Unique identifier for the compliance event
  name: id
  type: string
- description: Timestamp when the event was captured
  name: capturedAt
  type: integer
- description: Timestamp when the event was processed
  name: processedAt
  type: integer
- description: Configuration version
  name: configVersion
  type: string
- description: ''
  name: owner
  type: object
- description: ''
  name: actor
  type: object
- description: Name of the resource
  name: resourceName
  type: string
- description: Identifier of the resource
  name: resourceId
  type: string
- description: URI of the resource
  name: resourceUri
  type: string
- description: Action method performed
  name: method
  type: string
- description: Activity details
  name: activity
  type: object
- description: Processed activity details
  name: processedActivity
  type: object
- description: Related sibling activities
  name: siblingActivities
  type: array
- description: Parent activity if applicable
  name: parentActivity
  type: object
- description: Parent sibling activities
  name: parentSiblingActivities
  type: array
provider_name: LinkedIn
provider_slug: linkedin
schema_file: json-schema/linkedin-compliance-events-compliance-event-schema.json
slug: linkedin-compliance-events-compliance-event
tags:
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
title: ComplianceEvent
---

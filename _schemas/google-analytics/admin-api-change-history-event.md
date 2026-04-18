---
description: A set of changes within a Google Analytics account or its child properties that resulted from the same cause. Common causes would be updates made in the Google Analytics UI, changes from customer support, or automatic Google Analytics system changes.
layout: schema
name: ChangeHistoryEvent
properties_list:
- description: The type of actor that made this change.
  name: actorType
  type: string
- description: Time when change was made.
  name: changeTime
  type: string
- description: A list of changes made in this change history event that fit the filters specified in SearchChangeHistoryEventsRequest.
  name: changes
  type: array
- description: If true, then the list of changes returned was filtered, and does not represent all changes that occurred in this event.
  name: changesFiltered
  type: boolean
- description: ID of this change history event. This ID is unique across Google Analytics.
  name: id
  type: string
- description: Email address of the Google account that made the change. This will be a valid email address if the actor field is set to USER, and empty otherwise. Google accounts that have been deleted will cause a
  name: userActorEmail
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-change-history-event-schema.json
slug: admin-api-change-history-event
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: ChangeHistoryEvent
---

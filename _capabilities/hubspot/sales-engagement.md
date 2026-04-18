---
consumed_apis:
- engagement-calls-api
- engagement-emails-api
- engagement-meetings-api
- engagement-tasks-api
- engagement-notes
description: Sales activity tracking workflow for calls, emails, meetings, tasks, and notes.
layout: capability
name: HubSpot Sales Engagement
operations: []
personas: []
provider_name: HubSpot
provider_slug: hubspot
search_terms:
- hubspot search tasks
- getemailengagement
- hubspot batch read email engagements
- getcallbyid
- batchupdateemailengagements
- createtask
- hubspot batch update email engagements
- customer service
- hubspot archive a batch of notes
- deletemeeting
- hubspot create a task association
- updatemeeting
- hubspot list meeting associations
- batcharchivenotes
- batchcreatemeetings
- hubspot search email engagements
- batchupdatemeetings
- hubspot create a meeting association
- hubspot update a meeting
- gdprdeletecall
- listtasks
- hubspot batch update tasks
- searchcalls
- searchmeetings
- listtaskassociations
- hubspot delete an email engagement association
- hubspot update an email engagement
- batchreadtasks
- deleteemailengagement
- hubspot update a batch of notes
- analytics
- hubspot create a task
- hubspot update a batch of calls
- hubspot search notes
- activities
- hubspot search calls
- searchnotes
- listcalls
- hubspot list email engagement associations
- marketing
- deletetask
- createmeeting
- listemailengagements
- hubspot update a task
- hubspot get a note by id
- batchupdatenotes
- content
- hubspot batch create email engagements
- deletetaskassociation
- hubspot batch read meetings
- hubspot create an email engagement
- hubspot update a note
- hubspot create a batch of notes
- batchcreatetasks
- listmeetings
- hubspot list email engagements
- createemailengagementassociation
- hubspot get a meeting
- batchreadnotes
- sales
- hubspot get a call by id
- hubspot read a batch of calls
- batchcreatecalls
- hubspot batch create meetings
- hubspot list meetings
- getnotebyid
- hubspot archive a batch of calls
- hubspot create a batch of calls
- createtaskassociation
- updatenote
- createemailengagement
- hubspot list tasks
- hubspot get an email engagement
- hubspot
- listnotes
- batcharchivecalls
- batchreadcalls
- crm
- listemailengagementassociations
- createnote
- hubspot batch update meetings
- hubspot archive a task
- batchcreatenotes
- gdprdeletenote
- batchupdatetasks
- marketing automation
- hubspot read a batch of notes
- hubspot archive a call
- gettask
- commerce
- hubspot create a note
- hubspot list all notes
- hubspot delete a task association
- hubspot batch read tasks
- hubspot permanently delete a call for gdpr compliance
- email marketing
- archivenote
- hubspot create a call
- createcall
- engagements
- hubspot get a task
- searchtasks
- hubspot update a call
- hubspot archive an email engagement
- hubspot batch create tasks
- batchreademailengagements
- updateemailengagement
- getmeeting
- archivecall
- batchreadmeetings
- updatecall
- batchcreateemailengagements
- deleteemailengagementassociation
- batchupdatecalls
- searchemailengagements
- hubspot create an email engagement association
- hubspot list task associations
- updatetask
- createmeetingassociation
- operations
- hubspot archive a note
- deletemeetingassociation
- hubspot search meetings
- hubspot list all calls
- listmeetingassociations
- hubspot archive a meeting
- hubspot delete a meeting association
- hubspot create a meeting
- hubspot permanently delete a note for gdpr compliance
slug: sales-engagement
tags:
- HubSpot
- Sales
- Engagements
- Activities
tools:
- description: HubSpot List All Calls
  hints:
    readOnly: true
  name: listcalls
- description: HubSpot Create a Call
  hints:
    readOnly: false
  name: createcall
- description: HubSpot Get a Call by ID
  hints:
    readOnly: true
  name: getcallbyid
- description: HubSpot Update a Call
  hints:
    readOnly: false
  name: updatecall
- description: HubSpot Archive a Call
  hints:
    destructive: true
  name: archivecall
- description: HubSpot Create a Batch of Calls
  hints:
    readOnly: false
  name: batchcreatecalls
- description: HubSpot Read a Batch of Calls
  hints:
    readOnly: false
  name: batchreadcalls
- description: HubSpot Update a Batch of Calls
  hints:
    readOnly: false
  name: batchupdatecalls
- description: HubSpot Archive a Batch of Calls
  hints:
    readOnly: false
  name: batcharchivecalls
- description: HubSpot Search Calls
  hints:
    readOnly: false
  name: searchcalls
- description: HubSpot Permanently Delete a Call for GDPR Compliance
  hints:
    readOnly: false
  name: gdprdeletecall
- description: HubSpot List Email Engagements
  hints:
    readOnly: true
  name: listemailengagements
- description: HubSpot Create an Email Engagement
  hints:
    readOnly: false
  name: createemailengagement
- description: HubSpot Get an Email Engagement
  hints:
    readOnly: true
  name: getemailengagement
- description: HubSpot Update an Email Engagement
  hints:
    readOnly: false
  name: updateemailengagement
- description: HubSpot Archive an Email Engagement
  hints:
    destructive: true
  name: deleteemailengagement
- description: HubSpot Batch Read Email Engagements
  hints:
    readOnly: false
  name: batchreademailengagements
- description: HubSpot Batch Create Email Engagements
  hints:
    readOnly: false
  name: batchcreateemailengagements
- description: HubSpot Batch Update Email Engagements
  hints:
    readOnly: false
  name: batchupdateemailengagements
- description: HubSpot Search Email Engagements
  hints:
    readOnly: false
  name: searchemailengagements
- description: HubSpot List Email Engagement Associations
  hints:
    readOnly: true
  name: listemailengagementassociations
- description: HubSpot Create an Email Engagement Association
  hints:
    readOnly: false
  name: createemailengagementassociation
- description: HubSpot Delete an Email Engagement Association
  hints:
    destructive: true
  name: deleteemailengagementassociation
- description: HubSpot List Meetings
  hints:
    readOnly: true
  name: listmeetings
- description: HubSpot Create a Meeting
  hints:
    readOnly: false
  name: createmeeting
- description: HubSpot Get a Meeting
  hints:
    readOnly: true
  name: getmeeting
- description: HubSpot Update a Meeting
  hints:
    readOnly: false
  name: updatemeeting
- description: HubSpot Archive a Meeting
  hints:
    destructive: true
  name: deletemeeting
- description: HubSpot Batch Read Meetings
  hints:
    readOnly: false
  name: batchreadmeetings
- description: HubSpot Batch Create Meetings
  hints:
    readOnly: false
  name: batchcreatemeetings
- description: HubSpot Batch Update Meetings
  hints:
    readOnly: false
  name: batchupdatemeetings
- description: HubSpot Search Meetings
  hints:
    readOnly: false
  name: searchmeetings
- description: HubSpot List Meeting Associations
  hints:
    readOnly: true
  name: listmeetingassociations
- description: HubSpot Create a Meeting Association
  hints:
    readOnly: false
  name: createmeetingassociation
- description: HubSpot Delete a Meeting Association
  hints:
    destructive: true
  name: deletemeetingassociation
- description: HubSpot List Tasks
  hints:
    readOnly: true
  name: listtasks
- description: HubSpot Create a Task
  hints:
    readOnly: false
  name: createtask
- description: HubSpot Get a Task
  hints:
    readOnly: true
  name: gettask
- description: HubSpot Update a Task
  hints:
    readOnly: false
  name: updatetask
- description: HubSpot Archive a Task
  hints:
    destructive: true
  name: deletetask
- description: HubSpot Batch Read Tasks
  hints:
    readOnly: false
  name: batchreadtasks
- description: HubSpot Batch Create Tasks
  hints:
    readOnly: false
  name: batchcreatetasks
- description: HubSpot Batch Update Tasks
  hints:
    readOnly: false
  name: batchupdatetasks
- description: HubSpot Search Tasks
  hints:
    readOnly: false
  name: searchtasks
- description: HubSpot List Task Associations
  hints:
    readOnly: true
  name: listtaskassociations
- description: HubSpot Create a Task Association
  hints:
    readOnly: false
  name: createtaskassociation
- description: HubSpot Delete a Task Association
  hints:
    destructive: true
  name: deletetaskassociation
- description: HubSpot List All Notes
  hints:
    readOnly: true
  name: listnotes
- description: HubSpot Create a Note
  hints:
    readOnly: false
  name: createnote
- description: HubSpot Get a Note by ID
  hints:
    readOnly: true
  name: getnotebyid
- description: HubSpot Update a Note
  hints:
    readOnly: false
  name: updatenote
- description: HubSpot Archive a Note
  hints:
    destructive: true
  name: archivenote
- description: HubSpot Create a Batch of Notes
  hints:
    readOnly: false
  name: batchcreatenotes
- description: HubSpot Read a Batch of Notes
  hints:
    readOnly: false
  name: batchreadnotes
- description: HubSpot Update a Batch of Notes
  hints:
    readOnly: false
  name: batchupdatenotes
- description: HubSpot Archive a Batch of Notes
  hints:
    readOnly: false
  name: batcharchivenotes
- description: HubSpot Search Notes
  hints:
    readOnly: false
  name: searchnotes
- description: HubSpot Permanently Delete a Note for GDPR Compliance
  hints:
    readOnly: false
  name: gdprdeletenote
---

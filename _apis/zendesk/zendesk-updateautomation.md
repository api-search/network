---
aid: zendesk:zendesk-updateautomation
name: Zendesk Put  Api V2 Automations Automation_id
tags:
- Automations
humanURL: 
properties: []
description: >-
  Updates an automation.  Updated automations must be unique and have at least one condition that is true only once or an action that nullifies at least one of the conditions. Active automations can have overlapping conditions but can't be identical.  The request must include the following conditions in the `all` array: - At least one time-based condition - At least one condition that checks one of the following fields: 'status', 'type', 'group_id', 'assignee_id', or 'requester_id'  **Note**: U...

---

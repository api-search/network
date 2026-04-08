---
aid: zendesk:zendesk-customobjectrecordbulkjobs
name: Zendesk Post  Api V2 Custom_objects Custom_object_key Jobs
tags:
- Custom Object Records
humanURL: 
properties: []
description: >-
  Queues a background job to perform bulk actions on up to 100 custom object records per single request. Takes a `job` object with two nested fields: * `action`, one of:     * `"create"`     * `"delete"`     * `"delete_by_external_id"`     * `"create_or_update_by_external_id"`     * `"create_or_update_by_name"`     * `"update"` * `items`     * For a `"create"` action, an array of JSON objects representing the custom object records being created     * For a `"delete"` action, an array of strings...

---

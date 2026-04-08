---
aid: sendgrid:sendgrid-getimportcontact
name: Import Contacts Status
tags:
- Contacts
humanURL: 
properties: []
description: >-
  **This endpoint can be used to check the status of a contact import job**.   Use the `job_id` from the "Import Contacts," "Add or Update a Contact," or "Delete Contacts" endpoints as the `id` in the path parameter.  If there is an error with your `PUT` request, download the `errors_url` file and open it to view more details.  The job `status` field indicates whether the job is `pending`, `completed`, `errored`, or `failed`.   Pending means not started. Completed means finished without any err...

---

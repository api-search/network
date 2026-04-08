---
aid: sendgrid:sendgrid-duplicatesinglesend
name: Duplicate Single Send
tags:
- Single Sends
humanURL: 
properties: []
description: >-
  **This endpoint allows you to duplicate an existing Single Send using its Single Send ID.**  Duplicating a Single Send is useful when you want to create a Single Send but don't want to start from scratch. Once duplicated, you can update or edit the Single Send by making a PATCH request to the `/marketing/singlesends/{id}` endpoint.   If you leave the `name` field blank, your duplicate will be assigned the name of the Single Send it was copied from with the text “Copy of ” prepended to it. The...

---

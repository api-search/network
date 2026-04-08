---
aid: zendesk:zendesk-updatemanyviews
name: Zendesk Put  Api V2 Views Update_many
tags:
- Views
humanURL: 
properties: []
description: >-
  #### Allowed For  * Agents  #### Request Parameters  The PUT request expects a `views` object that lists the views to update.  Each view may have the following properties:  | Name     | Mandatory | Description | -------- | --------- | ----------- | id       | yes       | The ID of the view to update | position | no        | The new position of the view | active   | no        | The active status of the view (true or false)  #### Example Request Body  ```js {   "views": [     {"id": 25, "positi...

---

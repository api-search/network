---
aid: sendgrid:sendgrid-createmailbatch
name: Create a batch ID.
tags:
- Mail Batch
humanURL: 
properties: []
description: >-
  **This operation allows you to generate a new mail batch ID.**   Once a batch ID is created, you can associate it with a mail send by passing it in the request body of the [Mail Send operation](https://docs.sendgrid.com/api-reference/mail-send/mail-send). This makes it possible to group multiple requests to the Mail Send operation by assigning them the same batch ID.   A batch ID that's associated with a mail send can be used to access and modify the associated send. For example, you can paus...

---

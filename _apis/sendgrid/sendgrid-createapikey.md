---
aid: sendgrid:sendgrid-createapikey
name: Create API keys
tags:
- API Keys
humanURL: 
properties: []
description: >-
  **This endpoint allows you to create a new API Key for the user.**  To create your initial SendGrid API Key, you should [use the SendGrid App](https://app.sendgrid.com/settings/api_keys). Once you have created a first key with scopes to manage additional API keys, you can use this API for all other key management. A JSON request body containing a `name` property is required when making requests to this endpoint. If the number of maximum keys, 100, is reached, a `403` status will be returned. ...

---

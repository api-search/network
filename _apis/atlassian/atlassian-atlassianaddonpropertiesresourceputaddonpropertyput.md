---
aid: atlassian:atlassian-atlassianaddonpropertiesresourceputaddonpropertyput
name: Set App Property
tags:
- App properties
humanURL: 
properties: []
description: >-
  Sets the value of an app's property. Use this resource to store custom data for your app.<br><br>The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.<br><br>**[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request.<br>Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).

---

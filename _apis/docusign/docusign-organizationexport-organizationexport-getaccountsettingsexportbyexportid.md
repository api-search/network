---
aid: docusign:docusign-organizationexport-organizationexport-getaccountsettingsexportbyexportid
name: Returns the results for a single account settings export request.
tags:
- AccountSettingsExport
humanURL: 
properties: []
description: >-
  Returns the results for a single account settings export request.  - Required scopes: `account_read`  Given an export id, this method returns the results of an account settings export request. To get a list of all the export requests, use `getAccountSettingsExports`.  You can find the actual list of settings at  `results[n].url` in the response. The settings export is formatted like this:  ``` json {   "accounts": [     {       "account_id": "9ca037f4-xxxx-xxxx-xxxx-212e57d4f22e",       "name...

---

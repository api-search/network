---
aid: atlassian:atlassian-atlassiancreateorupdatereport
name: Create Or Update A Report
tags:
- Reports - Commits
humanURL: 
properties: []
description: >-
  Creates or updates a report for the specified commit.<br>To upload a report, make sure to generate an ID that is unique across all reports for that commit. If you want to use an existing id from your own system, we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-001.<br><br>### Sample cURL request:<br>```<br>curl --request PUT 'https://api.bitbucket.org/2.0/repositories///commit//reports/mysystem-001' \<br>--header 'Content-Type: application/json' \<b...

---

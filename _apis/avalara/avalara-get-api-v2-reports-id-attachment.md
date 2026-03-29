---
aid: avalara:avalara-get-api-v2-reports-id-attachment
name: DownloadReport
tags:
- Reports
humanURL: 
properties: []
description: >-
  This API downloads the file associated with a report.              If the report is not yet complete, you will receive a `ReportNotFinished` error.  To check if a report is complete, use the `GetReport` API.              Reports are run as asynchronous report tasks on the server.  When complete, the report file will be available for download for up to 30 days after completion.  To run an asynchronous report, you should follow these steps:              * Begin a report by calling the r...

---

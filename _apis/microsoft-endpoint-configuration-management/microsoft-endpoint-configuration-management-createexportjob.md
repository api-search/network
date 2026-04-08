---
aid: microsoft-endpoint-configuration-management:microsoft-endpoint-configuration-management-createexportjob
name: Microsoft Endpoint Configuration Management Create export job
tags:
- Export Jobs
humanURL: 
properties: []
description: >-
  Create a new deviceManagementExportJob object to initiate an asynchronous report export. The reportName parameter is required in the request body and identifies which report to export. After creation, poll the export job by ID until the status changes to completed, then download the report from the url property.

---

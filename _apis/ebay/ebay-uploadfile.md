---
aid: ebay:ebay-uploadfile
name: Upload File
tags:
- task
humanURL: 
properties: []
description: >-
  This method associates the specified file with the specified task ID and uploads the input file. After the file has been uploaded, the processing of the file begins. <br><br>Reports often take time to generate and it's common for this method to return an HTTP status of 202, which indicates the report is being generated. Use the <b> getTask</b> with the task ID or <b> getTasks</b> to determine the status of a report. <br><br>The status flow is <code>QUEUED</code> &gt; <code>IN_PROCESS</code> &...

---

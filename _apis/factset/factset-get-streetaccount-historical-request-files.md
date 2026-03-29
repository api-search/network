---
aid: factset:factset-get-streetaccount-historical-request-files
name: Returns the jobID
tags:
- - - - StreetAccount Historical Stories
humanURL: 
properties: []
description: >-
  Give the startDate and endDate parameters as request parameters in the /request-files endpoint, it returns the jobID. startDate and endDate should be in YYYY-MM-DDTHH:MM:SSZ format. This API only supports adhoc requests to retrieve historical files and does not support real-time files and if you interested in require real-time push should consider the other three methods (pushed via SFTP, to QNT account, or your Azure Storage). Per API request able to query till 2 years of data

---

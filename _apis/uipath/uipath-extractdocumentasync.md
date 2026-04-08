---
aid: uipath:uipath-extractdocumentasync
name: Start asynchronous document extraction
tags:
- Extraction
humanURL: 
properties: []
description: >-
  Submits a previously digitized document for asynchronous data extraction. The extractors to apply and the document type must be specified in the request body. Returns a requestId to poll for results. Results are retained for 24 hours. Use GET /extraction/{requestId}/result to retrieve extracted field values once processing completes.

---

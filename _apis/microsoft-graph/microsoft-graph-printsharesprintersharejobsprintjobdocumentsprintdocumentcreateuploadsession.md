---
aid: microsoft-graph:microsoft-graph-printsharesprintersharejobsprintjobdocumentsprintdocumentcreateuploadsession
name: Microsoft Graph Invoke action createUploadSession
tags:
- print.printerShare
humanURL: 
properties: []
description: >-
  Create an upload session that allows an app to iteratively upload ranges of a binary file linked to the print document. As part of the response, this action returns an upload URL that can be used in subsequent sequential PUT queries. Request headers for each PUT operation can be used to specify the exact range of bytes to be uploaded. This allows transfer to be resumed, in case the network connection is dropped during upload.

---

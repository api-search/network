---
aid: amazon-web-services:amazon-web-services-amazonwebserviceslistfragments
name: Listfragments
tags:
- API
humanURL: 
properties: []
description: >-
  Returns a list of Fragment objects from the specified stream and timestamp range within the archived data. Listing fragments is eventually consistent. This means that even if the producer receives an acknowledgment that a fragment is persisted, the result might not be returned immediately from a request to ListFragments. However, results are typically available in less than one second.  You must first call the GetDataEndpoint API to get an endpoint. Then send the ListFragments requests to thi...

---

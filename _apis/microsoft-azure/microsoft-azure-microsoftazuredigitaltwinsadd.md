---
aid: microsoft-azure:microsoft-azure-microsoftazuredigitaltwinsadd
name: Microsoft Azure Put Digitaltwins Id
tags:
- Twins
humanURL: 
properties: []
description: >-
  Adds or replaces a digital twin.<br>Status codes:<br>* 200 OK<br>* 400 Bad Request<br>  * InvalidArgument - The digital twin id or payload is invalid.<br>  * ModelDecommissioned - The model for the digital twin is decommissioned.<br>  * TwinLimitReached - The maximum number of digital twins allowed has been reached.<br>  * ValidationFailed - The digital twin payload is not valid.<br>* 412 Precondition Failed<br>  * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

---

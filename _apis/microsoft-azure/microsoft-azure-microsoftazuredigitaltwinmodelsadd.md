---
aid: microsoft-azure:microsoft-azure-microsoftazuredigitaltwinmodelsadd
name: Microsoft Azure Post Models
tags:
- Models
humanURL: 
properties: []
description: >-
  Uploads one or more models. When any error occurs, no models are uploaded.<br>Status codes:<br>* 201 Created<br>* 400 Bad Request<br>  * DTDLParserError - The models provided are not valid DTDL.<br>  * InvalidArgument - The model id is invalid.<br>  * LimitExceeded - The maximum number of model ids allowed in 'dependenciesFor' has been reached.<br>  * ModelVersionNotSupported - The version of DTDL used is not supported.<br>* 409 Conflict<br>  * ModelAlreadyExists - The model provided already ...

---

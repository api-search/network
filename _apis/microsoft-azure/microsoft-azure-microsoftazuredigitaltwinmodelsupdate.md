---
aid: microsoft-azure:microsoft-azure-microsoftazuredigitaltwinmodelsupdate
name: Microsoft Azure Patch Models Id
tags:
- Models
humanURL: 
properties: []
description: >-
  Updates the metadata for a model.<br>Status codes:<br>* 204 No Content<br>* 400 Bad Request<br>  * InvalidArgument - The model id is invalid.<br>  * JsonPatchInvalid - The JSON Patch provided is invalid.<br>  * MissingArgument - The model id was not provided.<br>* 404 Not Found<br>  * ModelNotFound - The model was not found.<br>* 409 Conflict<br>  * ModelReferencesNotDecommissioned - The model refers to models that are not decommissioned.

---

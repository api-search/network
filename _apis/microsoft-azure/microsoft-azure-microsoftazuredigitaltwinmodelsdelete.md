---
aid: microsoft-azure:microsoft-azure-microsoftazuredigitaltwinmodelsdelete
name: Microsoft Azure Delete Models Id
tags:
- Models
humanURL: 
properties: []
description: >-
  Deletes a model. A model can only be deleted if no other models reference it.<br>Status codes:<br>* 204 No Content<br>* 400 Bad Request<br>  * InvalidArgument - The model id is invalid.<br>  * MissingArgument - The model id was not provided.<br>* 404 Not Found<br>  * ModelNotFound - The model was not found.<br>* 409 Conflict<br>  * ModelReferencesNotDeleted - The model refers to models that are not deleted.

---

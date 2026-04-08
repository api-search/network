---
aid: replicate:replicate-modelsdelete
name: Replicate Delete a model
tags:
- Model
- Name
- Owner
humanURL: 
properties: []
description: >-
  Delete a model  Model deletion has some restrictions:  - You can only delete models you own. - You can only delete private models. - You can only delete models that have no versions associated with them. Currently you'll need to [delete the model's versions](#models.versions.delete) before you can delete the model itself.  Example cURL request:  ```command curl -s -X DELETE \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/models/replicate/hello-world ```  T...

---

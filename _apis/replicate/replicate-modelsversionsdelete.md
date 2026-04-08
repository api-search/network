---
aid: replicate:replicate-modelsversionsdelete
name: Replicate Delete a model version
tags:
- Model
- Name
- Owner
- Version
humanURL: 
properties: []
description: >-
  Delete a model version and all associated predictions, including all output files.  Model version deletion has some restrictions:  - You can only delete versions from models you own. - You can only delete versions from private models. - You cannot delete a version if someone other than you has run predictions with it. - You cannot delete a version if it is being used as the base model for a fine tune/training. - You cannot delete a version if it has an associated deployment. - You cannot dele...

---

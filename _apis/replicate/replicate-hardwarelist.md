---
aid: replicate:replicate-hardwarelist
name: Replicate List available hardware for models
tags:
- Hardware
humanURL: 
properties: []
description: >-
  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/hardware ```  The response will be a JSON array of hardware objects:  ```json [     {"name": "CPU", "sku": "cpu"},     {"name": "Nvidia T4 GPU", "sku": "gpu-t4"},     {"name": "Nvidia A40 GPU", "sku": "gpu-a40-small"},     {"name": "Nvidia A40 (Large) GPU", "sku": "gpu-a40-large"}, ] ```

---

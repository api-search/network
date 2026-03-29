---
aid: amazon-web-services:amazon-web-services-amazonwebservicesuploadlayerpart
name: Uploadlayerpart
tags:
- API
humanURL: 
properties: []
description: >-
  Uploads an image layer part to Amazon ECR. When an image is pushed, each new image layer is uploaded in parts. The maximum size of each image layer part can be 20971520 bytes (about 20MB). The UploadLayerPart API is called once for each new image layer part.  This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

---

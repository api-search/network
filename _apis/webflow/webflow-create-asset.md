---
aid: webflow:webflow-create-asset
name: Webflow Upload Asset
tags:
- Assets
humanURL: 
properties: []
description: >-
  The first step in uploading an asset to a site.   This endpoint generates a response with the following information: `uploadUrl` and `uploadDetails`.   Use these properties in the header of a [POST request to Amazson s3](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPOST.html) to complete the upload.   To learn more about how to upload assets to Webflow, see our [assets guide](/data/docs/working-with-assets).   Required scope | `assets:write`

---

---
aid: amazon-web-services:amazon-web-services-amazonwebservicesdeletechannel
name: Deletechannel
tags:
- API
humanURL: 
properties: []
description: >-
  Deletes the specified channel and its associated stream keys. If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call StopStream, wait for the Amazon EventBridge "Stream End" event (to verify that the stream's state is no longer Live), then call DeleteChannel. (See  Using EventBridge with Amazon IVS.)

---

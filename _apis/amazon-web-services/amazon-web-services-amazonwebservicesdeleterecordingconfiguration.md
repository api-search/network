---
aid: amazon-web-services:amazon-web-services-amazonwebservicesdeleterecordingconfiguration
name: Deleterecordingconfiguration
tags:
- API
humanURL: 
properties: []
description: >-
  Deletes the recording configuration for the specified ARN. If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use UpdateChannel to set the recordingConfigurationArn field to an empty string, then use DeleteRecordingConfiguration.

---

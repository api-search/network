---
aid: amazon-web-services:amazon-web-services-amazonwebservicescreateparticipantconnection
name: Createparticipantconnection
tags:
- API
humanURL: 
properties: []
description: >-
  Creates the participant's connection.    ParticipantToken is used for invoking this API instead of ConnectionToken.  The participant token is valid for the lifetime of the participant – until they are part of a contact. The response URL for WEBSOCKET Type has a connect expiry timeout of 100s. Clients must manually connect to the returned websocket URL and subscribe to the desired topic.  For chat, you need to publish the following on the established websocket connection:  {"topic":"aws/subscr...

---

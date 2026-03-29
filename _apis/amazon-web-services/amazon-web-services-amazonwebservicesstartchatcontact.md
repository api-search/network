---
aid: amazon-web-services:amazon-web-services-amazonwebservicesstartchatcontact
name: Startchatcontact
tags:
- API
humanURL: 
properties: []
description: >-
  Initiates a flow to start a new chat for the customer. Response of this API provides a token required to obtain credentials from the CreateParticipantConnection API in the Amazon Connect Participant Service. When a new chat contact is successfully created, clients must subscribe to the participant’s connection for the created chat within 5 minutes. This is achieved by invoking CreateParticipantConnection with WEBSOCKET and CONNECTION_CREDENTIALS.  A 429 error occurs in the following situation...

---

---
aid: microsoft-azure:microsoft-azure-microsoftazurewebhookstest
name: Microsoft Azure Sends A Request For Each Registered Event Type To The Registered Url
tags:
- 'Custom Speech Web Hooks:'
humanURL: 
properties: []
description: >-
  The payload will be generated from the last entity that would have invoked the web hook. If no entity is present for none of the registered event types,<br>the POST will respond with 204. If a test request can be made, it will respond with 200.<br>The request will contain a X-MicrosoftSpeechServices-Event header with the respective registered event type.<br>If the web hook was registered with a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payl...

---

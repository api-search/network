---
aid: microsoft-azure:microsoft-azure-microsoftazurepinghook
name: Microsoft Azure Sends A Ping Event To The Registered Url
tags:
- 'Custom Speech Web Hooks:'
humanURL: 
properties: []
description: >-
  The request body of the POST request sent to the registered web hook URL is of the same shape as in the GET request for a specific hook.<br>The Swagger Schema ID of the model is WebHookV3.<br>            <br>The request will contain a X-MicrosoftSpeechServices-Event header with the value ping. If the web hook was registered with<br>a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payload with<br>the secret as HMAC key. The hash is base64 encoded.

---

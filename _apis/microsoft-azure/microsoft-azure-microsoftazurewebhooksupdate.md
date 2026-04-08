---
aid: microsoft-azure:microsoft-azure-microsoftazurewebhooksupdate
name: Microsoft Azure Updates The Web Hook Identified By The Given Id
tags:
- 'Custom Speech Web Hooks:'
humanURL: 
properties: []
description: >-
  If the property secret in the configuration is omitted or contains an empty string, future callbacks won't contain X-MicrosoftSpeechServices-Signature<br>headers. If the property contains a non-empty string, it will be used to create a SHA256 hash of the payload with the secret as HMAC key. This hash<br>will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.<br>            <br>If the URL changes,  the web hook will stop receiving events until a<br>...

---

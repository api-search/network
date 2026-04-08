---
aid: microsoft-azure:microsoft-azure-microsoftazurecreatehook
name: Microsoft Azure Creates A New Web Hook
tags:
- 'Custom Speech Web Hooks:'
humanURL: 
properties: []
description: >-
  If the property secret in the configuration is present and contains a non-empty string, it will be used to create a SHA256 hash of the payload with<br>the secret as HMAC key. This hash will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.<br>            <br>When calling back into the registered URL, the request will contain a X-MicrosoftSpeechServices-Event header containing one of the registered event<br>types. There will be one request per regi...

---

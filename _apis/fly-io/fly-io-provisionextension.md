---
aid: fly-io:fly-io-provisionextension
name: Provision an extension resource
tags:
- Extensions
humanURL: 
properties: []
description: >-
  Called by Fly.io when a user provisions an extension via the flyctl CLI. The provider must create the requested resource and respond with its unique ID and a config object containing the environment variables to inject into the user's Fly App. Provisioning must complete within 5 seconds; if the resource takes longer to create, the provider should respond immediately and use the webhook endpoint to notify Fly.io when the resource becomes available.

---

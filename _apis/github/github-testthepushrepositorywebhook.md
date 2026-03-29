---
aid: github:github-testthepushrepositorywebhook
name: Test The Push Repository Webhook
tags:
- Tests
- Push
- Repositories
- Webhooks
humanURL: 
properties: []
description: >-
  This will trigger the hook with the latest push to the current repository if the hook is subscribed to `push` events. If the hook is not subscribed to `push` events, the server will respond with 204 but no test POST will be generated.  **Note**: Previously `/repos/:owner/:repo/hooks/:hook_id/test`

---

---
aid: github:github-rerequestchecksuite
name: Rerequest Check Suite
tags:
- Check Suites
humanURL: 
properties: []
description: >-
  Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger the [`check_suite` webhook](https://docs.github.com/enterprise-server@3.9/webhooks/event-payloads/#check_suite) event with the action `rerequested`. When a check suite is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.  OAuth apps and personal access tokens (classic) cannot use this endpoint.

---

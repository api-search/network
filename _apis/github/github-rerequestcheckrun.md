---
aid: github:github-rerequestcheckrun
name: Rerequest Check Run
tags:
- Check Runs
humanURL: 
properties: []
description: >-
  Triggers GitHub to rerequest an existing check run, without pushing new code to a repository. This endpoint will trigger the [`check_run` webhook](https://docs.github.com/enterprise-server@3.9/webhooks/event-payloads/#check_run) event with the action `rerequested`. When a check run is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.  For more information about how to re-run GitHub Actions jobs, see "[Re-run a job from a workflow run](https://docs.github.com/en...

---

---
aid: openai:openai-submittoolouputstorun
name: OpenAI When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.
tags:
- Threads
humanURL: 
properties: []
description: >-
  POST /threads/{thread_id}/runs/{run_id}/submit_tool_outputs for OpenAI threads.

---

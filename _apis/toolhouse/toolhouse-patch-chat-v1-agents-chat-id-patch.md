---
aid: toolhouse:toolhouse-patch-chat-v1-agents-chat-id-patch
name: Toolhouse Patch Chat
tags:
- SDK API
humanURL: 
properties: []
description: >-
  Patches a chat.  This endpoint allows users to update specific fields of a chat identified by its `chat_id`.  - **chat_id**: The unique identifier of the chat to be patched. This field cannot be updated. - **request**: A ChatModel object containing the fields to be updated. Only fields that are provided   will be updated. The ID of the user who owns the chat and the chat's ID cannot be updated.  **Responses:** - 200: Returns the updated ChatModel. - 404: If the chat is not found. - 500: If th...

---

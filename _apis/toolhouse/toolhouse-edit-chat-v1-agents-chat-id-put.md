---
aid: toolhouse:toolhouse-edit-chat-v1-agents-chat-id-put
name: Toolhouse Edit Chat
tags:
- SDK API
humanURL: 
properties: []
description: >-
  Updates a chat  This endpoint allows users to update Chats fields of a chat identified by its `chat_id`.  - **chat_id**: The unique identifier of the chat to be patched. This field cannot be updated. - **request**: A ChatRequest object containing the fields to be updated. All fields will be updated, if a field is not provided default values will be used. The ID of the user who owns the chat and the chat's ID cannot be updated.  **Responses:** - 200: Returns the updated ChatModel. - 404: If th...

---

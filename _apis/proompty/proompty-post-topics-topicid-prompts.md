---
aid: proompty:proompty-post-topics-topicid-prompts
name: Create a new prompts within a specified topic. Users can send a POST request to this endpoint, including the topicId parameter in the URL path and a JSON payload containing the details of the prompt to be created. This payload typically includes the prompt content, along with any relevant metadata. Upon successful execution, the API responds with the newly created prompt object in JSON format, confirming its addition to the specified topic. If there are any issues with the request, such as invalid input data or the specified topic not being found, the endpoint returns an appropriate error response (400 for bad request, 404 for topic not found), ensuring users receive accurate feedback regarding the status of their request. This endpoint offers users a straightforward method for adding prompts to topics, facilitating the efficient management and organization of content within the Proompty platform.
tags:
- Prompts
- Topic
- Topics
humanURL: 
properties: []
description: >-
  Create a prompt for a topic

---

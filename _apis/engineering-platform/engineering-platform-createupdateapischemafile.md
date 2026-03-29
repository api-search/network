---
aid: engineering-platform:engineering-platform-createupdateapischemafile
name: Create or update a schema file
tags:
- API
- Schema
humanURL: 
properties: []
description: >-
  Creates or updates an API schema file.  **Note:**  - If the provided file path exists, the file is updated with the new contents. - If the provided file path does not exist, then a new schema file is created. - If the file path contains a `/` (forward slash) character, then a folder is created. For example, if the file path is the `dir/schema.json` value, then a `dir` folder is created with the `schema.json` file inside. - You can only update the `root` tag for protobuf specifications.

---

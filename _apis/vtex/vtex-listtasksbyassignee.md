---
aid: vtex:vtex-listtasksbyassignee
name: VTex List tasks
tags:
- Task
humanURL: 
properties: []
description: >-
  This endpoint allows you to filter tasks. You can choose between the following filtering options:   - **Assignees:** using `assignee.email` and `status`. Example: `https://{{accountName}}.{{environment}}.com.br/api/do/tasks?assignee.email={{person@email.com}}&status={{open}}`.   - **Targets:** using `targetId` and `status`. Example: `https://{{accountName}}.{{environment}}.com.br/api/do/tasks?target.id={{name}}&status={{open}}`.   - **Paged tasks:** using `page`, `perPage` and `status`....

---

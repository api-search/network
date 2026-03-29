---
aid: atlassian:atlassian-atlassiandeleteprojectasynchronously
name: Delete Project Asynchronously
tags:
- Projects
humanURL: 
properties: []
description: >-
  Deletes a project asynchronously.<br><br>This operation is:<br><br> *  transactional, that is, if part of the delete fails the project is not deleted.<br> *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.<br><br>**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

---

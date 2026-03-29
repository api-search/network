---
aid: fargate:fargate-stoptask
name: Stop a running task
tags:
- Tasks
humanURL: 
properties: []
description: >-
  Stops a running task. When you call StopTask on a Fargate task, the equivalent of docker stop is issued to the containers running in the task. This results in a SIGTERM value and a default 30-second timeout, after which the SIGKILL value is sent and the containers are forcibly stopped. The task transitions through STOPPING to STOPPED.

---

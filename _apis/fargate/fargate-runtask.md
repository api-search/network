---
aid: fargate:fargate-runtask
name: Run a Fargate task
tags:
- Tasks
humanURL: 
properties: []
description: >-
  Starts a new task using the specified task definition. When using the Fargate launch type, tasks run on AWS Fargate serverless infrastructure without the need to manage servers. The networkConfiguration parameter with awsvpcConfiguration is required for Fargate tasks. You can optionally specify a platformVersion, which defaults to LATEST. Each RunTask call can launch up to 10 tasks.

---

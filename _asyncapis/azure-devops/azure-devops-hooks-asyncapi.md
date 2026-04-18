---
channels:
- description: Published when a work item is created in Azure Boards.
  name: workitem.created
  operation: subscribe
  operation_id: onWorkItemCreated
  summary: Work item created
- description: Published when a work item is updated in Azure Boards.
  name: workitem.updated
  operation: subscribe
  operation_id: onWorkItemUpdated
  summary: Work item updated
- description: Published when a build pipeline run completes.
  name: build.complete
  operation: subscribe
  operation_id: onBuildComplete
  summary: Build completed
- description: Published when code is pushed to a repository.
  name: git.push
  operation: subscribe
  operation_id: onGitPush
  summary: Code pushed to repository
- description: Published when a pull request is created.
  name: git.pullrequest.created
  operation: subscribe
  operation_id: onPullRequestCreated
  summary: Pull request created
- description: Published when a pull request is merged.
  name: git.pullrequest.merged
  operation: subscribe
  operation_id: onPullRequestMerged
  summary: Pull request merged
- description: Published when a release deployment completes.
  name: release.deployment.completed
  operation: subscribe
  operation_id: onReleaseDeploymentCompleted
  summary: Release deployment completed
description: Azure DevOps Service Hooks deliver event notifications for work item changes, build completions, pull request events, code pushes, and release deployments. Service hooks are configured in Azure DevOps settings and delivered via HTTPS POST to registered consumer endpoints.
layout: asyncapi
messages:
- description: ''
  name: WorkItemCreatedEvent
  summary: ''
  title: Work Item Created
- description: ''
  name: WorkItemUpdatedEvent
  summary: ''
  title: Work Item Updated
- description: ''
  name: BuildCompleteEvent
  summary: ''
  title: Build Complete
- description: ''
  name: GitPushEvent
  summary: ''
  title: Git Push
- description: ''
  name: PullRequestEvent
  summary: ''
  title: Pull Request Event
- description: ''
  name: ReleaseDeploymentEvent
  summary: ''
  title: Release Deployment Completed
name: Azure DevOps Service Hooks (Webhooks)
provider_name: Azure DevOps
provider_slug: azure-devops
servers:
- description: Your registered HTTPS consumer endpoint for Azure DevOps service hooks
  name: consumer
  protocol: https
  url: https://your-consumer.example.com/hooks/azure-devops
slug: azure-devops-hooks-asyncapi
spec_file: asyncapi/azure-devops-hooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/asyncapi/azure-devops-hooks-asyncapi.yml
tags:
- Azure
- CI/CD
- DevOps
- Pipelines
- Work Items
- AsyncAPI
- Webhooks
- Events
version: '7.2'
---

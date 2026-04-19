---
consumed_apis:
- github-actions
- github-repos
description: Unified workflow for continuous integration and deployment combining GitHub Actions workflows, runs, jobs, artifacts, and repository management. Used by DevOps engineers for pipeline management, build monitoring, and deployment automation.
layout: capability
name: GitHub CI/CD
operations:
- description: List workflows
  method: GET
  name: listRepositoryWorkflows
  path: /v1/repositories/{owner}/{repo}/workflows
- description: Get a workflow
  method: GET
  name: getWorkflow
  path: /v1/repositories/{owner}/{repo}/workflows/{workflow_id}
- description: Dispatch a workflow
  method: POST
  name: createWorkflowDispatchEvent
  path: /v1/repositories/{owner}/{repo}/workflows/{workflow_id}/dispatches
- description: List workflow runs
  method: GET
  name: listWorkflowRunsForRepository
  path: /v1/repositories/{owner}/{repo}/runs
- description: Get a workflow run
  method: GET
  name: getWorkflowRun
  path: /v1/repositories/{owner}/{repo}/runs/{run_id}
- description: Cancel a workflow run
  method: POST
  name: cancelWorkflowRun
  path: /v1/repositories/{owner}/{repo}/runs/{run_id}/cancel
- description: List jobs
  method: GET
  name: listJobsForWorkflowRun
  path: /v1/repositories/{owner}/{repo}/runs/{run_id}/jobs
- description: List artifacts
  method: GET
  name: listArtifactsForRepository
  path: /v1/repositories/{owner}/{repo}/artifacts
- description: List secrets
  method: GET
  name: listRepositorySecrets
  path: /v1/repositories/{owner}/{repo}/secrets
- description: List deployments
  method: GET
  name: listDeployments
  path: /v1/repositories/{owner}/{repo}/deployments
- description: List environments
  method: GET
  name: listEnvironments
  path: /v1/repositories/{owner}/{repo}/environments
personas: []
provider_name: GitHub
provider_slug: github
search_terms:
- trigger workflow runs
- software development
- ci/cd
- list runs
- download job logs
- get a workflow run
- dispatch workflow
- enable a workflow
- pipelines
- enable workflow
- create a release
- code
- listRepositorySecrets
- platform
- listDeployments
- workflows
- listArtifactsForRepository
- list repository workflows
- list jobs for a workflow run
- deployment management
- rerun failed jobs
- disable workflow
- get run
- list runners
- individual workflow operations
- create or update a secret
- createWorkflowDispatchEvent
- cancel run
- environment management
- create release
- getWorkflow
- workflow listing and dispatch
- workflow run jobs
- list github actions caches
- re-run a workflow
- get job
- rerun workflow
- cancelWorkflowRun
- source control
- actions
- getWorkflowRun
- list secrets
- listJobsForWorkflowRun
- list caches
- get a repository
- individual run operations
- list variables
- listWorkflowRunsForRepository
- listRepositoryWorkflows
- artifact management
- t1
- list self-hosted runners
- list artifacts
- list workflow runs
- list repository secrets
- listEnvironments
- get a workflow
- list releases
- create or update secret
- download artifact
- get repository
- get a job
- re-run failed jobs
- get workflow
- download an artifact
- list repository variables
- list workflows
- secret management
- list deployments
- trigger a workflow dispatch event
- dispatch a workflow
- deployments
- list jobs
- github
- devops
- cancel a workflow run
- disable a workflow
- workflow run management
- list environments
slug: ci-cd
tags:
- GitHub
- CI/CD
- Actions
- Workflows
- DevOps
- Deployments
tools:
- description: List repository workflows
  hints:
    readOnly: true
  name: list-workflows
- description: Get a workflow
  hints:
    readOnly: true
  name: get-workflow
- description: Trigger a workflow dispatch event
  hints: {}
  name: dispatch-workflow
- description: Enable a workflow
  hints: {}
  name: enable-workflow
- description: Disable a workflow
  hints: {}
  name: disable-workflow
- description: List workflow runs
  hints:
    readOnly: true
  name: list-runs
- description: Get a workflow run
  hints:
    readOnly: true
  name: get-run
- description: Cancel a workflow run
  hints: {}
  name: cancel-run
- description: Re-run a workflow
  hints: {}
  name: rerun-workflow
- description: Re-run failed jobs
  hints: {}
  name: rerun-failed-jobs
- description: List jobs for a workflow run
  hints:
    readOnly: true
  name: list-jobs
- description: Get a job
  hints:
    readOnly: true
  name: get-job
- description: Download job logs
  hints:
    readOnly: true
  name: download-job-logs
- description: List artifacts
  hints:
    readOnly: true
  name: list-artifacts
- description: Download an artifact
  hints:
    readOnly: true
  name: download-artifact
- description: List repository secrets
  hints:
    readOnly: true
  name: list-secrets
- description: Create or update a secret
  hints:
    idempotent: true
  name: create-or-update-secret
- description: List repository variables
  hints:
    readOnly: true
  name: list-variables
- description: List self-hosted runners
  hints:
    readOnly: true
  name: list-runners
- description: List GitHub Actions caches
  hints:
    readOnly: true
  name: list-caches
- description: Get a repository
  hints:
    readOnly: true
  name: get-repository
- description: List releases
  hints:
    readOnly: true
  name: list-releases
- description: Create a release
  hints: {}
  name: create-release
---

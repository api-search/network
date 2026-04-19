---
consumed_apis:
- cloud-rest-api
description: Workflow capability for code collaboration using Bitbucket - managing repositories, pull requests, code reviews, and CI/CD pipelines. Used by developers and DevOps engineers.
layout: capability
name: Bitbucket Code Collaboration
operations:
- description: List repositories
  method: GET
  name: list-repositories
  path: /v1/repositories
- description: Create a repository
  method: POST
  name: create-repository
  path: /v1/repositories
- description: Get repository details
  method: GET
  name: get-repository
  path: /v1/repositories
- description: List pull requests
  method: GET
  name: list-pullrequests
  path: /v1/pullrequests
- description: Create a pull request
  method: POST
  name: create-pullrequest
  path: /v1/pullrequests
- description: Merge a pull request
  method: POST
  name: merge-pullrequest
  path: /v1/pullrequests
- description: List pipelines
  method: GET
  name: list-pipelines
  path: /v1/pipelines
- description: Trigger a pipeline
  method: POST
  name: trigger-pipeline
  path: /v1/pipelines
personas: []
provider_name: Bitbucket
provider_slug: bitbucket
search_terms:
- list pull requests
- list pull requests for a repository
- Developer
- trigger a pipeline
- merge pullrequest
- ci/cd
- get pullrequest
- continuous integration and deployment pipelines
- atlassian
- trigger pipeline
- manages ci/cd pipelines, deployments, and repository settings
- list pullrequests
- get repository details
- decline a pull request
- code review
- merge a pull request
- managing git repositories, branches, and commits
- list repositories in a workspace
- pull requests
- list ci/cd pipelines
- writes code, creates pull requests, and reviews code
- ci/cd pipeline management
- DevOps Engineer
- version control
- delete a repository
- pull request workflows and code reviews
- list pipelines
- get pull request details
- devops
- pull request management
- decline pullrequest
- code collaboration
- repository hosting
- git
- create pullrequest
- get repository
- list repositories
- repository management, pull requests, code reviews, and ci/cd pipelines
- stop pipeline
- create repository
- get pipeline execution details
- create a repository
- create a new git repository
- create a new pull request
- create a pull request
- get pipeline
- stop a running pipeline
- repository management
- bitbucket
- delete repository
- trigger a new ci/cd pipeline
slug: code-collaboration
tags:
- Bitbucket
- Code Collaboration
- CI/CD
- DevOps
- Pull Requests
tools:
- description: List repositories in a workspace
  hints:
    openWorld: true
    readOnly: true
  name: list-repositories
- description: Get repository details
  hints:
    readOnly: true
  name: get-repository
- description: Create a new Git repository
  hints:
    readOnly: false
  name: create-repository
- description: Delete a repository
  hints:
    destructive: true
  name: delete-repository
- description: List pull requests for a repository
  hints:
    openWorld: true
    readOnly: true
  name: list-pullrequests
- description: Create a new pull request
  hints:
    readOnly: false
  name: create-pullrequest
- description: Get pull request details
  hints:
    readOnly: true
  name: get-pullrequest
- description: Merge a pull request
  hints:
    readOnly: false
  name: merge-pullrequest
- description: Decline a pull request
  hints:
    readOnly: false
  name: decline-pullrequest
- description: List CI/CD pipelines
  hints:
    openWorld: true
    readOnly: true
  name: list-pipelines
- description: Trigger a new CI/CD pipeline
  hints:
    readOnly: false
  name: trigger-pipeline
- description: Get pipeline execution details
  hints:
    readOnly: true
  name: get-pipeline
- description: Stop a running pipeline
  hints:
    destructive: true
  name: stop-pipeline
---

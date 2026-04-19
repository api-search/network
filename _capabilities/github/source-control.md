---
consumed_apis:
- github-repos
- github-pull-requests
description: Unified workflow for source code management combining repositories, branches, pull requests, and commits. Used by developers for day-to-day code collaboration, branch management, code review, and merging.
layout: capability
name: GitHub Source Control
operations:
- description: List public repositories
  method: GET
  name: listPublicRepositories
  path: /v1/repositories
- description: Search repositories
  method: GET
  name: searchRepositories
  path: /v1/repositories
- description: Get a repository
  method: GET
  name: getRepository
  path: /v1/repositories/{owner}/{repo}
- description: Update a repository
  method: PATCH
  name: updateRepository
  path: /v1/repositories/{owner}/{repo}
- description: Get a branch
  method: GET
  name: getBranch
  path: /v1/repositories/{owner}/{repo}/branches/{branch}
- description: List commits
  method: GET
  name: listCommits
  path: /v1/repositories/{owner}/{repo}/commits
- description: Compare two commits
  method: GET
  name: compareTwoCommits
  path: /v1/repositories/{owner}/{repo}/compare/{basehead}
- description: List pull requests
  method: GET
  name: listPullRequests
  path: /v1/repositories/{owner}/{repo}/pulls
- description: Create a pull request
  method: POST
  name: createPullRequest
  path: /v1/repositories/{owner}/{repo}/pulls
- description: Get a pull request
  method: GET
  name: getPullRequest
  path: /v1/repositories/{owner}/{repo}/pulls/{pull_number}
- description: Update a pull request
  method: PATCH
  name: updatePullRequest
  path: /v1/repositories/{owner}/{repo}/pulls/{pull_number}
- description: Merge a pull request
  method: PUT
  name: mergePullRequest
  path: /v1/repositories/{owner}/{repo}/pulls/{pull_number}/merge
- description: List reviews
  method: GET
  name: listReviewsForPullRequest
  path: /v1/repositories/{owner}/{repo}/pulls/{pull_number}/reviews
- description: Create a review
  method: POST
  name: createReviewForPullRequest
  path: /v1/repositories/{owner}/{repo}/pulls/{pull_number}/reviews
- description: List releases
  method: GET
  name: listReleases
  path: /v1/repositories/{owner}/{repo}/releases
- description: Create a release
  method: POST
  name: createRelease
  path: /v1/repositories/{owner}/{repo}/releases
- description: Get repository content
  method: GET
  name: getRepositoryContent
  path: /v1/repositories/{owner}/{repo}/contents/{path}
- description: Create or update file contents
  method: PUT
  name: createOrUpdateFileContents
  path: /v1/repositories/{owner}/{repo}/contents/{path}
personas: []
provider_name: GitHub
provider_slug: github
search_terms:
- request reviewers for a pull request
- get a commit
- repositories
- software development
- mergePullRequest
- branches
- getBranch
- get pull request
- searchRepositories
- merge a branch
- list reviews
- pull request merge
- update pull request
- createPullRequest
- pipelines
- getRepositoryContent
- create a release
- code
- platform
- getPullRequest
- createReviewForPullRequest
- release management
- request reviewers
- create a review for a pull request
- create or update file contents
- merge a pull request
- create pull request
- pull requests
- create release
- pull request management
- commit operations
- list repository tags
- listReleases
- compareTwoCommits
- source control
- create a review
- create or update file
- list pull request files
- update branch protection
- repository management
- list pull requests
- update a pull request
- getRepository
- updateRepository
- get a repository
- t1
- branch operations
- get a branch
- compare commits
- search repositories
- get branch
- list public repositories
- list releases
- get repository
- get repository content
- merge branch
- individual pull request operations
- code review management
- repository listing and search
- updatePullRequest
- get a pull request
- listCommits
- get content
- listPublicRepositories
- listPullRequests
- submit review
- code review
- repository content management
- update a repository
- list pr files
- compare two commits
- merge pull request
- createOrUpdateFileContents
- github
- list tags
- create review
- list commits
- listReviewsForPullRequest
- get commit
- createRelease
- submit a review for a pull request
- list reviews for a pull request
- create a pull request
slug: source-control
tags:
- GitHub
- Source Control
- Repositories
- Pull Requests
- Code Review
- Branches
tools:
- description: Get a repository
  hints:
    readOnly: true
  name: get-repository
- description: Search repositories
  hints:
    readOnly: true
  name: search-repositories
- description: Get a branch
  hints:
    readOnly: true
  name: get-branch
- description: List commits
  hints:
    readOnly: true
  name: list-commits
- description: Get a commit
  hints:
    readOnly: true
  name: get-commit
- description: Compare two commits
  hints:
    readOnly: true
  name: compare-commits
- description: Get repository content
  hints:
    readOnly: true
  name: get-content
- description: Create or update file contents
  hints:
    idempotent: true
  name: create-or-update-file
- description: Merge a branch
  hints: {}
  name: merge-branch
- description: List pull requests
  hints:
    readOnly: true
  name: list-pull-requests
- description: Create a pull request
  hints: {}
  name: create-pull-request
- description: Get a pull request
  hints:
    readOnly: true
  name: get-pull-request
- description: Update a pull request
  hints:
    idempotent: true
  name: update-pull-request
- description: Merge a pull request
  hints: {}
  name: merge-pull-request
- description: List reviews for a pull request
  hints:
    readOnly: true
  name: list-reviews
- description: Create a review for a pull request
  hints: {}
  name: create-review
- description: Submit a review for a pull request
  hints: {}
  name: submit-review
- description: Request reviewers for a pull request
  hints: {}
  name: request-reviewers
- description: List pull request files
  hints:
    readOnly: true
  name: list-pr-files
- description: List releases
  hints:
    readOnly: true
  name: list-releases
- description: Create a release
  hints: {}
  name: create-release
- description: List repository tags
  hints:
    readOnly: true
  name: list-tags
- description: Update branch protection
  hints:
    idempotent: true
  name: update-branch-protection
---

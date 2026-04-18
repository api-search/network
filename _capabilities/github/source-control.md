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
- create a pull request
- getPullRequest
- listReviewsForPullRequest
- repository listing and search
- get a branch
- branch operations
- commit operations
- request reviewers
- github
- code review management
- list reviews for a pull request
- submit review
- get repository content
- platform
- get a commit
- create or update file
- list pull request files
- list public repositories
- code review
- getBranch
- repositories
- branches
- createPullRequest
- createRelease
- list commits
- mergePullRequest
- list pull requests
- list reviews
- get pull request
- listCommits
- release management
- listPublicRepositories
- pull request management
- update a pull request
- pull request merge
- compare commits
- createOrUpdateFileContents
- repository management
- getRepositoryContent
- merge a pull request
- updatePullRequest
- getRepository
- create pull request
- request reviewers for a pull request
- create review
- create a review
- createReviewForPullRequest
- update pull request
- list releases
- list tags
- get commit
- source control
- compare two commits
- create release
- get repository
- get a pull request
- listReleases
- t1
- merge branch
- list pr files
- search repositories
- get branch
- searchRepositories
- code
- software development
- repository content management
- listPullRequests
- create or update file contents
- merge a branch
- updateRepository
- create a review for a pull request
- create a release
- pipelines
- individual pull request operations
- pull requests
- list repository tags
- submit a review for a pull request
- get content
- get a repository
- update a repository
- compareTwoCommits
- merge pull request
- update branch protection
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

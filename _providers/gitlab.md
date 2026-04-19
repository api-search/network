---
api_count: 41
apis:
- description: 'GraphQL is a query language for APIs. You can use it to request the exact data you need, and therefore limit the number of requests you need. GraphQL data is arranged in types, so your client can use '
  name: GitLab GraphQL API
  slug: gitlab-graphql-api
- description: The GitLab Groups API allows you to create, read, update, and delete groups and subgroups. Groups are used to manage access control and organize projects within a GitLab instance, enabling teams to co
  name: GitLab Groups API
  slug: apiv4groups
- description: The GitLab Projects API provides programmatic access to GitLab projects, enabling you to create, list, update, and delete projects. It supports managing project settings, members, forks, stars, and ot
  name: GitLab Projects API
  slug: apiv4projects
- description: The GitLab Admin API provides administrative endpoints for managing a GitLab instance. It includes operations for managing runners, CI/CD variables, Sidekiq queues, and other instance-level administra
  name: GitLab Admin API
  slug: apiv4admin
- description: The GitLab Applications API allows you to manage OAuth applications registered in GitLab. You can create, list, and delete OAuth applications that enable third-party services to access GitLab resource
  name: GitLab Applications API
  slug: apiv4applications
- description: 'The GitLab Avatar API allows you to retrieve avatar images for users and groups. It returns avatar URLs based on user email addresses, enabling applications to display profile images for GitLab users '
  name: GitLab Avatar API
  slug: apiv4avatar
- description: The GitLab Broadcast Messages API allows administrators to create and manage broadcast messages that appear as banners across all GitLab pages. These messages are used to communicate announcements, ma
  name: GitLab Broadcast Messages API
  slug: apiv4broadcast-messages
- description: The GitLab Bulk Imports API enables migration of groups and projects between GitLab instances. It provides endpoints for initiating bulk import operations and tracking their progress, facilitating lar
  name: GitLab Bulk Imports API
  slug: apiv4bulk-imports
- description: The GitLab Application Settings API provides access to instance-wide configuration settings for a GitLab installation. Administrators can retrieve and modify application settings such as sign-up restr
  name: GitLab Application Settings API
  slug: apiv4application
- description: 'The GitLab Metadata API provides information about the GitLab instance, including the version, revision, and other metadata about the running installation. It is useful for verifying connectivity and '
  name: GitLab Metadata API
  slug: apiv4metadata
- description: The GitLab Version API returns version and revision information for the GitLab instance. This endpoint is useful for verifying what version of GitLab is running and for checking compatibility with spe
  name: GitLab Version API
  slug: apiv4version
- description: The GitLab REST API provides programmatic access to GitLab resources, enabling you to build integrations, automate repetitive tasks, and extract data for custom reports. The API supports projects, gro
  name: GitLab REST API
  slug: gitlab-rest-api
- description: 'The GitLab OAuth 2.0 API enables third-party services to access GitLab resources on behalf of users using the OAuth 2.0 protocol. It supports authorization code with PKCE, device authorization grant, '
  name: GitLab OAuth 2.0 API
  slug: gitlab-oauth2-api
- description: GitLab Webhooks allow you to receive real-time HTTP POST notifications when events occur in GitLab projects or groups. Webhooks can be configured to trigger on events such as push events, merge reques
  name: GitLab Webhooks
  slug: gitlab-webhooks
- description: The GitLab Issues API provides programmatic access to manage issues across projects and groups. It supports creating, listing, updating, and deleting issues, as well as managing issue assignments, lab
  name: GitLab Issues API
  slug: apiv4issues
- description: The GitLab Merge Requests API enables programmatic management of merge requests across projects and groups. It supports creating, listing, updating, approving, and merging merge requests, as well as m
  name: GitLab Merge Requests API
  slug: apiv4merge-requests
- description: The GitLab Pipelines API provides programmatic access to CI/CD pipelines in GitLab projects. It supports listing, creating, retrying, and canceling pipelines, as well as retrieving pipeline details an
  name: GitLab Pipelines API
  slug: apiv4pipelines
- description: 'The GitLab Jobs API allows you to interact with CI/CD jobs in GitLab projects. It supports listing, retrieving, canceling, retrying, and erasing jobs, as well as downloading job artifacts and viewing '
  name: GitLab Jobs API
  slug: apiv4jobs
- description: The GitLab Runners API provides endpoints for managing CI/CD runners registered to a GitLab instance. It supports listing, registering, updating, and deleting runners, as well as managing runner confi
  name: GitLab Runners API
  slug: apiv4runners
- description: The GitLab Users API provides programmatic access to manage user accounts on a GitLab instance. It supports listing, creating, updating, and deleting users, managing SSH keys and GPG keys, viewing use
  name: GitLab Users API
  slug: apiv4users
- description: The GitLab Repositories API provides access to Git repository data within GitLab projects. It supports listing repository tree structures, retrieving file contents, comparing branches and tags, downlo
  name: GitLab Repositories API
  slug: apiv4repositories
- description: The GitLab Commits API provides programmatic access to Git commits within GitLab projects. It supports listing, creating, and retrieving commits, viewing commit diffs and comments, cherry-picking comm
  name: GitLab Commits API
  slug: apiv4commits
- description: The GitLab Branches API enables programmatic management of Git branches within GitLab projects. It supports listing, creating, and deleting branches, as well as retrieving branch details including the
  name: GitLab Branches API
  slug: apiv4branches
- description: The GitLab Tags API provides programmatic access to manage Git tags within GitLab projects. It supports listing, creating, and deleting tags, as well as retrieving tag details for version management a
  name: GitLab Tags API
  slug: apiv4tags
- description: The GitLab Releases API enables programmatic management of project releases. It supports creating, listing, updating, and deleting releases, as well as managing release assets and links for distributi
  name: GitLab Releases API
  slug: apiv4releases
- description: 'The GitLab Environments API provides programmatic access to manage deployment environments within GitLab projects. It supports creating, listing, updating, stopping, and deleting environments used to '
  name: GitLab Environments API
  slug: apiv4environments
- description: The GitLab Deployments API enables programmatic access to deployment records in GitLab projects. It supports listing, creating, and updating deployments, as well as retrieving deployment details and m
  name: GitLab Deployments API
  slug: apiv4deployments
- description: The GitLab Pipeline Schedules API provides programmatic access to manage scheduled CI/CD pipelines. It supports creating, listing, updating, and deleting pipeline schedules, as well as managing schedu
  name: GitLab Pipeline Schedules API
  slug: apiv4pipeline-schedules
- description: 'The GitLab Labels API provides programmatic access to manage project labels. It supports creating, listing, updating, deleting, and subscribing to labels used for categorizing issues, merge requests, '
  name: GitLab Labels API
  slug: apiv4labels
- description: The GitLab Milestones API provides programmatic access to manage project milestones. It supports creating, listing, updating, and deleting milestones, as well as retrieving issues and merge requests a
  name: GitLab Milestones API
  slug: apiv4milestones
- description: The GitLab Notes API provides programmatic access to manage comments and system notes on issues, merge requests, epics, and snippets. It supports creating, listing, updating, and deleting notes for co
  name: GitLab Notes API
  slug: apiv4notes
- description: The GitLab Snippets API provides programmatic access to manage code snippets. It supports creating, listing, updating, and deleting both personal and project snippets, enabling sharing of code fragmen
  name: GitLab Snippets API
  slug: apiv4snippets
- description: The GitLab Packages API provides programmatic access to the GitLab Package Registry. It supports listing, retrieving, and deleting packages across projects and groups, with support for multiple packag
  name: GitLab Packages API
  slug: apiv4packages
- description: The GitLab Container Registry API provides programmatic access to manage container images stored in the GitLab Container Registry. It supports listing repositories and tags, deleting images, and manag
  name: GitLab Container Registry API
  slug: apiv4container-registry
- description: The GitLab Vulnerabilities API provides programmatic access to manage security vulnerabilities detected in GitLab projects. It supports retrieving, confirming, resolving, and dismissing vulnerabilitie
  name: GitLab Vulnerabilities API
  slug: apiv4vulnerabilities
- description: The GitLab Deploy Keys API provides programmatic access to manage deploy keys for GitLab projects. It supports listing, creating, updating, and deleting SSH deploy keys that grant read-only or read-wr
  name: GitLab Deploy Keys API
  slug: apiv4deploy-keys
- description: The GitLab Protected Branches API provides programmatic access to manage branch protection rules. It supports listing, creating, updating, and removing protection settings that control who can push, m
  name: GitLab Protected Branches API
  slug: apiv4protected-branches
- description: The GitLab Wikis API provides programmatic access to manage project wiki pages. It supports listing, creating, updating, and deleting wiki pages, as well as uploading attachments, enabling teams to ma
  name: GitLab Wikis API
  slug: apiv4wikis
- description: The GitLab Events API provides programmatic access to review event activity across GitLab. It supports listing all events, retrieving user contribution events, and viewing project-specific events such
  name: GitLab Events API
  slug: apiv4events
- description: 'The GitLab Search API enables programmatic search across a GitLab instance, group, or project. It supports searching for projects, issues, merge requests, milestones, code blobs, commits, notes, wiki '
  name: GitLab Search API
  slug: apiv4search
- description: The GitLab Namespaces API provides programmatic access to manage namespaces in GitLab. It supports listing namespaces, retrieving namespace details, and verifying namespace existence, which is essenti
  name: GitLab Namespaces API
  slug: apiv4namespaces
asyncapis:
- description: GitLab Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in a GitLab project or group, such as pushes, merge requests, issues, pipeline status changes, and deploy
  name: GitLab Webhooks
  slug: gitlab-webhooks-asyncapi
capabilities:
- description: Unified capability for GitLab OAuth 2.0 authentication flows and user identity. Enables developers and platform administrators to manage OAuth application authorization, token lifecycle, and authentic
  name: GitLab Authentication And Identity
  slug: authentication-and-identity
- description: Unified capability for managing GitLab project webhooks, including CRUD operations, custom header and URL variable configuration, delivery event history, and testing. Used by DevOps engineers and plat
  name: GitLab Webhook Management
  slug: webhook-management
common:
- title: ''
  type: Website
  url: https://about.gitlab.com/
- title: ''
  type: Portal
  url: https://docs.gitlab.com/api/
- title: ''
  type: Documentation
  url: https://docs.gitlab.com/
- title: ''
  type: Authentication
  url: https://docs.gitlab.com/api/rest/authentication/
- title: ''
  type: GitHubOrganization
  url: https://github.com/gitlabhq
- title: ''
  type: Blog
  url: https://about.gitlab.com/blog/
- title: ''
  type: StatusPage
  url: https://status.gitlab.com/
- title: ''
  type: Pricing
  url: https://about.gitlab.com/pricing/
- title: ''
  type: TermsOfService
  url: https://about.gitlab.com/terms/
- title: ''
  type: PrivacyPolicy
  url: https://about.gitlab.com/privacy/
- title: ''
  type: Support
  url: https://about.gitlab.com/company/contact/
- title: ''
  type: IDESupport
  url: https://docs.gitlab.com/ee/editor_extensions/
- title: ''
  type: ReleaseNotes
  url: https://about.gitlab.com/releases/categories/releases/
- title: ''
  type: Portal
  url: https://developer.gitlab.com/
- title: ''
  type: Documentation
  url: https://docs.gitlab.com/
- title: ''
  type: GettingStarted
  url: https://about.gitlab.com/get-started/
- title: ''
  type: StatusPage
  url: https://status.gitlab.com/
- title: ''
  type: SignUp
  url: https://gitlab.com/users/sign_up
- title: ''
  type: Blog
  url: https://about.gitlab.com/blog/
- title: ''
  type: Support
  url: https://about.gitlab.com/support/
- title: ''
  type: ChangeLog
  url: https://gitlab.com/gitlab-org/gitlab/blob/master/CHANGELOG.md
- title: ''
  type: Authentication
  url: https://docs.gitlab.com/api/rest/authentication/
- title: ''
  type: SDK
  url: https://docs.gitlab.com/api/rest/third_party_clients/
- title: ''
  type: Support
  url: https://forum.gitlab.com/
- title: ''
  type: RateLimits
  url: https://docs.gitlab.com/security/rate_limits/
- title: ''
  type: JSONLD
  url: json-ld/gitlab-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/gitlab-project-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/gitlab-merge-request-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/gitlab-issue-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/gitlab-pipeline-schema.json
- title: ''
  type: Pricing
  url: https://about.gitlab.com/pricing/
- title: ''
  type: Security
  url: https://about.gitlab.com/security/
- title: ''
  type: Security
  url: https://about.gitlab.com/security/disclosure/
- title: ''
  type: Documentation
  url: https://about.gitlab.com/direction/
- title: ''
  type: Partners
  url: https://about.gitlab.com/partners/technology-partners/
- title: ''
  type: Documentation
  url: https://about.gitlab.com/solutions/open-source/
- title: ''
  type: Marketplace
  url: https://marketplace.gitlab.com/
- title: ''
  type: Tools
  url: https://docs.gitlab.com/api/openapi/openapi_interactive/
- title: ''
  type: GitHubRepository
  url: https://gitlab.com/gitlab-org/gitlab
created: 2023/11/10
description: GitLab Inc. is an open-core company that develops GitLab, a DevOps software platform for building, securing, and managing applications. Created by Ukrainian developer Dmytro Zaporozhets and Dutch developer Sytse Sijbrandij, GitLab became the first partly-Ukrainian unicorn in 2018. Known for promoting remote work, it is one of the largest all-remote companies globally. GitLab has approximately 30 million registered users, including 1 million active licensed users.
features:
- description: Comprehensive REST API for managing projects, groups, users, issues, merge requests, pipelines, and all GitLab resources.
  name: REST API v4
- description: Flexible query language API for requesting exactly the data you need with a versionless, non-breaking schema.
  name: GraphQL API
- description: Programmatically manage pipelines, jobs, runners, and deployment workflows.
  name: CI/CD Pipelines
- description: Manage container images and repositories for Docker image lifecycle management.
  name: Container Registry
- description: Publish and manage packages across npm, Maven, PyPI, NuGet, Conan, and other formats.
  name: Package Registry
- description: Receive real-time notifications for events across projects, groups, and system-level actions.
  name: Webhooks
- description: Standards-based OAuth 2.0 and OpenID Connect authentication for third-party applications.
  name: OAuth 2.0 Authentication
- description: Access SAST, DAST, dependency scanning, and container scanning results through APIs.
  name: Security Scanning
- description: Full lifecycle management of merge requests including creation, review, approval, and merge.
  name: Merge Request Management
- description: Create, manage, and query issues with labels, milestones, weights, and custom fields.
  name: Issue Tracking
- description: Manage repository files, branches, tags, commits, and merge operations.
  name: Repository Management
- description: Create and configure groups, subgroups, and projects with membership and permissions.
  name: Group and Project Management
image: /assets/icons/gitlab.png
integrations: []
jsonld:
- class_count: 38
  name: Gitlab Context
  property_count: 268
  slug: gitlab-context
layout: provider
modified: '2026-04-17'
name: GitLab
rules:
- name: GitLab API Rules
  rule_count: 24
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 6
  slug: gitlab-spectral-rules
skills: []
slug: gitlab
solutions:
- description: Core DevOps platform with unlimited repositories, CI/CD, issue tracking, and API access.
  name: GitLab Free
- description: Advanced DevOps with merge request approvals, code owners, and priority support.
  name: GitLab Premium
- description: Enterprise DevOps with security scanning, compliance, and advanced API features.
  name: GitLab Ultimate
- description: Single-tenant SaaS deployment with dedicated infrastructure and enhanced security.
  name: GitLab Dedicated
tags:
- Code
- Platform
- Software Development
- Source Control
url: https://raw.githubusercontent.com/api-search/code/main/_apis/gitlab/apis.md
use_cases:
- description: Automate CI/CD pipeline creation, runner management, and deployment workflows.
  name: DevOps Automation
- description: Programmatically manage issues, milestones, boards, and merge requests.
  name: Project Management
- description: Manage GitLab configuration, groups, projects, and settings through APIs.
  name: Infrastructure as Code
- description: Access vulnerability reports, security scan results, and compliance data.
  name: Security and Compliance
- description: Bulk import projects, users, and data from other platforms.
  name: Migration and Integration
- description: Build custom developer tools, dashboards, and bots for GitLab workflows.
  name: Custom Tooling
- description: Manage Docker images, Kubernetes clusters, and container deployments.
  name: Container Management
- description: Extract project analytics, contribution data, and productivity metrics.
  name: Analytics and Reporting
---

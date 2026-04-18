---
api_count: 65
apis:
- description: 'The GitHub App API is the set of REST/GraphQL endpoints and webhooks that lets a GitHub App securely integrate with and automate work across GitHub. Apps authenticate with a shortlived JSON Web Token '
  name: GitHub App API
  slug: github-app-api
- description: The GitHub Authorization (OAuth Authorizations) API historically let you programmatically create, list, inspect, and revoke access tokens for a user or OAuth applicationsetting scopes, verifying token
  name: GitHub Authorization API
  slug: github-auth-api
- description: GitHubs Code of Conduct API lets apps discover and retrieve the community codes of conduct that GitHub supports and see which one a repository has adopted. Through REST endpoints, clients can list ava
  name: GitHub Code of Conduct API
  slug: github-code-of-conduct-api
- description: The GitHub Emojis API is a simple REST endpoint (GET /emojis or https://api.github.com/emojis) that returns a JSON dictionary mapping emoji shortcodes (like "smile" or "octocat") to the image URLs Git
  name: GitHub Emojis API
  slug: github-emojis-api
- description: The GitHub Events API provides a read-only feed of recent activity on GitHub, exposing structured event objects you can poll to see what happened across the platform or within a specific repository, o
  name: GitHub Events API
  slug: github-events-api
- description: GitHubs Feeds API lets you programmatically discover the Atom feed URLs for GitHub activity thats relevant to you, such as the global timeline, a specific users activity, the authenticated users publi
  name: GitHub Feeds API
  slug: github-feeds-api
- description: The GitHub Gists API lets you programmatically manage gistslightweight code snippets and notesover HTTP. You can create gists (public or secret/unlisted), read individual gists, list public gists, you
  name: GitHub Gists API
  slug: github-gists-api
- description: The GitHub Gitignore Templates API is a REST interface that lets you discover and fetch canonical .gitignore templates maintained by GitHub, so you can programmatically create ignore files tailored to
  name: GitHub Gitignore Templates API
  slug: github-gitignore-templates-api
- description: The GitHub Installation API is part of the GitHub Apps platform and lets an app understand and manage where its installed and what it can access, and act on behalf of that installation. Using these en
  name: GitHub Installation API
  slug: github-installation-api
- description: The GitHub Issues API lets you programmatically manage issue tracking on GitHub, enabling you to list and filter issues across repositories, create and edit issues, change their state (open/closed), a
  name: GitHub Issues API
  slug: github-issues-api
- description: The GitHub Licenses API lets you programmatically discover and retrieve open source license information across GitHub. It provides endpoints to list the common licenses GitHub supports, get detailed m
  name: GitHub Licenses API
  slug: github-licenses-api
- description: The GitHub Enterprise Management API lets administrators automate and integrate the operational and security management of their enterprise on GitHub. It covers tasks like provisioning and governing o
  name: GitHub Enterprise Management API
  slug: github-manage-api
- description: The GitHub Markdown API is a REST service that converts Markdownespecially GitHub Flavored Markdowninto the same HTML GitHub renders in READMEs, issues, and pull requests, so external apps can display
  name: GitHub Markdown API
  slug: github-markdown-api
- description: Use the REST API to get meta information about GitHub, including the IP addresses of GitHub services.
  name: GitHub Meta API
  slug: github-meta-api
- description: GitHubs Networks API lets you retrieve a stream of public activity that occurs across a repositorys network, meaning the original repo and all of its forks. Exposed via the Events API (for example, li
  name: GitHub Networks API
  slug: github-networks-api
- description: This GitHub REST API allows you to programmatically manage your GitHub notifications, which include updates on issues, pull requests, and commits. The API requires authentication via a personal access
  name: GitHub Notifications API
  slug: github-notifications-api
- description: The GitHub Octocat API is a playful, non-functional endpoint in GitHubs REST API that returns an ASCII-art rendering of the Octocat mascot as plain text. Its primarily meant for fun and demospeople of
  name: GitHub Octocat API
  slug: github-octocat-api
- description: The GitHub Organization API lets you programmatically administer and integrate with organizations on GitHub, spanning both REST and GraphQL. It covers core governance tasks such as reading and updatin
  name: GitHub Organization API
  slug: github-org-api
- description: The GitHub Projects API enables developers to programmatically create and manage GitHub Projects, which are flexible tools for planning and tracking work using customizable boards, tables, and roadmap
  name: GitHub Projects API
  slug: github-projects-api
- description: GitHubs Rate Limit API lets you programmatically see how much API quota you have left and when it will reset, so you can avoid hitting API rate limit exceeded errors. By calling the /rate_limit endpoi
  name: GitHub Rate Limit API
  slug: github-rate-limit-api
- description: The GitHub Repos API is a set of REST endpoints that let you programmatically create, read, update, and delete repositories and their resources, giving you control over a repos lifecycle and configura
  name: GitHub Repos API
  slug: github-repos-api
- description: GitHubs SCIM API implements the SCIM 2.0 standard to automate user lifecycle management from an identity provider (such as Entra ID/Azure AD, Okta, or OneLogin) to GitHub Enterprise Cloud. It lets you
  name: GitHub SCIM API
  slug: github-scim-api
- description: The GitHub Search API lets you programmatically find and filter content across GitHubincluding repositories, code, issues and pull requests, commits, users, topics, and labelsusing a powerful query la
  name: GitHub Search API
  slug: github-search-api
- description: The GitHub Setup API is the administrative interface for GitHub Enterprise Server that lets you automate tasks normally done in the Management Console during first-time and ongoing configuration. It p
  name: GitHub Setup API
  slug: github-setup-api
- description: The GitHub Teams API lets you programmatically manage organization teams and the access they grant. With it, you can create, update, and delete teams; organize parent/child team hierarchies; add or re
  name: GitHub Teams API
  slug: github-teams-api
- description: The GitHub Zen API is a playful REST endpoint that returns a random aphorism from the Zen of GitHub, such as Keep it logically awesome. Each request to GET https://api.github.com/zen responds with a s
  name: GitHub Zen API
  slug: github-zen-api
- description: The GitHub Users API (part of the REST API) lets applications read and, for the authenticated account, manage user-related data on GitHub. It can fetch public profiles for any user or the authenticate
  name: GitHub User API
  slug: github-user-api
- description: The GitHub Actions API lets you manage and automate GitHub Actions workflows, including creating and managing workflow runs, jobs, artifacts, caches, secrets, variables, self-hosted runners, and runne
  name: GitHub Actions API
  slug: github-actions-api
- description: The GitHub Branches API lets you list, create, and manage branches in a repository, including configuring branch protection rules that enforce required status checks, pull request reviews, signed comm
  name: GitHub Branches API
  slug: github-branches-api
- description: 'The GitHub Code Scanning API lets you retrieve and manage code scanning alerts for a repository. Code scanning uses CodeQL or third-party analysis tools to find potential security vulnerabilities and '
  name: GitHub Code Scanning API
  slug: github-code-scanning-api
- description: 'The GitHub Collaborators API lets you manage access to repositories by adding, removing, and listing collaborators, checking permissions, and managing repository invitations. It supports fine-grained '
  name: GitHub Collaborators API
  slug: github-collaborators-api
- description: The GitHub Dependabot API lets you manage Dependabot alerts and secrets for repositories and organizations. It provides endpoints to list, get, and update Dependabot alerts for vulnerable dependencies
  name: GitHub Dependabot API
  slug: github-dependabot-api
- description: The GitHub Webhooks API lets you create and manage webhooks for repositories and organizations. Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur, such as pushes,
  name: GitHub Webhooks API
  slug: github-webhooks-api
- description: The GitHub Pull Requests API lets you create, list, update, and merge pull requests in a repository. It provides endpoints for managing pull request reviews, review comments, review requests, and merg
  name: GitHub Pull Requests API
  slug: github-pull-requests-api
- description: The GitHub Tags API lets you create and manage Git tag objects in a repository. Tags are references that point to specific commits, commonly used to mark release points. The API supports creating anno
  name: GitHub Tags API
  slug: github-tags-api
- description: 'The GitHub Checks API lets you create and manage check runs and check suites that report detailed status, annotations, and results for commits. It enables CI/CD tools and integrations to report build '
  name: GitHub Checks API
  slug: github-checks-api
- description: 'The GitHub Deployments API lets you create and manage deployments and deployment statuses for repositories. Deployments are requests to deploy a specific ref (branch, SHA, tag) to an environment, and '
  name: GitHub Deployments API
  slug: github-deployments-api
- description: The GitHub Releases API lets you create, edit, and delete releases for a repository, as well as upload and manage release assets (binaries, installers, archives). Releases are based on Git tags and pr
  name: GitHub Releases API
  slug: github-releases-api
- description: The GitHub Pages API lets you manage GitHub Pages sites for repositories, including creating, updating, and deleting sites, configuring custom domains and HTTPS enforcement, and triggering and monitor
  name: GitHub Pages API
  slug: github-pages-api
- description: The GitHub Packages API lets you manage packages and package versions in GitHub Packages, a software package hosting service that supports npm, Maven, Gradle, RubyGems, NuGet, Docker, and other packag
  name: GitHub Packages API
  slug: github-packages-api
- description: The GitHub Git Database API provides low-level access to Git objects (blobs, commits, refs, tags, and trees) in a repository. It lets you read and write raw Git data directly, enabling operations like
  name: GitHub Git Database API
  slug: github-git-database-api
- description: The GitHub Codespaces API lets you create, manage, start, stop, and delete cloud development environments (codespaces) for repositories. It provides endpoints for managing codespace secrets, machine t
  name: GitHub Codespaces API
  slug: github-codespaces-api
- description: The GitHub Copilot API lets organization and enterprise owners manage GitHub Copilot seat assignments, retrieve usage metrics and billing information, and configure Copilot policies. It provides endpo
  name: GitHub Copilot API
  slug: github-copilot-api
- description: The GitHub Billing API lets you view billing and usage information for organizations and enterprises, including Actions minutes, Packages storage and data transfer, Codespaces usage, and shared storag
  name: GitHub Billing API
  slug: github-billing-api
- description: The GitHub Migrations API lets you migrate data to and from GitHub. It supports organization migrations that export repositories and metadata as downloadable archives, source imports that convert repo
  name: GitHub Migrations API
  slug: github-migrations-api
- description: The GitHub Secret Scanning API lets you retrieve and manage secret scanning alerts for repositories, organizations, and enterprises. Secret scanning detects tokens, keys, and other credentials acciden
  name: GitHub Secret Scanning API
  slug: github-secret-scanning-api
- description: The GitHub Security Advisories API lets you view and manage security advisories for repositories and access the GitHub Advisory Database. It provides endpoints to create, update, and list repository s
  name: GitHub Security Advisories API
  slug: github-security-advisories-api
- description: The GitHub Commits API lets you list, retrieve, and compare commits in a repository, as well as manage commit comments and commit statuses. It provides endpoints for viewing commit details, listing pu
  name: GitHub Commits API
  slug: github-commits-api
- description: 'The GitHub Reactions API lets you create, list, and delete emoji reactions on issues, pull requests, issue comments, pull request review comments, commit comments, release assets, and team discussion '
  name: GitHub Reactions API
  slug: github-reactions-api
- description: The GitHub Deploy Keys API lets you manage deploy keys for repositories. Deploy keys are SSH keys that grant read-only or read-write access to a single repository, commonly used for automated deployme
  name: GitHub Deploy Keys API
  slug: github-deploy-keys-api
- description: The GitHub Dependency Graph API lets you view and submit dependency information for a repository. It provides endpoints to export the software bill of materials (SBOM) for a repository and to submit d
  name: GitHub Dependency Graph API
  slug: github-dependency-graph-api
- description: The GitHub Metrics API lets you access community profile and repository statistics, including contributor activity, commit frequency, code frequency, participation data, punch card data, and community
  name: GitHub Metrics API
  slug: github-metrics-api
- description: The GitHub Interactions API lets you temporarily restrict which users can comment, open issues, or create pull requests in public repositories. It supports setting interaction limits at the repository
  name: GitHub Interactions API
  slug: github-interactions-api
- description: The GitHub Models API provides access to the GitHub Models catalog, letting you list and retrieve details about AI models available on the GitHub platform. It supports browsing model metadata includin
  name: GitHub Models API
  slug: github-models-api
- description: The GitHub GraphQL API provides a flexible query language for accessing GitHub data, allowing clients to request exactly the fields they need in a single request. It supports queries, mutations, and s
  name: GitHub GraphQL API
  slug: github-graphql-api
- description: The GitHub Campaigns API lets organization owners and security managers create and manage security campaigns that coordinate remediation of code scanning alerts across multiple repositories. It provid
  name: GitHub Campaigns API
  slug: github-campaigns-api
- description: The GitHub Classroom API lets you programmatically interact with GitHub Classroom, providing endpoints to list classrooms, get classroom details, list assignments for a classroom, get assignment detai
  name: GitHub Classroom API
  slug: github-classroom-api
- description: The GitHub Code Security API lets organizations and enterprises create and manage reusable code security configurations that standardize security settings across repositories. It provides endpoints to
  name: GitHub Code Security API
  slug: github-code-security-api
- description: The GitHub Credentials API lets you programmatically manage authentication credentials, providing endpoints to revoke a list of credentials such as tokens and keys for security purposes. It enables au
  name: GitHub Credentials API
  slug: github-credentials-api
- description: 'The GitHub Enterprise Teams API lets enterprise owners create and manage enterprise-level teams. It provides endpoints to list, create, get, update, and delete teams, manage team membership including '
  name: GitHub Enterprise Teams API
  slug: github-enterprise-teams-api
- description: 'The GitHub Private Registries API lets organizations configure and manage private package registries. It provides endpoints to list, create, get, update, and delete private registry configurations at '
  name: GitHub Private Registries API
  slug: github-private-registries-api
- description: The GitHub Autolinks API lets repository administrators manage autolink references that automatically link issues, pull requests, commit messages, and release descriptions to external third-party serv
  name: GitHub Autolinks API
  slug: github-autolinks-api
- description: The GitHub Starring API lets you bookmark repositories and manage your starred list. It provides endpoints to list stargazers for a repository, list repositories starred by the authenticated user or a
  name: GitHub Starring API
  slug: github-starring-api
- description: The GitHub Watching API lets you subscribe to notifications for activity in a repository. It provides endpoints to list watchers of a repository, get and set a repository subscription, delete a subscr
  name: GitHub Watching API
  slug: github-watching-api
- description: The GitHub Repository Invitations API lets you manage repository collaboration invitations. It provides endpoints to list repository invitations, update an invitation, delete an invitation, list invit
  name: GitHub Repository Invitations API
  slug: github-repository-invitations-api
asyncapis:
- description: GitHub Webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur on GitHub, such as pushes, pull requests, issues, releases, and more. Webhooks can be configured at the r
  name: GitHub Webhooks
  slug: github-webhooks-asyncapi
capabilities:
- description: Unified workflow for continuous integration and deployment combining GitHub Actions workflows, runs, jobs, artifacts, and repository management. Used by DevOps engineers for pipeline management, build
  name: GitHub CI/CD
  slug: ci-cd
- description: Unified workflow for community engagement combining gists, user profiles, organizations, and team discussions. Used by community managers, developer advocates, and open source maintainers for communit
  name: GitHub Community
  slug: community
- description: Unified workflow for platform administration combining GitHub Apps, organizations, teams, and packages. Used by platform administrators for managing app integrations, organization governance, team acc
  name: GitHub Platform Administration
  slug: platform-administration
- description: Unified workflow for project management combining issues, projects, milestones, labels, and search. Used by project managers and team leads for tracking work, organizing sprints, and managing delivera
  name: GitHub Project Management
  slug: project-management
- description: Unified workflow for security operations combining code scanning, Dependabot, and secret scanning. Used by security engineers for vulnerability management, dependency auditing, and secret leak remedia
  name: GitHub Security Operations
  slug: security-operations
- description: Unified workflow for source code management combining repositories, branches, pull requests, and commits. Used by developers for day-to-day code collaboration, branch management, code review, and merg
  name: GitHub Source Control
  slug: source-control
common:
- title: ''
  type: Plans
  url: https://github.com/pricing
- title: ''
  type: RoadMap
  url: https://github.com/github/roadmap
- title: ''
  type: About
  url: https://github.com/about
- title: ''
  type: Documentation
  url: https://docs.github.com/en/get-started/exploring-integrations/about-building-integrations
- title: ''
  type: StatusPage
  url: https://www.githubstatus.com/
- title: ''
  type: CLI
  url: https://cli.github.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/github
- title: ''
  type: Support
  url: https://support.github.com/
- title: ''
  type: Partners
  url: https://github.com/partners/
- title: ''
  type: TermsOfService
  url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- title: ''
  type: RateLimits
  url: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28
- title: ''
  type: Pagination
  url: https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28
- title: ''
  type: Authentication
  url: https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
- title: ''
  type: GettingStarted
  url: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
- title: ''
  type: sdks
  url: https://docs.github.com/en/rest/overview/libraries
- title: ''
  type: Blog
  url: https://github.blog/
- title: ''
  type: Website
  url: https://github.com
- title: ''
  type: Login
  url: https://github.com/login
- title: ''
  type: SignUp
  url: https://github.com/signup
- title: ''
  type: Portal
  url: https://docs.github.com/en/rest
- title: ''
  type: ChangeLog
  url: https://github.blog/changelog/
- title: ''
  type: Community
  url: https://github.com/orgs/community/discussions
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/github-api
- title: ''
  type: YouTube
  url: https://www.youtube.com/github
- title: ''
  type: Security
  url: https://github.com/security
- title: ''
  type: DeveloperTools
  url: https://docs.github.com/en/graphql/overview/explorer
- title: ''
  type: OpenAPI
  url: https://github.com/github/rest-api-description
- title: ''
  type: Versioning
  url: https://docs.github.com/en/rest/about-the-rest-api/api-versions
- title: ''
  type: Errors
  url: https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api
- title: ''
  type: Quickstart
  url: https://docs.github.com/en/rest/quickstart
- title: ''
  type: Webhooks
  url: https://docs.github.com/en/webhooks
- title: ''
  type: X
  url: https://x.com/github
- title: ''
  type: SDKs
  url: https://github.com/octokit
- title: ''
  type: JSONSchema
  url: json-schema/github-repository-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-issue-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-pull-request-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-user-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-organization-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-commit-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-webhook-delivery-schema.json
- title: ''
  type: JSON-LD
  url: json-ld/github-context.jsonld
created: 2024/04/14
description: The GitHub REST API allows developers to programmatically interact with GitHub resources including repositories, users, organizations, pull requests, issues, and more.
features:
- description: Comprehensive REST API v3 for managing repositories, issues, pull requests, actions, and all GitHub resources.
  name: REST API
- description: Flexible GraphQL API v4 for querying exactly the data you need with a single request.
  name: GraphQL API
- description: Real-time event notifications for repository, organization, and marketplace events.
  name: Webhooks
- description: First-class integrations with fine-grained permissions, installation tokens, and webhook events.
  name: GitHub Apps
- description: CI/CD workflow automation with API access to runs, jobs, artifacts, and secrets.
  name: GitHub Actions
- description: Package registry supporting npm, Maven, NuGet, Docker, and RubyGems.
  name: Packages
- description: Search across repositories, code, issues, pull requests, and users.
  name: Code Search
- description: Dependabot alerts, code scanning, secret scanning, and security advisories.
  name: Security
- description: AI-powered code completion and chat APIs for developer tools integration.
  name: Copilot
- description: Project boards with custom fields, views, and automation for issue tracking.
  name: Projects
- description: Cloud development environments with API management for machines and secrets.
  name: Codespaces
- description: Community discussion forums with categories, comments, and reactions.
  name: Discussions
image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
integrations:
- description: GitHub integration in Visual Studio Code with Copilot, PR reviews, and Codespaces.
  name: VS Code
- description: GitHub notifications, deployments, and actions in Slack channels.
  name: Slack
- description: Link GitHub commits and PRs to Jira issues for project tracking.
  name: Jira
- description: Manage GitHub repositories, teams, and settings as infrastructure code.
  name: Terraform
- description: Cross-platform CI/CD with GitHub repos and Azure Pipelines.
  name: Azure DevOps
jsonld:
- class_count: 85
  name: Github Context
  property_count: 451
  slug: github-context
layout: provider
modified: '2026-04-17'
name: GitHub
rules:
- name: GitHub API Rules
  rule_count: 20
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 3
  slug: github-spectral-rules
skills: []
slug: github
solutions:
- description: Free tier with unlimited public and private repos, Actions minutes, and Packages storage.
  name: GitHub Free
- description: Advanced tools for individual developers with more Actions minutes and Packages.
  name: GitHub Pro
- description: Collaboration features for teams with code owners, required reviews, and Pages.
  name: GitHub Team
- description: Enterprise features with SAML SSO, audit log streaming, and advanced security.
  name: GitHub Enterprise
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
url: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/apis.yml
use_cases:
- description: Automate build, test, and deployment pipelines with GitHub Actions API.
  name: CI/CD Automation
- description: Programmatically create, configure, and manage repositories and branches.
  name: Repository Management
- description: Create, update, and query issues, labels, milestones, and project boards.
  name: Issue and Project Tracking
- description: Automate pull request reviews, checks, and merge workflows.
  name: Code Review Automation
- description: Access Dependabot alerts, code scanning results, and secret scanning alerts.
  name: Security Scanning
- description: Build GitHub Apps, CLI extensions, and IDE integrations.
  name: Developer Tools
- description: Manage teams, members, permissions, and audit logs for organizations.
  name: Organization Management
- description: Publish and manage packages across multiple package registries.
  name: Package Publishing
---

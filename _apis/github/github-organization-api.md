---
aid: github:github-org-api
name: GitHub Organization API
tags:
  - Organizations
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/orgs?apiVersion=2022-11-28
overlays:
  - url: overlays/github-org-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-org-api-openapi.yml
    type: OpenAPI
description: >-
  The GitHub Organization API lets you programmatically administer and integrate
  with organizations on GitHub, spanning both REST and GraphQL. It covers core
  governance tasks such as reading and updating org settings and policies,
  managing members and outside collaborators, sending invitations and assigning
  roles, organizing teams and their permissions, and controlling repository
  access at scale. It also supports operational and security workflows,
  including organization webhooks, audit log retrieval, required security and
  compliance settings (e.g., Dependabot and secret scanning policies),
  finegrained personal access token and GitHub App installation approvals, and
  management of Actions resources like selfhosted runners. Where applicable, it
  integrates with SSO/SCIM provisioning and exposes usage/billing and
  installation dataenabling endtoend automation of org operations, security, and
  permissions.

---
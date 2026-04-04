---
aid: github:github-manage-api
name: GitHub Enterprise Management API
tags:
  - Management
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest?apiVersion=2022-11-28
overlays:
  - url: overlays/github-manage-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-manage-api-openapi.yml
    type: OpenAPI
description: >-
  The GitHub Enterprise Management API lets administrators automate and
  integrate the operational and security management of their enterprise on
  GitHub. It covers tasks like provisioning and governing organizations, users,
  and teams; enforcing policies for repositories, security, and GitHub Actions;
  integrating identity and access management via SSO/SCIM; retrieving audit logs
  and usage data for compliance and billing; and managing self-hosted runners.
  For GitHub Enterprise Server, it also includes Management Console endpoints to
  configure instance settings (such as TLS, SMTP, and clustering), apply
  licenses, monitor health, and coordinate backups and restores. By exposing
  these controls via REST, GraphQL, and SCIM endpoints, the API enables
  large-scale automation and integration with ITSM, IdPs, and SIEM tools.

---
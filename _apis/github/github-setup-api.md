---
aid: github:github-setup-api
name: GitHub Setup API
tags:
  - Configuration Check
  - Configurations
  - Setup
  - Status
  - Configure
  - Process
  - Maintenance
  - Disable
  - Enable
  - Mode
  - Settings
  - Sets
  - Authorized
  - Keys
  - SSH
  - Removes
  - Git
  - Hub
  - Licenses
  - Upgrade
baseURL: https://api.github.com/
humanURL: >-
  https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28
overlays:
  - url: overlays/github-setup-openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-setup-openapi-original.yml
    type: OpenAPI
description: Use the REST API to create and manage teams in your GitHub organization.

---
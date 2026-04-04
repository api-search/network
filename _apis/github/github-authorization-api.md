---
aid: github:github-auth-api
name: GitHub Authorization API
tags:
  - Authorization
  - Authentication
baseURL: https://api.github.com
humanURL: >-
  https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28
properties:
  - url: openapi/github-auth-api-openapi.yml
    type: OpenAPI
  - url: >-

      https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
    type: Documentation
description: >-
  The GitHub Authorization (OAuth Authorizations) API historically let you
  programmatically create, list, inspect, and revoke access tokens for a user or
  OAuth applicationsetting scopes, verifying token validity, rotating or
  deleting tokens, and generally managing what an app could do on a users
  behalf. It was commonly used with basic authentication (and 2FA) to mint
  personal access tokens and to manage OAuth app grants. For security reasons,
  these endpoints have been deprecated and disabled on GitHub.com; today, apps
  should use modern authorization flows (OAuth web or device flow) or GitHub
  Apps with finegrained permissions, and manage personal access tokens via the
  web UI or the current OAuth application endpoints for token verification and
  revocation.

---
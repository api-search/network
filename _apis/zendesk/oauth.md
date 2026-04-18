---
aid: zendesk:oauth
baseURL: https://{subdomain}.zendesk.com
description: The Zendesk OAuth API implements the OAuth 2.0 standard to let apps securely access Zendesk data on a users or accounts behalf without sharing passwords. Developers register an OAuth client in a Zendesk account, redirect users to Zendesk for signin and consent, and exchange the returned authorization code for access (and optionally refresh) tokens.
humanURL: https://developer.zendesk.com/api-reference/ticketing/oauth/oauth_tokens/
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Zendesk Oauth API
properties:
- type: Documentation
  url: https://developer.zendesk.com/api-reference/ticketing/oauth/oauth_tokens/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/openapi/oauth-openapi-original.yml
provider_name: Zendesk
provider_slug: zendesk
slug: oauth
tags:
- Authentication
- Authorization
- Oauth
---

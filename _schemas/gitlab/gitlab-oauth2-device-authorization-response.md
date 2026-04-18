---
description: DeviceAuthorizationResponse from GitLab API
layout: schema
name: DeviceAuthorizationResponse
properties_list:
- description: The device verification code used to poll for the access token.
  name: device_code
  type: string
- description: The end-user verification code to enter on the authorization page.
  name: user_code
  type: string
- description: The end-user verification URI on the authorization server.
  name: verification_uri
  type: string
- description: The verification URI that includes the user_code.
  name: verification_uri_complete
  type: string
- description: The lifetime in seconds of the device_code and user_code.
  name: expires_in
  type: integer
- description: Minimum number of seconds between polling requests.
  name: interval
  type: integer
provider_name: GitLab
provider_slug: gitlab
schema_file: json-schema/gitlab-oauth2-device-authorization-response-schema.json
slug: gitlab-oauth2-device-authorization-response
tags:
- Code
- Platform
- Software Development
- Source Control
title: DeviceAuthorizationResponse
---

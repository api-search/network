---
aid: microsoft-graph:microsoft-graph-certificate-based-authorization-configuration
name: Microsoft Graph Certificate Based Authorization Configuration
tags:
  - Authorization
  - Configuration
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/certificatebasedauthconfiguration-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graphs certificate-based authentication configuration is a
  tenant-level setting in Microsoft Entra ID that you manage via the Graph API
  to enable and govern sign-in using X.509 client certificates. It lets
  administrators specify which certificate authorities are trusted, how
  certificate chains and revocation are validated, and how fields in a presented
  certificate (such as Subject or Subject Alternative Name/UPN) are mapped to a
  specific user account. During sign-in, Entra ID uses this configuration to
  validate the certificate, bind it to the right identity, and issue tokens for
  Microsoft Graph and other apps, allowing organizations to automate and control
  certificate-based sign-in without relying on AD FS.

---
---
aid: microsoft-graph:microsoft-graph-invitations
name: Microsoft Graph Invitations
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/invitations-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Invitations is a Microsoft Graph API feature that lets apps
  programmatically invite external (B2B) users into a Microsoft Entra ID tenant.
  By calling POST /invitations, it creates a guest user and can send an email
  invitation with a redemption link, or you can suppress the email and use the
  returned inviteRedeemUrl to deliver the link yourself. You can set the invited
  users email and display name, choose a post-acceptance redirect URL (often a
  deep link to your app), and customize the invitation message and recipients.
  When the invite is redeemed, the user is added as a guest (userType=Guest) and
  can be assigned to apps, groups, and resources per your policies. This enables
  automated, governed cross-tenant collaboration and streamlined external user
  onboarding.

---
---
aid: microsoft-graph:microsoft-graph-group-lifecycle-policies
name: Microsoft Graph Group Lifecycle Policies
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/grouplifecyclepolicies-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Group Lifecycle Policies let administrators govern the
  lifespan of Microsoft 365 groups by setting an expiration period, scoping the
  policy to all or selected groups, and automating renewal and cleanup. When a
  group nears expiration, owners (and optional alternate email recipients)
  receive reminder emails; if not renewed, the group is softdeleted and can be
  restored within a grace period. Policies can be created and managed
  programmatically via Microsoft Graphspecifying the lifetime in days, choosing
  which groups are managed, adding or removing groups from a policy, and
  triggering renewalshelping organizations reduce stale groups, maintain
  directory hygiene, and enforce consistent governance at scale.

---
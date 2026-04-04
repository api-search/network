---
aid: microsoft-graph:microsoft-graph-schema-extensions
name: Microsoft Graph Schema Extensions
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/schemaextensions-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph schema extensions let you add your own strongly typed fields
  to Microsoft 365 resourcessuch as users, groups, messages, events, devices,
  and moreso your applications data can live alongside Microsoft data and be
  accessed through the same Graph APIs. You register a schema extension (with a
  unique ID tied to your verified domain), define property names and types, and
  then write values to individual resource instances; those values are returned
  with the resource and can be selected or, on supported entities, filtered in
  queries. Unlike untyped open extensions, schema extensions are discoverable
  and enforce types, making them easier to share across apps and tenants and to
  manage through a defined lifecycle. This approach reduces the need for a
  separate store or custom service, keeps data consistent and secured under
  Microsoft Graphs auth model, and enables richer, domain-specific solutions
  built on top of Microsoft 365.

---
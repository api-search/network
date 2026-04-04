---
aid: microsoft-graph:microsoft-graph-group-setting-templates
name: Microsoft Graph Group Setting Templates
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/groupsettingtemplates-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Group Setting Templates are read-only blueprints that define
  the configurable options you can apply to Microsoft 365 groups (and some other
  directory objects). Administrators use these templates (for example, those
  covering naming policies, guest access, classifications, welcome emails, and
  usage-guidelines URLs) to create directory settings that enforce
  organizationwide or pergroup behaviorsuch as who can create groups, whether
  guests are allowed, or what classifications are available. The templates
  provide the schema and validation for each setting, ensuring consistent and
  predictable configuration through the Graph API and the Entra admin portal. In
  practice, you query the available templates (GET /groupSettingTemplates), then
  instantiate one as a directory setting with your values (POST /groupSettings)
  and apply it at the tenant or group scope; the templates themselves remain
  immutable.

---
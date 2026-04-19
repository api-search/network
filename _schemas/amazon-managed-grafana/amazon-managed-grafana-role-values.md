---
description: This structure defines which groups defined in the SAML assertion attribute are to be mapped to the Grafana <code>Admin</code> and <code>Editor</code> roles in the workspace. SAML authenticated users not part of <code>Admin</code> or <code>Editor</code> role groups have <code>Viewer</code> permission over the workspace.
layout: schema
name: RoleValues
properties_list:
- description: ''
  name: admin
  type: object
- description: ''
  name: editor
  type: object
provider_name: Amazon Managed Grafana
provider_slug: amazon-managed-grafana
schema_file: json-schema/amazon-managed-grafana-role-values-schema.json
slug: amazon-managed-grafana-role-values
tags:
- AWS
- Dashboards
- Monitoring
- Observability
- Visualization
title: RoleValues
---

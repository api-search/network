---
description: These are IAM Identity Center identity store attributes that you can configure for use in attributes-based access control (ABAC). You can create permissions policies that determine who can access your AWS resources based upon the configured attribute values. When you enable ABAC and specify <code>AccessControlAttributes</code>, IAM Identity Center passes the attribute values of the authenticated user into IAM for use in policy evaluation.
layout: schema
name: AccessControlAttribute
properties_list:
- description: ''
  name: Key
  type: object
- description: ''
  name: Value
  type: object
provider_name: Amazon IAM Identity Center
provider_slug: amazon-iam-identity-center
schema_file: json-schema/sso-admin-access-control-attribute-schema.json
slug: sso-admin-access-control-attribute
tags:
- Access Control
- Authentication
- AWS
- Identity Management
- Single Sign-On
title: AccessControlAttribute
---

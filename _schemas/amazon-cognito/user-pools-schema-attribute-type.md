---
description: <p>A list of the user attributes and their properties in your user pool. The attribute schema contains standard attributes, custom attributes with a <code>custom:</code> prefix, and developer attributes with a <code>dev:</code> prefix. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html">User pool attributes</a>.</p> <p>Developer-only attributes are a legacy feature of user pools, are read-only to all app clients. You can create and update developer-only attributes only with IAM-authenticated API operations. Use app client read/write permissions instead.</p>
layout: schema
name: SchemaAttributeType
properties_list:
- description: ''
  name: Name
  type: object
- description: ''
  name: AttributeDataType
  type: object
- description: ''
  name: DeveloperOnlyAttribute
  type: object
- description: ''
  name: Mutable
  type: object
- description: ''
  name: Required
  type: object
- description: ''
  name: NumberAttributeConstraints
  type: object
- description: ''
  name: StringAttributeConstraints
  type: object
provider_name: Amazon Cognito
provider_slug: amazon-cognito
schema_file: json-schema/user-pools-schema-attribute-type-schema.json
slug: user-pools-schema-attribute-type
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
title: SchemaAttributeType
---

---
description: <p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker.</p> <important><p>Does not apply to RabbitMQ brokers.</p></important>
layout: schema
name: LdapServerMetadataInput
properties_list:
- description: ''
  name: Hosts
  type: object
- description: ''
  name: RoleBase
  type: object
- description: ''
  name: RoleName
  type: object
- description: ''
  name: RoleSearchMatching
  type: object
- description: ''
  name: RoleSearchSubtree
  type: object
- description: ''
  name: ServiceAccountPassword
  type: object
- description: ''
  name: ServiceAccountUsername
  type: object
- description: ''
  name: UserBase
  type: object
- description: ''
  name: UserRoleName
  type: object
- description: ''
  name: UserSearchMatching
  type: object
- description: ''
  name: UserSearchSubtree
  type: object
provider_name: Amazon MQ
provider_slug: amazon-mq
schema_file: json-schema/mq-api-ldap-server-metadata-input-schema.json
slug: mq-api-ldap-server-metadata-input
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: LdapServerMetadataInput
---

---
class_count: 13
classes:
- attr_based_filter
- check_group_membership
- check_user_in_particular_group
- domain_param
- fetch_all_users_attrs
- group_filter
- list_all_groups_in_domain
- list_all_users_in_domain
- list_groups_user_belongs_to
- list_specific_groups
- list_specific_users
- list_users_in_particular_group
- pagination_params
context_file: json-ld/palo-alto-cloud-identity-engine-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cloud-identity-engine-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Cloud Identity Engine Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Cloud Identity Engine Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: attrName
  type: string
- container: ''
  name: attrValue
  type: string
- container: set
  name: attrs
  type: string
- container: ''
  name: domain
  type: string
- container: ''
  name: filter
  type: reference
- container: ''
  name: level
  type: string
- container: ''
  name: match
  type: string
- container: ''
  name: name
  type: reference
- container: ''
  name: pageNum
  type: integer
- container: ''
  name: pageSz
  type: integer
- container: ''
  name: type
  type: string
- container: ''
  name: useNormalizedAttrs
  type: string
property_count: 12
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-cloud-identity-engine-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---

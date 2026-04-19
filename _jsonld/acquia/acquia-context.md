---
class_count: 17
classes:
- Error
- Ux Message
- User
- Application
- Subscription
- Ide
- Environment
- Agreement
- Ssh Key
- Organization
- Team
- Invite
- Notification
- url
- name
- email
- description
context_file: json-ld/acquia-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/json-ld/acquia-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Acquia from Acquia.
layout: jsonld
name: Acquia Context
namespaces:
- prefix: acquia
  uri: https://acquia.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: error
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: uuid
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: body
  type: string
- container: ''
  name: filters
  type: string
- container: ''
  name: flags
  type: string
- container: ''
  name: weight
  type: integer
- container: ''
  name: start_at
  type: dateTime
- container: ''
  name: expire_at
  type: dateTime
- container: ''
  name: _links
  type: string
- container: ''
  name: first_name
  type: string
- container: ''
  name: last_name
  type: string
- container: ''
  name: last_login_at
  type: dateTime
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: mail
  type: string
- container: ''
  name: phone
  type: string
- container: ''
  name: job_title
  type: string
- container: ''
  name: job_function
  type: string
- container: ''
  name: company
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: timezone
  type: string
- container: ''
  name: picture_url
  type: reference
- container: set
  name: features
  type: string
- container: ''
  name: metadata
  type: string
- container: ''
  name: hosting
  type: string
- container: ''
  name: subscription
  type: string
- container: ''
  name: organization
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: _embedded
  type: string
- container: ''
  name: product
  type: string
- container: ''
  name: applications_total
  type: integer
- container: ''
  name: applications_used
  type: integer
- container: ''
  name: label
  type: string
- container: ''
  name: application
  type: string
- container: set
  name: domains
  type: string
- container: ''
  name: active_domain
  type: string
- container: ''
  name: default_domain
  type: string
- container: ''
  name: image_url
  type: reference
- container: ''
  name: ssh_url
  type: string
- container: set
  name: ips
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: balancer
  type: string
- container: ''
  name: platform
  type: string
- container: ''
  name: size
  type: string
- container: ''
  name: vcs
  type: string
- container: ''
  name: configuration
  type: string
- container: ''
  name: artifact
  type: string
- container: ''
  name: document_uuid
  type: string
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: actioned_by
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: public_key
  type: string
- container: ''
  name: fingerprint
  type: string
- container: ''
  name: subscriptions_total
  type: integer
- container: ''
  name: admins_total
  type: integer
- container: ''
  name: users_total
  type: integer
- container: ''
  name: teams_total
  type: integer
- container: ''
  name: roles_total
  type: integer
- container: ''
  name: owner
  type: string
- container: ''
  name: token
  type: string
- container: ''
  name: author
  type: string
- container: ''
  name: team
  type: string
- container: set
  name: applications
  type: string
- container: set
  name: roles
  type: string
- container: ''
  name: progress
  type: integer
- container: ''
  name: user
  type: string
- container: ''
  name: started_at
  type: dateTime
- container: ''
  name: completed_at
  type: dateTime
- container: ''
  name: labels
  type: string
property_count: 73
provider_name: Acquia
provider_slug: acquia
slug: acquia-context
tags:
- Content
- Experience
- JSON-LD
- Linked Data
- Semantic Web
---

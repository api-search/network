---
class_count: 4
classes:
- Repository
- Pullrequest
- Pipeline
- Commit
context_file: json-ld/bitbucket-cloud-rest-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/json-ld/bitbucket-cloud-rest-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Bitbucket Cloud Rest Api from Bitbucket.
layout: jsonld
name: Bitbucket Cloud Rest Api Context
namespaces:
- prefix: bb
  uri: https://api.bitbucket.org/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: uuid
  type: string
- container: ''
  name: fullName
  type: string
- container: ''
  name: slug
  type: string
- container: ''
  name: isPrivate
  type: boolean
- container: ''
  name: createdOn
  type: dateTime
- container: ''
  name: updatedOn
  type: dateTime
- container: ''
  name: completedOn
  type: dateTime
- container: ''
  name: size
  type: integer
- container: ''
  name: language
  type: string
- container: ''
  name: hash
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: buildNumber
  type: integer
- container: ''
  name: commentCount
  type: integer
- container: ''
  name: taskCount
  type: integer
- container: ''
  name: forkPolicy
  type: string
- container: ''
  name: scm
  type: string
- container: set
  name: reviewers
  type: reference
- container: set
  name: participants
  type: reference
- container: set
  name: parents
  type: reference
property_count: 23
provider_name: Bitbucket
provider_slug: bitbucket
slug: bitbucket-cloud-rest-api-context
tags:
- Atlassian
- CI/CD
- Code Collaboration
- Code Review
- DevOps
- Git
- Pull Requests
- Repository Hosting
- Version Control
- JSON-LD
- Linked Data
- Semantic Web
---

---
description: The details of a repository stored in CodeArtifact. A CodeArtifact repository contains a set of package versions, each of which maps to a set of assets. Repositories are polyglot—a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <code>npm</code> CLI, the Maven CLI (<code>mvn</code>), and <code>pip</code>. You can create up to 100 repositories per Amazon Web Services account.
layout: schema
name: RepositoryDescription
properties_list:
- description: ''
  name: name
  type: object
- description: ''
  name: administratorAccount
  type: object
- description: ''
  name: domainName
  type: object
- description: ''
  name: domainOwner
  type: object
- description: ''
  name: arn
  type: object
- description: ''
  name: description
  type: object
- description: ''
  name: upstreams
  type: object
- description: ''
  name: externalConnections
  type: object
- description: ''
  name: createdTime
  type: object
provider_name: Amazon CodeArtifact
provider_slug: amazon-codeartifact
schema_file: json-schema/codeartifact-repository-description-schema.json
slug: codeartifact-repository-description
tags:
- Amazon
- AWS
- Artifact Repository
- Package Management
- DevOps
- Software Supply Chain
- npm
- Maven
- PyPI
- NuGet
title: RepositoryDescription
---

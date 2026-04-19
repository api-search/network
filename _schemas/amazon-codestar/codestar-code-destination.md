---
description: The repository to be created in AWS CodeStar. Valid values are AWS CodeCommit or GitHub. After AWS CodeStar provisions the new repository, the source code files provided with the project request are placed in the repository.
layout: schema
name: CodeDestination
properties_list:
- description: ''
  name: codeCommit
  type: object
- description: ''
  name: gitHub
  type: object
provider_name: Amazon CodeStar
provider_slug: amazon-codestar
schema_file: json-schema/codestar-code-destination-schema.json
slug: codestar-code-destination
tags:
- AWS
- Developer Tools
- DevOps
- Project Management
- Team Collaboration
title: CodeDestination
---

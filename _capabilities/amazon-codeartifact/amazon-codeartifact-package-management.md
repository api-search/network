---
consumed_apis:
- codeartifact
description: Unified workflow for DevOps teams to manage artifact repositories, publish packages, control access, and govern software supply chains using Amazon CodeArtifact.
layout: capability
name: Amazon CodeArtifact Package Management
operations: []
personas: []
provider_name: Amazon CodeArtifact
provider_slug: amazon-codeartifact
search_terms:
- Software Developer
- devops
- publish a new package version to a repository
- list packages
- manage codeartifact repositories
- list package versions
- copy package versions
- delete specific package versions from a repository
- get repository endpoint
- list repositories in a domain
- delete package versions
- get details about a codeartifact repository
- create a new codeartifact domain
- pypi
- create domain
- governance and security of external package dependencies and internal packages.
- copy package versions between repositories in the same domain
- list versions of a package in a repository
- publish package version
- list all codeartifact domains in the account
- list repositories
- describe package
- get authorization tokens for package managers
- software supply chain
- DevOps Engineer
- publishes and consumes packages from codeartifact repositories.
- describe domain
- sets up domains, repositories, and governance controls across teams.
- create repository
- get authorization token
- aws
- maven
- amazon
- managing software package lifecycle including publishing, versioning, and deprecation.
- get details about a package in a repository
- Platform Engineer
- associate external connection
- generate a temporary authorization token for accessing codeartifact repositories
- package management
- get details about a codeartifact domain
- storage and retrieval of software artifacts and their metadata.
- npm
- manage packages and package versions
- create a new codeartifact repository within a domain
- list packages in a repository
- connect a repository to a public package registry like npmjs or pypi
- get the package-format-specific endpoint url for a repository
- manages repository infrastructure, external connections, and domain policies.
- nuget
- describe repository
- manage codeartifact domains
- artifact repository
- unified workflow for managing artifact repositories, packages, and software supply chain governance.
- list domains
slug: amazon-codeartifact-package-management
tags:
- Amazon
- AWS
- Package Management
- DevOps
- Artifact Repository
- Software Supply Chain
tools:
- description: List all CodeArtifact domains in the account
  hints:
    openWorld: true
    readOnly: true
  name: list-domains
- description: List repositories in a domain
  hints:
    openWorld: true
    readOnly: true
  name: list-repositories
- description: List packages in a repository
  hints:
    openWorld: true
    readOnly: true
  name: list-packages
- description: List versions of a package in a repository
  hints:
    openWorld: true
    readOnly: true
  name: list-package-versions
- description: Get details about a CodeArtifact domain
  hints:
    openWorld: true
    readOnly: true
  name: describe-domain
- description: Get details about a CodeArtifact repository
  hints:
    openWorld: true
    readOnly: true
  name: describe-repository
- description: Get details about a package in a repository
  hints:
    openWorld: true
    readOnly: true
  name: describe-package
- description: Generate a temporary authorization token for accessing CodeArtifact repositories
  hints:
    openWorld: false
    readOnly: false
  name: get-authorization-token
- description: Create a new CodeArtifact domain
  hints:
    openWorld: false
    readOnly: false
  name: create-domain
- description: Create a new CodeArtifact repository within a domain
  hints:
    openWorld: false
    readOnly: false
  name: create-repository
- description: Copy package versions between repositories in the same domain
  hints:
    openWorld: false
    readOnly: false
  name: copy-package-versions
- description: Connect a repository to a public package registry like npmjs or PyPI
  hints:
    openWorld: false
    readOnly: false
  name: associate-external-connection
- description: Publish a new package version to a repository
  hints:
    destructive: false
    openWorld: false
    readOnly: false
  name: publish-package-version
- description: Delete specific package versions from a repository
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-package-versions
- description: Get the package-format-specific endpoint URL for a repository
  hints:
    openWorld: true
    readOnly: true
  name: get-repository-endpoint
---

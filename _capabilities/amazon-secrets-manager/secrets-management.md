---
consumed_apis:
- amazon-secrets-manager
description: Unified capability for managing application secrets lifecycle including creation, retrieval, rotation, and deletion. Used by DevOps Engineers and Application Developers.
layout: capability
name: Amazon Secrets Manager Secrets Management
operations:
- description: List all managed secrets
  method: GET
  name: list-secrets
  path: /v1/secrets
- description: Create and store a new secret
  method: POST
  name: create-secret
  path: /v1/secrets
- description: Get metadata for a secret
  method: GET
  name: describe-secret
  path: /v1/secrets/{name}
- description: Retrieve the current value of a secret
  method: GET
  name: get-secret-value
  path: /v1/secrets/{name}/value
- description: Update the value of a secret
  method: PUT
  name: put-secret-value
  path: /v1/secrets/{name}/value
- description: Trigger rotation for a secret
  method: POST
  name: rotate-secret
  path: /v1/secrets/{name}/rotate
- description: Generate a cryptographically secure random password
  method: POST
  name: get-random-password
  path: /v1/passwords/random
personas: []
provider_name: Amazon Secrets Manager
provider_slug: amazon-secrets-manager
search_terms:
- trigger rotation for a secret
- Application Developer
- update the value of a secret
- put secret value
- cancel scheduled deletion and restore a secret
- engineers who manage application infrastructure and configure secrets rotation and access policies
- create a new secret in amazon secrets manager
- create secret
- configuration
- list all managed secrets
- devops
- random password generation
- developers who integrate applications with secrets manager to retrieve credentials at runtime
- list secrets
- get metadata and configuration details of a secret
- retrieve the current value of a secret
- delete secret
- secret rotation management
- security
- amazon secrets manager
- end-to-end secrets lifecycle management including creation, retrieval, rotation, and deletion
- rotation
- update the value stored in a secret
- DevOps Engineer
- restore secret
- create and store a new secret
- individual secret management
- secret value retrieval and update
- schedule a secret for deletion
- rotate secret
- get metadata for a secret
- aws
- secure storage and access control for sensitive credentials and configuration
- get random password
- lifecycle management of secrets including rotation, versioning, and audit
- list all secrets stored in amazon secrets manager
- generate a cryptographically secure random password
- secret lifecycle management
- retrieve the plaintext value of a secret
- credentials
- describe secret
- get secret value
- secrets
- trigger automatic rotation for a secret
slug: secrets-management
tags:
- Amazon Secrets Manager
- Security
- Secrets
- DevOps
- Credentials
tools:
- description: List all secrets stored in Amazon Secrets Manager
  hints:
    idempotent: true
    readOnly: true
  name: list-secrets
- description: Create a new secret in Amazon Secrets Manager
  hints:
    idempotent: false
    readOnly: false
  name: create-secret
- description: Retrieve the plaintext value of a secret
  hints:
    idempotent: true
    readOnly: true
  name: get-secret-value
- description: Update the value stored in a secret
  hints:
    idempotent: false
    readOnly: false
  name: put-secret-value
- description: Get metadata and configuration details of a secret
  hints:
    idempotent: true
    readOnly: true
  name: describe-secret
- description: Trigger automatic rotation for a secret
  hints:
    idempotent: false
    readOnly: false
  name: rotate-secret
- description: Schedule a secret for deletion
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-secret
- description: Cancel scheduled deletion and restore a secret
  hints:
    idempotent: true
    readOnly: false
  name: restore-secret
- description: Generate a cryptographically secure random password
  hints:
    idempotent: false
    readOnly: false
  name: get-random-password
---

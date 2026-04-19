---
consumed_apis:
- cognito-user-pools
- cognito-identity-pools
description: Workflow capability for managing user authentication, identity federation, and access control using Amazon Cognito User Pools and Identity Pools. Used by application developers and platform administrators to implement secure sign-up, sign-in, and AWS resource access for web and mobile apps.
layout: capability
name: Amazon Cognito User Authentication
operations:
- description: List all user pools.
  method: GET
  name: list-user-pools
  path: /v1/user-pools
- description: Create a new user pool.
  method: POST
  name: create-user-pool
  path: /v1/user-pools
- description: List users in a user pool.
  method: GET
  name: list-users
  path: /v1/user-pools/{user_pool_id}/users
- description: Create a new user in the pool.
  method: POST
  name: create-user
  path: /v1/user-pools/{user_pool_id}/users
- description: List all identity pools.
  method: GET
  name: list-identity-pools
  path: /v1/identity-pools
- description: Start the authentication flow.
  method: POST
  name: initiate-auth
  path: /v1/auth/initiate
- description: Get temporary AWS credentials for a federated identity.
  method: POST
  name: get-credentials
  path: /v1/credentials
personas: []
provider_name: Amazon Cognito
provider_slug: amazon-cognito
search_terms:
- list all user pools.
- create a new user in the pool.
- describe user pool
- list all identity pools.
- Application Developer
- list users in a cognito user pool.
- oauth
- list users in a user pool.
- create a new amazon cognito user pool.
- federated identity
- get credentials
- authentication
- manage users within a user pool.
- get temporary aws credentials for a federated cognito identity.
- get temporary aws credentials for a federated identity.
- get details of a specific cognito identity pool.
- user management
- create user
- manages user pools, groups, and identity pool configurations.
- create identity pool
- describe identity pool
- Platform Administrator
- delete user
- create user pool
- list users
- identity
- aws
- initiate auth
- create a new user pool.
- start the authentication flow.
- amazon
- get temporary aws credentials.
- get user
- create a new user in a cognito user pool.
- list all cognito identity pools.
- get configuration details of a specific cognito user pool.
- delete a user from a cognito user pool.
- initiate authentication flows.
- manage cognito identity pools.
- get details of a specific user in a cognito user pool.
- end-to-end user authentication using user pools and identity pools.
- create a new cognito identity pool for federated identity management.
- list user pools
- integrates cognito authentication into web and mobile applications.
- list identity pools
- initiate an authentication flow in cognito.
- list all amazon cognito user pools in the account.
- manage cognito user pools.
slug: user-authentication
tags:
- Amazon
- AWS
- Authentication
- Identity
- User Management
- OAuth
- Federated Identity
tools:
- description: List all Amazon Cognito user pools in the account.
  hints:
    readOnly: true
  name: list-user-pools
- description: Get configuration details of a specific Cognito user pool.
  hints:
    readOnly: true
  name: describe-user-pool
- description: Create a new Amazon Cognito user pool.
  hints:
    destructive: false
    readOnly: false
  name: create-user-pool
- description: List users in a Cognito user pool.
  hints:
    readOnly: true
  name: list-users
- description: Get details of a specific user in a Cognito user pool.
  hints:
    readOnly: true
  name: get-user
- description: Create a new user in a Cognito user pool.
  hints:
    destructive: false
    readOnly: false
  name: create-user
- description: Delete a user from a Cognito user pool.
  hints:
    destructive: true
    readOnly: false
  name: delete-user
- description: Initiate an authentication flow in Cognito.
  hints:
    destructive: false
    readOnly: false
  name: initiate-auth
- description: List all Cognito identity pools.
  hints:
    readOnly: true
  name: list-identity-pools
- description: Get details of a specific Cognito identity pool.
  hints:
    readOnly: true
  name: describe-identity-pool
- description: Get temporary AWS credentials for a federated Cognito identity.
  hints:
    readOnly: true
  name: get-credentials
- description: Create a new Cognito identity pool for federated identity management.
  hints:
    destructive: false
    readOnly: false
  name: create-identity-pool
---

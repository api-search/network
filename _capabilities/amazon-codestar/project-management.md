---
consumed_apis:
- codestar
description: Workflow capability for managing AWS CodeStar development projects, team collaboration, and user profiles. Used by development team leads and platform administrators to set up CI/CD toolchains and manage project access.
layout: capability
name: Amazon CodeStar Project Management
operations:
- description: List all AWS CodeStar projects.
  method: GET
  name: list-projects
  path: /v1/projects
- description: Create a new AWS CodeStar project.
  method: POST
  name: create-project
  path: /v1/projects
- description: Describe a specific CodeStar project.
  method: GET
  name: describe-project
  path: /v1/projects/{project_id}
- description: Delete a CodeStar project.
  method: DELETE
  name: delete-project
  path: /v1/projects/{project_id}
- description: List all team members in a project.
  method: GET
  name: list-team-members
  path: /v1/projects/{project_id}/team-members
- description: Add an IAM user to the project team.
  method: POST
  name: associate-team-member
  path: /v1/projects/{project_id}/team-members
- description: List tags for a CodeStar project.
  method: GET
  name: list-tags
  path: /v1/projects/{project_id}/tags
- description: List all user profiles.
  method: GET
  name: list-user-profiles
  path: /v1/user-profiles
- description: Create a user profile.
  method: POST
  name: create-user-profile
  path: /v1/user-profiles
personas: []
provider_name: Amazon CodeStar
provider_slug: amazon-codestar
search_terms:
- devops
- update attributes of an aws codestar project.
- describe project
- manage team members for a project.
- manage codestar user profiles.
- create a new aws codestar project.
- create user profile
- tag project
- Development Team Lead
- list tags for a codestar project.
- manages user profiles and project-level access controls.
- remove an iam user from an aws codestar project team.
- list all aws codestar user profiles.
- list resources
- list all aws codestar projects in the account.
- update project
- delete project
- create a user profile.
- list team members
- creates and manages codestar projects and team membership.
- list projects
- get and update individual codestar project.
- list all team members in a project.
- list tags
- project management
- list user profiles
- delete an aws codestar project and its resources.
- disassociate team member
- add tags to an aws codestar project for organization.
- Platform Administrator
- list aws resources associated with a codestar project.
- delete a codestar project.
- create a new aws codestar development project with ci/cd toolchain.
- create and manage codestar projects, team members, and user profiles.
- list all aws codestar projects.
- developer tools
- aws
- amazon
- manage codestar projects.
- list all user profiles.
- manage tags on a project.
- create a user profile for aws codestar.
- add an iam user to the project team.
- add an iam user to an aws codestar project team with a role.
- create project
- associate team member
- team collaboration
- describe a specific codestar project.
- get details of a specific aws codestar project.
- list all team members and their roles in a codestar project.
slug: project-management
tags:
- Amazon
- AWS
- Developer Tools
- DevOps
- Project Management
- Team Collaboration
tools:
- description: List all AWS CodeStar projects in the account.
  hints:
    openWorld: false
    readOnly: true
  name: list-projects
- description: Create a new AWS CodeStar development project with CI/CD toolchain.
  hints:
    destructive: false
    readOnly: false
  name: create-project
- description: Get details of a specific AWS CodeStar project.
  hints:
    openWorld: false
    readOnly: true
  name: describe-project
- description: Update attributes of an AWS CodeStar project.
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: update-project
- description: Delete an AWS CodeStar project and its resources.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-project
- description: List AWS resources associated with a CodeStar project.
  hints:
    readOnly: true
  name: list-resources
- description: List all team members and their roles in a CodeStar project.
  hints:
    readOnly: true
  name: list-team-members
- description: Add an IAM user to an AWS CodeStar project team with a role.
  hints:
    destructive: false
    readOnly: false
  name: associate-team-member
- description: Remove an IAM user from an AWS CodeStar project team.
  hints:
    destructive: true
    readOnly: false
  name: disassociate-team-member
- description: List all AWS CodeStar user profiles.
  hints:
    readOnly: true
  name: list-user-profiles
- description: Create a user profile for AWS CodeStar.
  hints:
    destructive: false
    readOnly: false
  name: create-user-profile
- description: Add tags to an AWS CodeStar project for organization.
  hints:
    destructive: false
    readOnly: false
  name: tag-project
---

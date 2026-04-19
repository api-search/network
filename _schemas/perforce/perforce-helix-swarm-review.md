---
description: A code review in Helix Swarm, representing a set of changes under review with participants, votes, and state.
layout: schema
name: Review
properties_list:
- description: The unique review identifier.
  name: id
  type: integer
- description: The username of the review author.
  name: author
  type: string
- description: List of changelist IDs associated with the review.
  name: changes
  type: array
- description: List of committed changelist IDs.
  name: commits
  type: array
- description: Status of commit operations.
  name: commitStatus
  type: array
- description: Unix timestamp when the review was created.
  name: created
  type: integer
- description: Deploy configuration details.
  name: deployDetails
  type: array
- description: The current deploy status.
  name: deployStatus
  type: string
- description: The review description.
  name: description
  type: string
- description: Reviewer groups assigned to the review.
  name: groups
  type: array
- description: Map of participant usernames to their participation details including votes and required status.
  name: participants
  type: object
- description: Whether the review has a pending changelist.
  name: pending
  type: boolean
- description: Map of project IDs to affected branch names.
  name: projects
  type: object
- description: Map of roles to lists of usernames.
  name: roles
  type: object
- description: The current state of the review.
  name: state
  type: string
- description: A display-friendly label for the current state.
  name: stateLabel
  type: string
- description: Details of test runs.
  name: testDetails
  type: array
- description: The overall test status.
  name: testStatus
  type: string
- description: The review type (default or personal).
  name: type
  type: string
- description: Unix timestamp when the review was last updated.
  name: updated
  type: integer
- description: ISO 8601 formatted date when the review was last updated.
  name: updateDate
  type: string
- description: List of review version objects.
  name: versions
  type: array
provider_name: Perforce
provider_slug: perforce
schema_file: json-schema/perforce-helix-swarm-review-schema.json
slug: perforce-helix-swarm-review
tags: []
title: Review
---

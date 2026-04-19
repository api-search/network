---
description: A code review in Perforce Helix Swarm (P4 Code Review), representing a set of changelists under review with participants, votes, state transitions, and test/deploy status.
layout: schema
name: Perforce Helix Swarm Review
properties_list:
- description: The unique review identifier assigned by Swarm.
  name: id
  type: integer
- description: The Perforce username of the review author.
  name: author
  type: string
- description: List of changelist IDs associated with this review.
  name: changes
  type: array
- description: List of committed changelist IDs resulting from this review.
  name: commits
  type: array
- description: Status details for commit operations on this review.
  name: commitStatus
  type: array
- description: Unix timestamp when the review was created.
  name: created
  type: integer
- description: Details of deployment operations triggered by this review.
  name: deployDetails
  type: array
- description: The current deployment status for the review.
  name: deployStatus
  type:
  - string
  - 'null'
- description: The review description, typically derived from the changelist description.
  name: description
  type: string
- description: Reviewer groups assigned to the review.
  name: groups
  type: array
- description: Map of participant usernames to their participation details, including votes and required status.
  name: participants
  type: object
- description: Whether the review is associated with a pending (shelved) changelist.
  name: pending
  type: boolean
- description: Map of Swarm project IDs to the branch names affected by this review.
  name: projects
  type: object
- description: Map of role names to lists of usernames holding those roles.
  name: roles
  type: object
- description: The current state of the review in its lifecycle.
  name: state
  type: string
- description: A human-readable label for the current state.
  name: stateLabel
  type: string
- description: Details of test runs executed against this review.
  name: testDetails
  type: array
- description: The overall test status for the review, such as pass or fail.
  name: testStatus
  type:
  - string
  - 'null'
- description: The review type. Default reviews are standard; personal reviews are private to the author.
  name: type
  type: string
- description: Unix timestamp when the review was last updated.
  name: updated
  type: integer
- description: ISO 8601 formatted date-time when the review was last updated.
  name: updateDate
  type: string
- description: History of review versions, each representing an update to the shelved changelist.
  name: versions
  type: array
provider_name: Perforce
provider_slug: perforce
schema_file: json-schema/perforce-review-schema.json
slug: perforce-review
tags: []
title: Perforce Helix Swarm Review
---

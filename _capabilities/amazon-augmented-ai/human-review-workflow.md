---
consumed_apis: []
description: Workflow capability for managing human-in-the-loop review of machine learning predictions using Amazon Augmented AI.
layout: capability
name: Human Review Workflow
operations:
- description: Start a human review loop
  method: POST
  name: start-human-loop
  path: /v1/human-loops
- description: List human review loops
  method: GET
  name: list-human-loops
  path: /v1/human-loops
personas: []
provider_name: Amazon Augmented AI
provider_slug: amazon-augmented-ai
search_terms:
- describe human loop
- human review loop management
- stop human loop
- list human review loops
- human in the loop
- list human loops
- aws
- start a human review loop
- machine learning
- amazon augmented ai
- list all human review loops to track review progress and status.
- initiate human review of an ml prediction by starting a new human loop.
- get the current status and output of a specific human review loop.
- start human loop
- ai review
- stop an in-progress human review loop when review is no longer needed.
slug: human-review-workflow
tags:
- Amazon Augmented AI
- Human In The Loop
- Machine Learning
- AI Review
- AWS
tools:
- description: Initiate human review of an ML prediction by starting a new human loop.
  hints:
    openWorld: false
    readOnly: false
  name: start-human-loop
- description: List all human review loops to track review progress and status.
  hints:
    openWorld: true
    readOnly: true
  name: list-human-loops
- description: Get the current status and output of a specific human review loop.
  hints:
    openWorld: true
    readOnly: true
  name: describe-human-loop
- description: Stop an in-progress human review loop when review is no longer needed.
  hints:
    openWorld: false
    readOnly: false
  name: stop-human-loop
---

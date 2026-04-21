---
consumed_apis:
- kinesis
description: Unified workflow capability for Amazon Kinesis combining resource management and operations.
layout: capability
name: Amazon Kinesis Workflow
operations: []
personas: []
provider_name: Amazon Kinesis
provider_slug: amazon-kinesis
search_terms:
- streams describe stream summary
- amazon kinesis
- analytics
- real-time
- data processing
- big data
- Administrator
- streams create stream
- streaming
- Developer
- creates a kinesis data stream.
- manages resources and configurations
- integrates api into applications
- aws
- lists your kinesis data streams.
- unified workflow for amazon kinesis resource management
- workflow
- streams list streams
- provides a summarized description of the specified kinesis data stream.
slug: amazon-kinesis-workflow
tags:
- Amazon Kinesis
- AWS
- Workflow
tools:
- description: Creates a Kinesis data stream.
  hints:
    idempotent: false
    readOnly: false
  name: streams-create-stream
- description: Lists your Kinesis data streams.
  hints:
    idempotent: true
    readOnly: true
  name: streams-list-streams
- description: Provides a summarized description of the specified Kinesis data stream.
  hints:
    idempotent: true
    readOnly: true
  name: streams-describe-stream-summary
---

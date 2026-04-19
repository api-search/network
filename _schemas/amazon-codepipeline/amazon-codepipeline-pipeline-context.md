---
description: <p>Represents information about a pipeline to a job worker.</p> <note> <p>PipelineContext contains <code>pipelineArn</code> and <code>pipelineExecutionId</code> for custom action jobs. The <code>pipelineArn</code> and <code>pipelineExecutionId</code> fields are not populated for ThirdParty action jobs.</p> </note>
layout: schema
name: PipelineContext
properties_list:
- description: ''
  name: pipelineName
  type: object
- description: ''
  name: stage
  type: object
- description: ''
  name: action
  type: object
- description: ''
  name: pipelineArn
  type: object
- description: ''
  name: pipelineExecutionId
  type: object
provider_name: Amazon CodePipeline
provider_slug: amazon-codepipeline
schema_file: json-schema/amazon-codepipeline-pipeline-context-schema.json
slug: amazon-codepipeline-pipeline-context
tags:
- Amazon
- AWS
- CI/CD
- Continuous Delivery
- DevOps
- Pipeline
- Release Automation
title: PipelineContext
---

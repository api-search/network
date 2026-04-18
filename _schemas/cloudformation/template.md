---
description: Represents the structure of an AWS CloudFormation template. A template is a JSON or YAML formatted text file that describes the AWS infrastructure and resources to provision. Templates can be used to create and update CloudFormation stacks.
layout: schema
name: AWS CloudFormation Template
properties_list:
- description: The AWS CloudFormation template version that the template conforms to. The only valid value is 2010-09-09.
  name: AWSTemplateFormatVersion
  type: string
- description: A text string that describes the template.
  name: Description
  type: string
- description: Objects that provide additional information about the template. Can include template-specific metadata such as AWS::CloudFormation::Interface.
  name: Metadata
  type: object
- description: Values to pass to your template at runtime when you create or update a stack. Parameters enable you to customize stack creation.
  name: Parameters
  type: object
- description: Validates a parameter or a combination of parameters passed to a template during stack creation or update.
  name: Rules
  type: object
- description: A mapping of keys and associated values that you can use to specify conditional parameter values. Similar to a lookup table.
  name: Mappings
  type: object
- description: Conditions that control whether certain resources are created or whether certain resource properties are assigned a value during stack creation or update.
  name: Conditions
  type: object
- description: For serverless applications, specifies the version of the AWS SAM to use. You can also use AWS::Include transforms to work with template snippets stored separately.
  name: Transform
  type: object
- description: Specifies the stack resources and their properties, such as an Amazon EC2 instance or an Amazon S3 bucket. You must declare each resource separately.
  name: Resources
  type: object
- description: Describes the values that are returned whenever you view your stack's properties. Output values can be used for cross-stack references.
  name: Outputs
  type: object
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/template.json
slug: template
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: AWS CloudFormation Template
---

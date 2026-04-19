---
description: <p>This API allows you to create a conformance pack template with an Amazon Web Services Systems Manager document (SSM document). To deploy a conformance pack using an SSM document, first create an SSM document with conformance pack content, and then provide the <code>DocumentName</code> in the <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html">PutConformancePack API</a>. You can also provide the <code>DocumentVersion</code>.</p> <p>The <code>TemplateSSMDocumentDetails</code> object contains the name of the SSM document and the version of the SSM document.</p>
layout: schema
name: TemplateSSMDocumentDetails
properties_list:
- description: ''
  name: DocumentName
  type: object
- description: ''
  name: DocumentVersion
  type: object
provider_name: Amazon Config
provider_slug: amazon-config
schema_file: json-schema/config-template-ssm-document-details-schema.json
slug: config-template-ssm-document-details
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
title: TemplateSSMDocumentDetails
---

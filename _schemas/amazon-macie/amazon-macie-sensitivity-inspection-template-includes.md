---
description: Specifies the allow lists, custom data identifiers, and managed data identifiers to include (use) when performing automated sensitive data discovery for an Amazon Macie account. The configuration must specify at least one custom data identifier or managed data identifier. For information about the managed data identifiers that Amazon Macie currently provides, see <a href="https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html">Using managed data identifiers</a> in the <i>Amazon Macie User Guide</i>.
layout: schema
name: SensitivityInspectionTemplateIncludes
properties_list:
- description: ''
  name: allowListIds
  type: object
- description: ''
  name: customDataIdentifierIds
  type: object
- description: ''
  name: managedDataIdentifierIds
  type: object
provider_name: Amazon Macie
provider_slug: amazon-macie
schema_file: json-schema/amazon-macie-sensitivity-inspection-template-includes-schema.json
slug: amazon-macie-sensitivity-inspection-template-includes
tags:
- AWS
- Data Security
- Sensitive Data
- Privacy
- Compliance
- Machine Learning
- S3
title: SensitivityInspectionTemplateIncludes
---

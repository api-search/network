---
description: The style of a section, influencing the layout of the section's content.
layout: schema
name: SectionStyle
properties_list:
- description: The section's columns properties. If empty, the section contains one column with the default properties.
  name: columnProperties
  type: array
- description: The style of column separators.
  name: columnSeparatorStyle
  type: string
- description: The content direction of this section.
  name: contentDirection
  type: string
- description: The type of section.
  name: sectionType
  type: string
- description: ''
  name: defaultHeaderId
  type: string
- description: ''
  name: defaultFooterId
  type: string
- description: ''
  name: evenPageHeaderId
  type: string
- description: ''
  name: evenPageFooterId
  type: string
- description: ''
  name: firstPageHeaderId
  type: string
- description: ''
  name: firstPageFooterId
  type: string
- description: ''
  name: useFirstPageHeaderFooter
  type: boolean
- description: ''
  name: pageNumberStart
  type: integer
- description: ''
  name: flipPageOrientation
  type: boolean
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-section-style-schema.json
slug: google-docs-v1-section-style
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: SectionStyle
---

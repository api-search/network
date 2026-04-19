---
description: Represents the styling that can be applied to text. Inherited text styles are represented as unset fields. A text style's parent depends on where the text style is defined.
layout: schema
name: TextStyle
properties_list:
- description: Whether the text is bold.
  name: bold
  type: boolean
- description: Whether the text is italicized.
  name: italic
  type: boolean
- description: Whether the text is underlined.
  name: underline
  type: boolean
- description: Whether the text is struck through.
  name: strikethrough
  type: boolean
- description: Whether the text is in small capital letters.
  name: smallCaps
  type: boolean
- description: The text's vertical offset from its normal position.
  name: baselineOffset
  type: string
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-text-style-schema.json
slug: google-docs-v1-text-style
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: TextStyle
---

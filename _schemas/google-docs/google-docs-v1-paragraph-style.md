---
description: Styles that apply to a whole paragraph. Inherited paragraph styles are represented as unset fields.
layout: schema
name: ParagraphStyle
properties_list:
- description: The heading ID of the paragraph.
  name: headingId
  type: string
- description: The named style type of the paragraph.
  name: namedStyleType
  type: string
- description: The text alignment for this paragraph.
  name: alignment
  type: string
- description: The amount of space between lines as a percentage of normal, where normal is represented as 100.0.
  name: lineSpacing
  type: number
- description: The text direction of this paragraph.
  name: direction
  type: string
- description: The spacing mode for the paragraph.
  name: spacingMode
  type: string
- description: A list of the tab stops for this paragraph, sorted in ascending order of the tab stop offset.
  name: tabStops
  type: array
- description: Whether all lines of the paragraph should be laid out on the same page or column if possible.
  name: keepLinesTogether
  type: boolean
- description: Whether at least a part of this paragraph should be laid out on the same page or column as the next paragraph if possible.
  name: keepWithNext
  type: boolean
- description: Whether to avoid widows and orphans for the paragraph.
  name: avoidWidowAndOrphan
  type: boolean
- description: Whether the current paragraph should always start at the beginning of a page.
  name: pageBreakBefore
  type: boolean
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-paragraph-style-schema.json
slug: google-docs-v1-paragraph-style
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: ParagraphStyle
---

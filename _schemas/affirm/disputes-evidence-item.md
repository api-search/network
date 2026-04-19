---
description: A single piece of evidence associated with a dispute.
layout: schema
name: EvidenceItem
properties_list:
- description: Unique identifier for this evidence item.
  name: id
  type: string
- description: Type of evidence (file, text, tracking).
  name: type
  type: string
- description: For text evidence, the content of the explanation. For file evidence, the file identifier.
  name: content
  type: string
- description: Timestamp when this evidence was submitted, in RFC 3339 format.
  name: submitted_at
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/disputes-evidence-item-schema.json
slug: disputes-evidence-item
tags: []
title: EvidenceItem
---

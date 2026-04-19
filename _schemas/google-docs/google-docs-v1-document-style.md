---
description: The style of the document, influencing the look of the document and any defaults for new content.
layout: schema
name: DocumentStyle
properties_list:
- description: The ID of the default header.
  name: defaultHeaderId
  type: string
- description: The ID of the default footer.
  name: defaultFooterId
  type: string
- description: The ID of the header used for even pages.
  name: evenPageHeaderId
  type: string
- description: The ID of the footer used for even pages.
  name: evenPageFooterId
  type: string
- description: The ID of the header used for the first page.
  name: firstPageHeaderId
  type: string
- description: The ID of the footer used for the first page.
  name: firstPageFooterId
  type: string
- description: Whether to use the first page header/footer IDs for the first page of the document.
  name: useFirstPageHeaderFooter
  type: boolean
- description: Whether to use the even page header/footer IDs for even pages.
  name: useEvenPageHeaderFooter
  type: boolean
- description: The page number from which to start counting the number of pages.
  name: pageNumberStart
  type: integer
- description: Whether to use custom header/footer margins.
  name: useCustomHeaderFooterMargins
  type: boolean
- description: Whether to flip the orientation of the page to landscape, which effectively swaps the width and height of the page size.
  name: flipPageOrientation
  type: boolean
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-document-style-schema.json
slug: google-docs-v1-document-style
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: DocumentStyle
---

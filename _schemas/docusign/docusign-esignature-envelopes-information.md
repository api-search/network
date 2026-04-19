---
description: Contains information about the envelopes returned by a list request, including the result set and pagination details.
layout: schema
name: EnvelopesInformation
properties_list:
- description: The list of envelopes matching the query.
  name: envelopes
  type: array
- description: The number of results in the current set.
  name: resultSetSize
  type: string
- description: The total number of envelopes matching the query.
  name: totalSetSize
  type: string
- description: The starting index position of the current result set.
  name: startPosition
  type: string
- description: The ending index position of the current result set.
  name: endPosition
  type: string
- description: URI for the next page of results.
  name: nextUri
  type: string
- description: URI for the previous page of results.
  name: previousUri
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-envelopes-information-schema.json
slug: docusign-esignature-envelopes-information
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: EnvelopesInformation
---

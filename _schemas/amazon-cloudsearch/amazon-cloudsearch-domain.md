---
description: Represents an Amazon CloudSearch domain with its configuration, index fields, and service endpoints.
layout: schema
name: Amazon CloudSearch Domain
properties_list:
- description: An internally generated unique identifier for a domain.
  name: domainId
  type: string
- description: A string that represents the name of a domain.
  name: domainName
  type: string
- description: The Amazon Resource Name (ARN) of the search domain.
  name: arn
  type: string
- description: True if the search domain is created.
  name: created
  type: boolean
- description: True if the search domain has been deleted.
  name: deleted
  type: boolean
- description: True if processing is being done to activate the current domain configuration.
  name: processing
  type: boolean
- description: True if IndexDocuments needs to be called to activate the current domain configuration.
  name: requiresIndexDocuments
  type: boolean
- description: The number of search instances that are available to process search requests.
  name: searchInstanceCount
  type: integer
- description: The instance type that is being used to process search requests.
  name: searchInstanceType
  type: string
- description: The service endpoint for updating documents in a search domain.
  name: docService
  type: object
- description: The service endpoint for requesting search results from a search domain.
  name: searchService
  type: object
provider_name: Amazon CloudSearch
provider_slug: amazon-cloudsearch
schema_file: json-schema/amazon-cloudsearch-domain-schema.json
slug: amazon-cloudsearch-domain
tags:
- AWS
- CloudSearch
- Search
- Full-Text Search
- Managed
title: Amazon CloudSearch Domain
---

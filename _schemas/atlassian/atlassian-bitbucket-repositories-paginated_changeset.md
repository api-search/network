---
description: A paginated list of commits.
layout: schema
name: paginated_changeset
properties_list:
- description: Total number of objects in the response. This is an optional element that is not provided in all responses, as it can be expensive to compute.
  name: size
  type: integer
- description: Page number of the current results. This is an optional element that is not provided in all responses.
  name: page
  type: integer
- description: Current number of objects on the existing page. The default value is 10 with 100 being the maximum allowed value. Individual APIs may enforce different values.
  name: pagelen
  type: integer
- description: Link to the next page if it exists. The last page of a collection does not have this value. Use this link to navigate the result set and refrain from constructing your own URLs.
  name: next
  type: string
- description: Link to previous page if it exists. A collections first page does not have this value. This is an optional element that is not provided in all responses. Some result sets strictly support forward navi
  name: previous
  type: string
- description: ''
  name: values
  type: array
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-bitbucket-repositories-paginated_changeset-schema.json
slug: atlassian-bitbucket-repositories-paginated_changeset
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: paginated_changeset
---

---
description: Response message for listing projects.
layout: schema
name: ListProjectsResponse
properties_list:
- description: The list of projects under the specified parent.
  name: projects
  type: array
- description: Pagination token to retrieve the next page of results. Empty if there are no more results.
  name: nextPageToken
  type: string
provider_name: Google Cloud Platform
provider_slug: google-cloud-platform
schema_file: json-schema/cloud-resource-manager-list-projects-response-schema.json
slug: cloud-resource-manager-list-projects-response
tags:
- API Management
- Cloud Computing
- Infrastructure
- Platform as a Service
title: ListProjectsResponse
---

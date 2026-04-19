---
description: Information about the application.
layout: schema
name: Application
properties_list:
- description: The application Amazon Resource Name (ARN).
  name: applicationId
  type: string
- description: The name of the application.
  name: name
  type: string
- description: The name of the author publishing the app.
  name: author
  type: string
- description: The description of the application.
  name: description
  type: string
- description: The date and time this resource was created.
  name: creationTime
  type: string
- description: A URL with more information about the application.
  name: homePageUrl
  type: string
- description: Labels to improve discovery of apps in search results.
  name: labels
  type: array
- description: A link to a license file of the app.
  name: licenseUrl
  type: string
- description: A link to the readme file in Markdown language.
  name: readmeUrl
  type: string
- description: A valid identifier from https://spdx.org/licenses/.
  name: spdxLicenseId
  type: string
- description: ''
  name: version
  type: object
provider_name: Amazon Serverless Application Repository
provider_slug: amazon-serverless-application-repository
schema_file: json-schema/amazon-serverless-application-repository-application-schema.json
slug: amazon-serverless-application-repository-application
tags:
- Application Repository
- AWS
- Lambda
- SAM
- Serverless
title: Application
---

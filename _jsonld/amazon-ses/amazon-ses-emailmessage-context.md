---
class_count: 1
classes:
- EmailMessage
context_file: json-ld/amazon-ses-emailmessage-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-ses/refs/heads/main/json-ld/amazon-ses-emailmessage-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Ses Emailmessage from Amazon SES.
layout: jsonld
name: Amazon Ses Emailmessage Context
namespaces:
- prefix: aws
  uri: https://aws.amazon.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Simple
  type: string
- container: ''
  name: Subject
  type: string
- container: ''
  name: Data
  type: string
- container: ''
  name: Charset
  type: string
- container: ''
  name: Body
  type: string
- container: ''
  name: Text
  type: string
- container: ''
  name: Html
  type: string
- container: ''
  name: Raw
  type: string
- container: ''
  name: Template
  type: string
- container: ''
  name: TemplateName
  type: string
- container: ''
  name: TemplateArn
  type: string
- container: ''
  name: TemplateData
  type: string
- container: ''
  name: FromEmailAddress
  type: string
- container: ''
  name: Destination
  type: string
- container: set
  name: ToAddresses
  type: string
- container: set
  name: CcAddresses
  type: string
- container: set
  name: BccAddresses
  type: string
- container: set
  name: ReplyToAddresses
  type: string
- container: ''
  name: ConfigurationSetName
  type: string
property_count: 19
provider_name: Amazon SES
provider_slug: amazon-ses
slug: amazon-ses-emailmessage-context
tags:
- AWS
- Email
- Email Deliverability
- Email Service
- Marketing Email
- Notifications
- SMTP
- Transactional Email
- JSON-LD
- Linked Data
- Semantic Web
---

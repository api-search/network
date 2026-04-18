---
class_count: 19
classes:
- BlogPost
- BlogPostInput
- BlogPostCollection
- ScheduleRequest
- CloneRequest
- PushLiveRequest
- ResetDraftRequest
- RestorePreviousVersionRequest
- VersionHistory
- BatchInputItem
- BatchInput
- BatchResponse
- DetachFromLanguageGroupRequest
- SetLanguagePrimaryRequest
- AttachToLanguageGroupRequest
- CreateLanguageVariationRequest
- Paging
- PagingNext
- PagingPrevious
context_file: json-ld/hubspot-blog-posts-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-blog-posts-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Blog Posts Api from HubSpot.
layout: jsonld
name: Hubspot Blog Posts Api Context
namespaces:
- prefix: hubspot
  uri: https://developers.hubspot.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: slug
  type: string
- container: ''
  name: htmlTitle
  type: string
- container: ''
  name: postBody
  type: string
- container: ''
  name: postSummary
  type: string
- container: ''
  name: blogAuthorId
  type: string
- container: ''
  name: authorName
  type: string
- container: ''
  name: contentGroupId
  type: string
- container: ''
  name: campaign
  type: string
- container: ''
  name: categoryId
  type: integer
- container: ''
  name: state
  type: string
- container: ''
  name: currentState
  type: string
- container: ''
  name: publishDate
  type: dateTime
- container: ''
  name: created
  type: dateTime
- container: ''
  name: updated
  type: dateTime
- container: ''
  name: archivedAt
  type: dateTime
- container: ''
  name: currentlyPublished
  type: boolean
- container: ''
  name: domain
  type: string
- container: ''
  name: featuredImage
  type: string
- container: ''
  name: featuredImageAltText
  type: string
- container: ''
  name: metaDescription
  type: string
- container: ''
  name: headHtml
  type: string
- container: ''
  name: footerHtml
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: translatedFromId
  type: string
- container: set
  name: tagIds
  type: integer
- container: ''
  name: useFeaturedImage
  type: boolean
- container: ''
  name: url
  type: ''
- container: ''
  name: abStatus
  type: string
- container: ''
  name: abTestId
  type: string
- container: ''
  name: folderId
  type: string
- container: ''
  name: total
  type: integer
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: revisionId
  type: string
- container: ''
  name: object
  type: reference
- container: ''
  name: user
  type: reference
- container: ''
  name: timestamp
  type: dateTime
- container: set
  name: inputs
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: requestedAt
  type: dateTime
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: links
  type: reference
- container: ''
  name: primaryId
  type: string
- container: ''
  name: primaryLanguage
  type: string
- container: ''
  name: next
  type: reference
- container: ''
  name: prev
  type: reference
- container: ''
  name: after
  type: string
- container: ''
  name: link
  type: string
- container: ''
  name: before
  type: string
property_count: 52
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-blog-posts-api-context
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
- JSON-LD
- Linked Data
- Semantic Web
---

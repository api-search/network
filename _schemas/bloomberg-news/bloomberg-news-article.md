---
description: Schema for a Bloomberg news article delivered through the Bloomberg News API or BLPAPI //blp/mktdata and //blp/refdata news services, representing breaking news, analysis, and multimedia content covering global markets and business.
layout: schema
name: Bloomberg News Article
properties_list:
- description: Unique Bloomberg identifier for the news story
  name: storyId
  type: string
- description: Primary headline of the news article
  name: headline
  type: string
- description: Secondary headline or deck providing additional context
  name: subHeadline
  type:
  - string
  - 'null'
- description: Brief summary or abstract of the article content
  name: summary
  type: string
- description: Full text body of the news article
  name: body
  type: string
- description: ISO 8601 timestamp when the article was first published
  name: publishedAt
  type: string
- description: ISO 8601 timestamp when the article was last updated
  name: updatedAt
  type:
  - string
  - 'null'
- description: Canonical URL of the article on Bloomberg.com
  name: url
  type: string
- description: List of authors who contributed to the article
  name: authors
  type: array
- description: Originating news source or wire service
  name: source
  type: string
- description: ISO 639-1 language code of the article
  name: language
  type: string
- description: Total word count of the article body
  name: wordCount
  type: integer
- description: Classification of the article type
  name: articleType
  type: string
- description: News urgency classification reflecting the BLPAPI NEWS_STORY_URGENCY field
  name: urgency
  type: string
- description: Bloomberg topic codes and categories associated with the article
  name: topics
  type: array
- description: Securities mentioned in or related to the article, referenced by Bloomberg identifiers
  name: securities
  type: array
- description: Geographic regions relevant to the article
  name: regions
  type: array
- description: Industry sectors relevant to the article content
  name: sectors
  type: array
- description: Free-form tags or keywords associated with the article
  name: tags
  type: array
- description: Associated multimedia content such as images, videos, or charts
  name: media
  type: array
- description: References to related Bloomberg news stories
  name: relatedStories
  type: array
- description: Copyright notice for the article content
  name: copyright
  type: string
provider_name: Bloomberg News
provider_slug: bloomberg-news
schema_file: json-schema/bloomberg-news-article-schema.json
slug: bloomberg-news-article
tags:
- Analytics
- Business Intelligence
- Financial Services
- Market Data
- News
title: Bloomberg News Article
---

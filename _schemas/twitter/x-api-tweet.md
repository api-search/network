---
description: Tweet schema from X API v2
layout: schema
name: Tweet
properties_list:
- description: Specifies the type of attachments (if any) present in this Tweet.
  name: attachments
  type: object
- description: Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: author_id
  type: string
- description: The unique identifier of this Community.
  name: community_id
  type: string
- description: ''
  name: context_annotations
  type: array
- description: Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: conversation_id
  type: string
- description: Creation time of the Tweet.
  name: created_at
  type: string
- description: Represent a boundary range (start and end zero-based indices) for the portion of text that is displayed for a post. `start` must be smaller than `end`. The start index is inclusive, the end index is e
  name: display_text_range
  type: array
- description: ''
  name: edit_controls
  type: object
- description: A list of Tweet Ids in this Tweet chain.
  name: edit_history_tweet_ids
  type: array
- description: ''
  name: entities
  type: object
- description: The location tagged on the Tweet, if the user provided one.
  name: geo
  type: object
- description: Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: id
  type: string
- description: Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: in_reply_to_user_id
  type: string
- description: Language of the Tweet, if detected by X. Returned as a BCP47 language tag.
  name: lang
  type: string
- description: Nonpublic engagement metrics for the Tweet at the time of the request.
  name: non_public_metrics
  type: object
- description: The full-content of the Tweet, including text beyond 280 characters.
  name: note_tweet
  type: object
- description: Organic nonpublic engagement metrics for the Tweet at the time of the request.
  name: organic_metrics
  type: object
- description: Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.
  name: possibly_sensitive
  type: boolean
- description: Promoted nonpublic engagement metrics for the Tweet at the time of the request.
  name: promoted_metrics
  type: object
- description: Engagement metrics for the Tweet at the time of the request.
  name: public_metrics
  type: object
- description: A list of Posts this Tweet refers to. For example, if the parent Tweet is a Retweet, a Quoted Tweet or a Reply, it will include the related Tweet referenced to by its parent.
  name: referenced_tweets
  type: array
- description: Shows who can reply a Tweet. Fields returned are everyone, mentioned_users, subscribers, verified and following.
  name: reply_settings
  type: string
- description: The scopes for this tweet
  name: scopes
  type: object
- description: This is deprecated.
  name: source
  type: string
- description: ''
  name: suggested_source_links
  type: array
- description: Suggested source links and the number of requests that included each link.
  name: suggested_source_links_with_counts
  type: object
- description: The content of the Tweet.
  name: text
  type: string
- description: The X handle (screen name) of this user.
  name: username
  type: string
- description: Indicates withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).
  name: withheld
  type: object
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-tweet-schema.json
slug: x-api-tweet
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: Tweet
---

---
description: TweetCreateRequest schema from X API v2
layout: schema
name: TweetCreateRequest
properties_list:
- description: Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link.
  name: card_uri
  type: string
- description: The unique identifier of this Community.
  name: community_id
  type: string
- description: Link to take the conversation from the public timeline to a private Direct Message.
  name: direct_message_deep_link
  type: string
- description: Options for editing an existing Post. When provided, this request will edit the specified Post instead of creating a new one.
  name: edit_options
  type: object
- description: Exclusive Tweet for super followers.
  name: for_super_followers_only
  type: boolean
- description: Place ID being attached to the Tweet for geo location.
  name: geo
  type: object
- description: Whether this Post contains AI-generated media. When true, the Post will be labeled accordingly.
  name: made_with_ai
  type: boolean
- description: Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.
  name: media
  type: object
- description: Nullcasted (promoted-only) Posts do not appear in the public timeline and are not served to followers.
  name: nullcast
  type: boolean
- description: Whether this Post is a paid partnership. When true, the Post will be labeled as a paid promotion.
  name: paid_partnership
  type: boolean
- description: Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.
  name: poll
  type: object
- description: Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: quote_tweet_id
  type: string
- description: Tweet information of the Tweet being replied to.
  name: reply
  type: object
- description: Settings to indicate who can reply to the Tweet.
  name: reply_settings
  type: string
- description: Share community post with followers too.
  name: share_with_followers
  type: boolean
- description: The content of the Tweet.
  name: text
  type: string
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-tweet-create-request-schema.json
slug: x-api-tweet-create-request
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: TweetCreateRequest
---

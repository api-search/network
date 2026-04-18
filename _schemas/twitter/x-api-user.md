---
description: The X User object.
layout: schema
name: User
properties_list:
- description: Metadata about a user's affiliation.
  name: affiliation
  type: object
- description: Returns detailed information about the relationship between two users.
  name: connection_status
  type: array
- description: Creation time of this User.
  name: created_at
  type: string
- description: The text of this User's profile description (also known as bio), if the User provided one.
  name: description
  type: string
- description: A list of metadata found in the User's profile description.
  name: entities
  type: object
- description: Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: id
  type: string
- description: The location specified in the User's profile, if the User provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with
  name: location
  type: string
- description: Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: most_recent_tweet_id
  type: string
- description: The friendly name of this User, as shown on their profile.
  name: name
  type: string
- description: Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  name: pinned_tweet_id
  type: string
- description: The URL to the profile banner for this User.
  name: profile_banner_url
  type: string
- description: The URL to the profile image for this User.
  name: profile_image_url
  type: string
- description: Indicates if this User has chosen to protect their Posts (in other words, if this User's Posts are private).
  name: protected
  type: boolean
- description: A list of metrics for this User.
  name: public_metrics
  type: object
- description: Indicates if you can send a DM to this User
  name: receives_your_dm
  type: boolean
- description: 'The X Blue subscription type of the user, eg: Basic, Premium, PremiumPlus or None.'
  name: subscription_type
  type: string
- description: The URL specified in the User's profile.
  name: url
  type: string
- description: The X handle (screen name) of this user.
  name: username
  type: string
- description: Indicate if this User is a verified X User.
  name: verified
  type: boolean
- description: 'The X Blue verified type of the user, eg: blue, government, business or none.'
  name: verified_type
  type: string
- description: Indicates withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).
  name: withheld
  type: object
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-user-schema.json
slug: x-api-user
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: User
---

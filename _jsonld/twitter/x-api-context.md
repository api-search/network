---
class_count: 23
classes:
- ActivityStreamingResponse
- ActivitySubscription
- ComplianceJob
- CreateDmConversationRequest
- DmEvent
- Error
- Expansions
- FilteredStreamingTweetResponse
- Get2TweetsSearchRecentResponse
- Get2UsersIdResponse
- List
- ListCreateRequest
- Media
- Place
- Poll
- Problem
- Space
- Tweet
- TweetCreateRequest
- TweetCreateResponse
- TweetDeleteResponse
- User
- UsersFollowingCreateRequest
context_file: json-ld/x-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/json-ld/x-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for X Api from X (Twitter).
layout: jsonld
name: X Api Context
namespaces:
- prefix: x
  uri: https://docs.x.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: affiliation
  type: reference
- container: ''
  name: attachments
  type: reference
- container: ''
  name: authorId
  type: string
- container: ''
  name: cardUri
  type: string
- container: set
  name: cashtags
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: communityId
  type: string
- container: set
  name: connectionStatus
  type: string
- container: set
  name: containedWithin
  type: string
- container: set
  name: contextAnnotations
  type: string
- container: ''
  name: conversationId
  type: string
- container: ''
  name: conversationType
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: creatorId
  type: string
- container: ''
  name: data
  type: reference
- container: ''
  name: description
  type: string
- container: ''
  name: detail
  type: string
- container: ''
  name: directMessageDeepLink
  type: string
- container: set
  name: displayTextRange
  type: string
- container: ''
  name: dmConversationId
  type: string
- container: ''
  name: downloadExpiresAt
  type: dateTime
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: durationMinutes
  type: string
- container: ''
  name: editControls
  type: reference
- container: set
  name: editHistoryTweetIds
  type: string
- container: ''
  name: editOptions
  type: reference
- container: ''
  name: endDatetime
  type: dateTime
- container: ''
  name: endedAt
  type: dateTime
- container: ''
  name: entities
  type: reference
- container: set
  name: errors
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: filter
  type: reference
- container: ''
  name: followerCount
  type: integer
- container: ''
  name: forSuperFollowersOnly
  type: boolean
- container: ''
  name: fullName
  type: string
- container: ''
  name: geo
  type: reference
- container: set
  name: hashtags
  type: string
- container: ''
  name: height
  type: integer
- container: set
  name: hostIds
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: inReplyToUserId
  type: string
- container: ''
  name: includes
  type: reference
- container: set
  name: invitedUserIds
  type: string
- container: ''
  name: isTicketed
  type: boolean
- container: ''
  name: lang
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: madeWithAi
  type: boolean
- container: set
  name: matchingRules
  type: string
- container: ''
  name: media
  type: reference
- container: ''
  name: mediaKey
  type: string
- container: ''
  name: memberCount
  type: integer
- container: set
  name: mentions
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: meta
  type: reference
- container: ''
  name: mostRecentTweetId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: nonPublicMetrics
  type: reference
- container: ''
  name: noteTweet
  type: reference
- container: ''
  name: nullcast
  type: boolean
- container: set
  name: options
  type: string
- container: ''
  name: organicMetrics
  type: reference
- container: ''
  name: ownerId
  type: string
- container: ''
  name: paidPartnership
  type: boolean
- container: ''
  name: participantCount
  type: string
- container: set
  name: participantIds
  type: string
- container: ''
  name: pinnedTweetId
  type: string
- container: ''
  name: placeType
  type: string
- container: set
  name: places
  type: string
- container: ''
  name: poll
  type: reference
- container: set
  name: polls
  type: string
- container: ''
  name: possiblySensitive
  type: boolean
- container: ''
  name: private
  type: boolean
- container: ''
  name: profileBannerUrl
  type: reference
- container: ''
  name: profileImageUrl
  type: reference
- container: ''
  name: promotedMetrics
  type: reference
- container: ''
  name: protected
  type: boolean
- container: ''
  name: publicMetrics
  type: reference
- container: ''
  name: quoteTweetId
  type: string
- container: ''
  name: receivesYourDm
  type: boolean
- container: set
  name: referencedTweets
  type: string
- container: ''
  name: reply
  type: reference
- container: ''
  name: replySettings
  type: string
- container: ''
  name: scheduledStart
  type: dateTime
- container: ''
  name: scopes
  type: reference
- container: ''
  name: senderId
  type: string
- container: ''
  name: shareWithFollowers
  type: boolean
- container: ''
  name: source
  type: string
- container: set
  name: speakerIds
  type: string
- container: ''
  name: startedAt
  type: dateTime
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: subscriberCount
  type: string
- container: ''
  name: subscriptionId
  type: string
- container: ''
  name: subscriptionType
  type: string
- container: set
  name: suggestedSourceLinks
  type: string
- container: ''
  name: suggestedSourceLinksWithCounts
  type: reference
- container: ''
  name: tag
  type: string
- container: ''
  name: targetUserId
  type: string
- container: ''
  name: text
  type: string
- container: ''
  name: title
  type: string
- container: set
  name: topics
  type: string
- container: set
  name: tweets
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: uploadExpiresAt
  type: dateTime
- container: ''
  name: uploadUrl
  type: reference
- container: ''
  name: url
  type: string
- container: set
  name: urls
  type: string
- container: ''
  name: username
  type: string
- container: set
  name: users
  type: string
- container: ''
  name: verified
  type: boolean
- container: ''
  name: verifiedType
  type: string
- container: ''
  name: votingStatus
  type: string
- container: ''
  name: webhookId
  type: string
- container: ''
  name: width
  type: integer
- container: ''
  name: withheld
  type: reference
property_count: 118
provider_name: X (Twitter)
provider_slug: twitter
slug: x-api-context
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
- JSON-LD
- Linked Data
- Semantic Web
---

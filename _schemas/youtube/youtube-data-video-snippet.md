---
description: Basic details about a video, including its title, description, tags, and category.
layout: schema
name: VideoSnippet
properties_list:
- description: The date and time when the video was published.
  name: publishedAt
  type: string
- description: The ID of the YouTube channel that published the video.
  name: channelId
  type: string
- description: The video title.
  name: title
  type: string
- description: The video description.
  name: description
  type: string
- description: A map of thumbnail images associated with the video.
  name: thumbnails
  type: object
- description: The channel title of the YouTube channel that published the video.
  name: channelTitle
  type: string
- description: A list of keyword tags associated with the video.
  name: tags
  type: array
- description: The YouTube video category associated with the video.
  name: categoryId
  type: string
- description: Indicates if the video is an upcoming/active live broadcast.
  name: liveBroadcastContent
  type: string
- description: The language of the text in the video resource's snippet.title and snippet.description properties.
  name: defaultLanguage
  type: string
- description: The snippet.localized object contains either a localized title and description for the video or the title in the default language.
  name: localized
  type: object
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-data-video-snippet-schema.json
slug: youtube-data-video-snippet
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: VideoSnippet
---

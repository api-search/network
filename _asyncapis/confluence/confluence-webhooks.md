---
channels:
- description: Channel for page_created events
  name: pageCreated
- description: Channel for page_updated events
  name: pageUpdated
- description: Channel for page_removed events
  name: pageRemoved
- description: Channel for page_trashed events
  name: pageTrashed
- description: Channel for page_restored events
  name: pageRestored
- description: Channel for space_created events
  name: spaceCreated
- description: Channel for space_updated events
  name: spaceUpdated
- description: Channel for space_removed events
  name: spaceRemoved
- description: Channel for comment_created events
  name: commentCreated
- description: Channel for comment_updated events
  name: commentUpdated
- description: Channel for comment_removed events
  name: commentRemoved
- description: Channel for attachment_created events
  name: attachmentCreated
- description: Channel for attachment_updated events
  name: attachmentUpdated
- description: Channel for attachment_removed events
  name: attachmentRemoved
- description: Channel for label_created events
  name: labelCreated
- description: Channel for label_removed events
  name: labelRemoved
- description: Channel for blog_created events
  name: blogCreated
- description: Channel for blog_updated events
  name: blogUpdated
- description: Channel for blog_removed events
  name: blogRemoved
description: Asynchronous event notifications from Confluence Cloud. Webhooks allow applications to receive real-time notifications when content, spaces, or other entities are created, updated, or deleted in Confluence. Webhooks can be registered through the Confluence UI, REST API, or via Atlassian Connect app descriptors.
layout: asyncapi
messages:
- description: ''
  name: PageCreated
  summary: A new page has been created in Confluence.
  title: Page Created
- description: ''
  name: PageUpdated
  summary: An existing page has been updated in Confluence.
  title: Page Updated
- description: ''
  name: PageRemoved
  summary: A page has been permanently removed from Confluence.
  title: Page Removed
- description: ''
  name: PageTrashed
  summary: A page has been moved to the trash in Confluence.
  title: Page Trashed
- description: ''
  name: PageRestored
  summary: A page has been restored from the trash in Confluence.
  title: Page Restored
- description: ''
  name: SpaceCreated
  summary: A new space has been created in Confluence.
  title: Space Created
- description: ''
  name: SpaceUpdated
  summary: A space has been updated in Confluence.
  title: Space Updated
- description: ''
  name: SpaceRemoved
  summary: A space has been removed from Confluence.
  title: Space Removed
- description: ''
  name: CommentCreated
  summary: A new comment has been added to a page or blog post.
  title: Comment Created
- description: ''
  name: CommentUpdated
  summary: A comment has been updated on a page or blog post.
  title: Comment Updated
- description: ''
  name: CommentRemoved
  summary: A comment has been removed from a page or blog post.
  title: Comment Removed
- description: ''
  name: AttachmentCreated
  summary: A file has been attached to a page or blog post.
  title: Attachment Created
- description: ''
  name: AttachmentUpdated
  summary: An attachment has been updated with a new version.
  title: Attachment Updated
- description: ''
  name: AttachmentRemoved
  summary: An attachment has been removed from content.
  title: Attachment Removed
- description: ''
  name: LabelCreated
  summary: A label has been added to content.
  title: Label Created
- description: ''
  name: LabelRemoved
  summary: A label has been removed from content.
  title: Label Removed
- description: ''
  name: BlogCreated
  summary: A new blog post has been created in Confluence.
  title: Blog Post Created
- description: ''
  name: BlogUpdated
  summary: A blog post has been updated in Confluence.
  title: Blog Post Updated
- description: ''
  name: BlogRemoved
  summary: A blog post has been removed from Confluence.
  title: Blog Post Removed
name: Confluence Cloud Webhooks
provider_name: Confluence
provider_slug: confluence
servers:
- description: Your application endpoint that receives webhook callbacks from Confluence Cloud. This URL is configured when registering the webhook.
  name: webhookReceiver
  protocol: https
  url: ''
slug: confluence-webhooks
spec_file: asyncapi/confluence-webhooks.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/confluence/refs/heads/main/asyncapi/confluence-webhooks.yml
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---

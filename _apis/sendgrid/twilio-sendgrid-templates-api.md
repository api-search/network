---
aid: sendgrid:twilio-sendgrid-templates-api
name: Twilio SendGrid Templates API
tags: []
properties:
  - url: openapi/tsg_templates_v3.yaml
    type: OpenAPI
description: >-
  The Twilio SendGrid Templates API allows you to create and manage email
  templates to be delivered with SendGrid's sending APIs. The templates you
  create will be available using a template ID that is passed to our sending
  APIs as part of the request. Each template may then have multiple versions
  associated with it. Whichever version is set as "active" at the time of the
  request will be sent to your recipients. This system allows you to update a
  single template's look and feel entirely without modifying your requests to
  our Mail Send API. For example, you could have a single template for welcome
  emails. That welcome template could then have a version for each season of the
  year that's themed appropriately and marked as active during the appropriate
  season. The template ID passed to our sending APIs never needs to change; you
  can just modify which version is active.


  This API provides operations to create and manage your templates as well as
  their versions.


  Each user can create up to 300 different templates. Templates are specific to
  accounts and Subusers. Templates created on a parent account will not be
  accessible from the Subusers' accounts.

---
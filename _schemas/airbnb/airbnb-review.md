---
description: ''
layout: schema
name: Review
properties_list:
- description: The unique identifier of the review.
  name: id
  type: string
- description: The identifier of the associated reservation.
  name: reservation_id
  type: string
- description: Whether the review was written by a guest or host.
  name: reviewer_type
  type: string
- description: The overall star rating from 1 to 5.
  name: rating
  type: integer
- description: The text content of the review.
  name: comments
  type: string
- description: Individual category ratings provided by the reviewer.
  name: category_ratings
  type: object
- description: The host response to the review, if provided.
  name: host_response
  type: string
- description: The timestamp when the review was submitted.
  name: created_at
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-review-schema.json
slug: airbnb-review
tags: []
title: Review
---

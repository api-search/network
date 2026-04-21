---
consumed_apis:
- pluralsight-content-catalog
- pluralsight-content-slug
- pluralsight-course-catalog
- pluralsight-public-course-catalog
- pluralsight-channels
- pluralsight-learning-paths
- pluralsight-programs
- pluralsight-labs
- pluralsight-tags
description: Unified workflow for L&D managers and content administrators to browse, organize, and manage learning content across courses, channels, learning paths, programs, labs, and tags. Combines content catalog, course catalog, public catalog, channels, learning paths, programs, labs, content slugs, and tags APIs.
layout: capability
name: Pluralsight Learning Content Management
operations:
- description: Query the general content catalog
  method: POST
  name: query-content-catalog
  path: /v1/content-catalog
- description: Resolve content slugs to internal identifiers
  method: POST
  name: query-content-slugs
  path: /v1/content-slugs
- description: Query the course catalog
  method: POST
  name: query-course-catalog
  path: /v1/course-catalog
- description: Retrieve the full public course catalog
  method: GET
  name: get-public-course-catalog
  path: /v1/public-courses
- description: Query and manage content channels
  method: POST
  name: manage-channels
  path: /v1/channels
- description: Query learning path catalog data
  method: POST
  name: query-learning-paths
  path: /v1/learning-paths
- description: Query the program catalog
  method: POST
  name: query-programs
  path: /v1/programs
- description: Query lab catalog and activity data
  method: POST
  name: query-labs
  path: /v1/labs
- description: Query content tags and taxonomy data
  method: POST
  name: query-tags
  path: /v1/tags
personas: []
provider_name: Pluralsight
provider_slug: pluralsight
search_terms:
- manage channels
- query the program catalog
- query and manage content channels
- course catalog with titles, descriptions, authors, and metadata
- skills assessment
- technology
- query content catalog
- query labs
- courses
- query content slugs
- engineering metrics
- content management
- query course catalog
- query content tags and taxonomy data used to categorize and organize learning content.
- resolve content slugs to internal identifiers
- query lab catalog and lab activity data for hands-on learning experiences and practical exercises.
- channels
- content channels for organizing and curating learning content
- query programs
- resolve content slugs to internal identifiers for content lookup by human-readable url slugs.
- structured learning programs and curriculum offerings
- structured sequences of courses organized around skills and roles
- retrieve the full public course catalog
- content tags and taxonomy for categorization
- query the program catalog including structured learning programs and curriculum offerings.
- query learning path catalog data
- general content catalog including videos, guides, and interactive courses
- query the general content catalog including videos, guides, interactive courses, and other content types.
- query course catalog information including titles, descriptions, authors, duration, release dates, and retirement status.
- query the general content catalog
- video training
- learning paths
- query content tags and taxonomy data
- pluralsight
- public course catalog accessible without authentication
- get public course catalog
- learning
- learning content
- query lab catalog and activity data
- hands-on labs and practical exercises
- retrieve the full public course catalog including course ids, titles, durations, release dates, and retirement status.
- query tags
- education
- query learning path catalog data including structured sequences of courses and content organized around specific skills and roles.
- query the course catalog
- query and manage content channels including creating channels, managing members and groups, organizing content sections, and tracking channel progress.
- query learning paths
slug: learning-content-management
tags:
- Pluralsight
- Learning Content
- Content Management
- Courses
- Channels
- Learning Paths
tools:
- description: Query the general content catalog including videos, guides, interactive courses, and other content types.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-content-catalog
- description: Resolve content slugs to internal identifiers for content lookup by human-readable URL slugs.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-content-slugs
- description: Query course catalog information including titles, descriptions, authors, duration, release dates, and retirement status.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-course-catalog
- description: Retrieve the full public course catalog including course IDs, titles, durations, release dates, and retirement status.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-public-course-catalog
- description: Query and manage content channels including creating channels, managing members and groups, organizing content sections, and tracking channel progress.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: manage-channels
- description: Query learning path catalog data including structured sequences of courses and content organized around specific skills and roles.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-learning-paths
- description: Query the program catalog including structured learning programs and curriculum offerings.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-programs
- description: Query lab catalog and lab activity data for hands-on learning experiences and practical exercises.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-labs
- description: Query content tags and taxonomy data used to categorize and organize learning content.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-tags
---

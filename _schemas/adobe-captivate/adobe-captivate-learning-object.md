---
description: Schema for a learning object in Adobe Learning Manager (formerly Captivate Prime). Learning objects include courses, learning programs, certifications, and job aids. The API follows JSON:API conventions, with resources represented by type, id, attributes, and relationships.
layout: schema
name: Adobe Learning Manager Learning Object
properties_list:
- description: ''
  name: data
  type: object
- description: Related resources included via the include query parameter, such as instances, skills, and authors
  name: included
  type: array
provider_name: Adobe Captivate
provider_slug: adobe-captivate
schema_file: json-schema/adobe-captivate-learning-object-schema.json
slug: adobe-captivate-learning-object
tags:
- Authoring
- Education
- eLearning
- LMS
- SCORM
- Training
- xAPI
title: Adobe Learning Manager Learning Object
---

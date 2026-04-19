---
consumed_apis:
- pluralsight-skills-assessment
- pluralsight-role-iq
- pluralsight-practice-exams
description: Unified workflow for L&D managers and developers to assess skills through Skill IQ, Role IQ, and practice exams. Combines skills assessment, role IQ, and practice exams APIs for comprehensive competency measurement.
layout: capability
name: Pluralsight Skills Assessment
operations:
- description: Query skill assessments and Skill IQ scores
  method: POST
  name: query-skills-assessment
  path: /v1/skills-assessments
- description: Query and manage Role IQ assessments and role associations
  method: POST
  name: manage-role-iq
  path: /v1/role-iq
- description: Query practice exam attempt data and results
  method: POST
  name: query-practice-exams
  path: /v1/practice-exams
personas: []
provider_name: Pluralsight
provider_slug: pluralsight
search_terms:
- pluralsight
- manage role iq
- query practice exam attempt data and results
- courses
- query skill assessments, skill iq scores, assessment catalogs, and competency measurements.
- learning
- query and manage role iq assessments, role catalogs, skill assignments, and user/team role associations.
- skill iq
- role iq assessments, role catalogs, and skill assignments
- role iq
- education
- practice exams
- practice exam attempts, scores, and results
- engineering metrics
- query skills assessment
- query practice exam attempt data including scores and results.
- query skill assessments and skill iq scores
- skills assessment
- skill iq assessments, scores, and competency measurements
- video training
- query practice exams
- technology
- query and manage role iq assessments and role associations
slug: skills-assessment
tags:
- Pluralsight
- Skills Assessment
- Skill IQ
- Role IQ
- Practice Exams
tools:
- description: Query skill assessments, Skill IQ scores, assessment catalogs, and competency measurements.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-skills-assessment
- description: Query and manage Role IQ assessments, role catalogs, skill assignments, and user/team role associations.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: manage-role-iq
- description: Query practice exam attempt data including scores and results.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-practice-exams
---

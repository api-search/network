---
aid: atlassian:atlassian-atlassianfindsourcesfortarget
name: Find Source Entities Related To A Target Entity
tags:
- Relation
humanURL: 
properties: []
description: >-
  Returns all target entities that have a particular relationship to the<br>source entity. Note, relationships are one way.<br><br>For example, the following method finds all users that have a 'collaborator'<br>relationship to a piece of content with an ID of '1234':<br>`GET /wiki/rest/api/relation/collaborator/to/content/1234/from/user`<br>Note, 'collaborator' is an example custom relationship type.<br><br>**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:<br>Permission to ...

---

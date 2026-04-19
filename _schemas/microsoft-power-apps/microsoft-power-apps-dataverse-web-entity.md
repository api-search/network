---
description: Metadata definition for a Dataverse table (entity). Provides information about the table structure including logical names, collection names, and configuration. Read-only entity type supporting only RetrieveMultiple operations.
layout: schema
name: Entity
properties_list:
- description: Unique identifier of the entity definition.
  name: entityid
  type: string
- description: Display name of the entity.
  name: name
  type: string
- description: Logical name of the entity, used in API requests and programmatic references.
  name: logicalname
  type: string
- description: Logical collection name of the entity.
  name: logicalcollectionname
  type: string
- description: Collection name of the entity.
  name: collectionname
  type: string
- description: Entity set name used in Web API URLs to reference this table.
  name: entitysetname
  type: string
- description: Physical database table name of the entity.
  name: physicalname
  type: string
- description: Base table name of the entity.
  name: basetablename
  type: string
- description: External name of the entity for virtual entities.
  name: externalname
  type: string
- description: External collection name of the entity.
  name: externalcollectionname
  type: string
- description: Address table name associated with the entity.
  name: addresstablename
  type: string
- description: Extension table name of the entity.
  name: extensiontablename
  type: string
- description: Report view name of the entity.
  name: reportviewname
  type: string
- description: Parent controlling attribute name of the entity.
  name: parentcontrollingattributename
  type: string
- description: Original localized display name of the entity.
  name: originallocalizedname
  type: string
- description: Original localized collection name of the entity.
  name: originallocalizedcollectionname
  type: string
- description: Whether this entity is an activity type.
  name: isactivity
  type: boolean
- description: Object type code of the entity.
  name: objecttypecode
  type: integer
- description: Component state of the entity. 0 = Published, 1 = Unpublished, 2 = Deleted, 3 = Deleted Unpublished.
  name: componentstate
  type: integer
- description: Unique identifier of the associated solution.
  name: solutionid
  type: string
- description: Record overwrite time for internal use.
  name: overwritetime
  type: string
- description: Version number of the entity definition record.
  name: versionnumber
  type: integer
provider_name: Microsoft Power Apps
provider_slug: microsoft-power-apps
schema_file: json-schema/microsoft-power-apps-dataverse-web-entity-schema.json
slug: microsoft-power-apps-dataverse-web-entity
tags:
- Business Applications
- Cloud
- Enterprise
- Low-Code
- Microsoft
- No-Code
- Power Platform
- SaaS
title: Entity
---

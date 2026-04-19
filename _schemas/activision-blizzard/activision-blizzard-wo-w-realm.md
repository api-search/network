---
description: A World of Warcraft realm
layout: schema
name: WoWRealm
properties_list:
- description: Realm ID
  name: id
  type: integer
- description: Realm name
  name: name
  type: string
- description: Realm slug
  name: slug
  type: string
- description: Region reference
  name: region
  type: object
- description: Realm category
  name: category
  type: string
- description: Realm locale
  name: locale
  type: string
- description: Realm timezone
  name: timezone
  type: string
- description: Realm type (Normal, RP, etc.)
  name: type
  type: object
- description: Whether this is a tournament realm
  name: is_tournament
  type: boolean
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-wo-w-realm-schema.json
slug: activision-blizzard-wo-w-realm
tags: []
title: WoWRealm
---

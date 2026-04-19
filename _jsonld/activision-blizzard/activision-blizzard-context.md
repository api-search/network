---
class_count: 17
classes:
- WoWItem
- HearthstoneDeck
- WoWCharacter
- D3HeroSummary
- WoWCharacterSummary
- WoWRealmsIndex
- BattleNetProfile
- WoWProfileSummary
- WoWAccount
- D3CareerProfile
- WoWGuild
- WoWCharacterAchievements
- WoWRealm
- HearthstoneCardsResponse
- SC2Profile
- D3Hero
- HearthstoneCard
context_file: json-ld/activision-blizzard-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/activision-blizzard/refs/heads/main/json-ld/activision-blizzard-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Activision Blizzard from activision-blizzard.
layout: jsonld
name: Activision Blizzard Context
namespaces:
- prefix: blizzard
  uri: https://develop.battle.net/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: quality
  type: string
- container: ''
  name: level
  type: integer
- container: ''
  name: itemClass
  type: string
- container: ''
  name: itemSubclass
  type: string
- container: ''
  name: inventoryType
  type: string
- container: ''
  name: purchasePrice
  type: integer
- container: ''
  name: sellPrice
  type: integer
- container: ''
  name: deckCode
  type: string
- container: ''
  name: version
  type: integer
- container: ''
  name: format
  type: string
- container: ''
  name: hero
  type: string
- container: ''
  name: heroPower
  type: string
- container: ''
  name: class
  type: string
- container: set
  name: cards
  type: string
- container: ''
  name: cardCount
  type: integer
- container: ''
  name: gender
  type: string
- container: ''
  name: faction
  type: string
- container: ''
  name: race
  type: string
- container: ''
  name: characterClass
  type: string
- container: ''
  name: activeSpec
  type: string
- container: ''
  name: realm
  type: string
- container: ''
  name: guild
  type: string
- container: ''
  name: experience
  type: integer
- container: ''
  name: achievementPoints
  type: integer
- container: ''
  name: lastLoginTimestamp
  type: integer
- container: ''
  name: hardcore
  type: boolean
- container: ''
  name: seasonal
  type: boolean
- container: ''
  name: dead
  type: boolean
- container: ''
  name: character
  type: string
- container: ''
  name: protectedCharacter
  type: string
- container: ''
  name: playableClass
  type: string
- container: ''
  name: playableRace
  type: string
- container: set
  name: realms
  type: string
- container: ''
  name: battletag
  type: string
- container: ''
  name: sub
  type: string
- container: set
  name: wowAccounts
  type: string
- container: set
  name: characters
  type: string
- container: ''
  name: paragonLevel
  type: integer
- container: ''
  name: paragonLevelHardcore
  type: integer
- container: ''
  name: guildName
  type: string
- container: set
  name: heroes
  type: string
- container: ''
  name: lastHeroPlayed
  type: integer
- container: ''
  name: kills
  type: string
- container: ''
  name: timePlayed
  type: string
- container: ''
  name: memberCount
  type: integer
- container: ''
  name: totalQuantity
  type: integer
- container: ''
  name: totalPoints
  type: integer
- container: set
  name: achievements
  type: string
- container: ''
  name: slug
  type: string
- container: ''
  name: region
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: locale
  type: string
- container: ''
  name: timezone
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: isTournament
  type: boolean
- container: ''
  name: pageCount
  type: integer
- container: ''
  name: page
  type: integer
- container: ''
  name: summary
  type: string
- container: ''
  name: snapshot
  type: string
- container: ''
  name: skills
  type: string
- container: ''
  name: items
  type: string
- container: ''
  name: stats
  type: string
- container: ''
  name: collectible
  type: integer
- container: ''
  name: classId
  type: integer
- container: set
  name: multiClassIds
  type: integer
- container: ''
  name: cardTypeId
  type: integer
- container: ''
  name: cardSetId
  type: integer
- container: ''
  name: rarityId
  type: integer
- container: ''
  name: artistName
  type: string
- container: ''
  name: health
  type: integer
- container: ''
  name: attack
  type: integer
- container: ''
  name: manaCost
  type: integer
- container: ''
  name: text
  type: string
- container: ''
  name: image
  type: reference
- container: ''
  name: imageGold
  type: reference
- container: ''
  name: flavorText
  type: string
- container: ''
  name: cropImage
  type: reference
property_count: 79
provider_name: activision-blizzard
provider_slug: activision-blizzard
slug: activision-blizzard-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---

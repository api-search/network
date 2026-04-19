---
description: A Hearthstone deck
layout: schema
name: HearthstoneDeck
properties_list:
- description: The deck code
  name: deckCode
  type: string
- description: Deck format version
  name: version
  type: integer
- description: Deck format
  name: format
  type: object
- description: ''
  name: hero
  type: object
- description: ''
  name: heroPower
  type: object
- description: Deck class
  name: class
  type: object
- description: Cards in the deck
  name: cards
  type: array
- description: Number of cards in the deck
  name: cardCount
  type: integer
provider_name: activision-blizzard
provider_slug: activision-blizzard
schema_file: json-schema/activision-blizzard-hearthstone-deck-schema.json
slug: activision-blizzard-hearthstone-deck
tags: []
title: HearthstoneDeck
---

---
consumed_apis:
- amazon-gamelift
description: Unified workflow capability for game developers and operations teams managing Amazon GameLift resources. Combines fleet management, game session lifecycle, player matchmaking, and scaling operations into a single workflow-oriented interface for multiplayer game infrastructure.
layout: capability
name: Amazon GameLift Game Operations
operations:
- description: List all game server fleets
  method: GET
  name: list-fleets
  path: /v1/fleets
- description: Create a new game server fleet
  method: POST
  name: create-fleet
  path: /v1/fleets
- description: Get fleet attributes
  method: GET
  name: describe-fleet
  path: /v1/fleets/{fleetId}
- description: Delete a fleet
  method: DELETE
  name: delete-fleet
  path: /v1/fleets/{fleetId}
- description: Start a new game session
  method: POST
  name: create-game-session
  path: /v1/game-sessions
- description: Search for active game sessions
  method: GET
  name: search-game-sessions
  path: /v1/game-sessions
- description: Request optimal game session placement
  method: POST
  name: start-placement
  path: /v1/game-sessions/placement
- description: Reserve a player slot in a game session
  method: POST
  name: create-player-session
  path: /v1/player-sessions
- description: Submit a matchmaking request
  method: POST
  name: start-matchmaking
  path: /v1/matchmaking
- description: Get matchmaking ticket status
  method: GET
  name: describe-matchmaking
  path: /v1/matchmaking
- description: Create or update a fleet scaling policy
  method: PUT
  name: put-scaling-policy
  path: /v1/scaling-policies
- description: List all game server builds
  method: GET
  name: list-builds
  path: /v1/builds
- description: Create a new game server build
  method: POST
  name: create-build
  path: /v1/builds
- description: List all fleet aliases
  method: GET
  name: list-aliases
  path: /v1/aliases
- description: Create a fleet alias
  method: POST
  name: create-alias
  path: /v1/aliases
personas: []
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
search_terms:
- reserve a player slot in a game session
- submit a matchmaking request
- create fleet
- create a new game server fleet
- cloud computing
- game session and player session lifecycle
- manage game server fleets
- create a new game server build resource
- get or update a specific fleet
- view logged events for a fleet during a specified time period
- fleet aliases for traffic routing
- list all fleet aliases defined in the region
- DevOps Engineer
- describe fleet utilization
- aws
- list fleets
- create game session
- Game Developer
- delete a fleet
- player matchmaking operations
- get active server process, game session, and player statistics for a fleet
- describe fleet events
- creating, configuring, and scaling game server fleets
- create or update a fleet auto-scaling policy
- get current auto-scaling policies for a fleet
- list all game server fleets
- reserve a player slot in an existing game session
- search for active game sessions with available player slots
- request optimal placement for a new game session across available fleets
- search for active game sessions
- list all amazon gamelift game server fleets with their status and configuration
- manages fleet infrastructure, scaling, and deployment pipelines
- start game session placement
- describe matchmaking
- put scaling policy
- unified workflow for game infrastructure management
- describe scaling policies
- get the status of a matchmaking request
- get detailed attributes and configuration of a game server fleet
- get fleet attributes
- place game sessions using queue optimization
- describe game sessions
- develops and tests multiplayer game server integration with gamelift
- game server build and script management
- request optimal game session placement
- manually adjust fleet capacity settings
- multiplayer
- create a new game server build
- create a new game server fleet with specified configuration
- search game sessions
- matchmaking
- update fleet capacity
- delete fleet
- create build
- create a fleet alias
- monitors live game sessions, manages player capacity, and handles incidents
- amazon gamelift
- create a fleet alias for traffic routing and fleet transitions
- game server builds
- create player session
- player matchmaking and flexmatch configuration
- flexmatch
- list all fleet aliases
- describe fleet attributes
- game servers
- manage game sessions
- start a new game session
- start placement
- list all game server builds
- get metadata on specific game sessions
- describe fleet
- create alias
- get current capacity settings and utilization for a fleet
- fleetiq
- start matchmaking
- list all game server builds uploaded to gamelift
- Game Operations Team
- fleet auto-scaling policies
- list builds
- gaming
- create or update a fleet scaling policy
- submit a matchmaking request to find other players and start a game
- get matchmaking ticket status
- start a new game session on a specific fleet
- cost-optimized spot instance game hosting
- list aliases
- manage player slots in game sessions
- describe fleet capacity
slug: amazon-gamelift-game-operations
tags:
- Amazon GameLift
- Gaming
- Game Servers
- Multiplayer
- Matchmaking
- AWS
tools:
- description: List all Amazon GameLift game server fleets with their status and configuration
  hints:
    openWorld: true
    readOnly: true
  name: list-fleets
- description: Create a new game server fleet with specified configuration
  hints:
    readOnly: false
  name: create-fleet
- description: Get detailed attributes and configuration of a game server fleet
  hints:
    idempotent: true
    readOnly: true
  name: describe-fleet-attributes
- description: Get current capacity settings and utilization for a fleet
  hints:
    readOnly: true
  name: describe-fleet-capacity
- description: Manually adjust fleet capacity settings
  hints:
    idempotent: true
    readOnly: false
  name: update-fleet-capacity
- description: Start a new game session on a specific fleet
  hints:
    readOnly: false
  name: create-game-session
- description: Search for active game sessions with available player slots
  hints:
    readOnly: true
  name: search-game-sessions
- description: Get metadata on specific game sessions
  hints:
    readOnly: true
  name: describe-game-sessions
- description: Request optimal placement for a new game session across available fleets
  hints:
    readOnly: false
  name: start-game-session-placement
- description: Reserve a player slot in an existing game session
  hints:
    readOnly: false
  name: create-player-session
- description: Submit a matchmaking request to find other players and start a game
  hints:
    readOnly: false
  name: start-matchmaking
- description: Get the status of a matchmaking request
  hints:
    readOnly: true
  name: describe-matchmaking
- description: Create or update a fleet auto-scaling policy
  hints:
    idempotent: true
    readOnly: false
  name: put-scaling-policy
- description: Get current auto-scaling policies for a fleet
  hints:
    readOnly: true
  name: describe-scaling-policies
- description: List all game server builds uploaded to GameLift
  hints:
    readOnly: true
  name: list-builds
- description: Create a new game server build resource
  hints:
    readOnly: false
  name: create-build
- description: List all fleet aliases defined in the region
  hints:
    readOnly: true
  name: list-aliases
- description: Create a fleet alias for traffic routing and fleet transitions
  hints:
    readOnly: false
  name: create-alias
- description: Get active server process, game session, and player statistics for a fleet
  hints:
    readOnly: true
  name: describe-fleet-utilization
- description: View logged events for a fleet during a specified time period
  hints:
    readOnly: true
  name: describe-fleet-events
---

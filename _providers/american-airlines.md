---
api_count: 1
apis:
- description: Runway is American Airlines' developer experience platform providing APIs for flight operations, booking, scheduling, and travel services. Built on Spotify's Backstage platform, Runway serves as the c
  name: American Airlines Runway Developer API
  slug: runway-developer-api
capabilities:
- description: Unified workflow for travel applications and agents accessing American Airlines flight data, status, and booking capabilities. Serves travel technology teams and booking platform developers.
  name: American Airlines Flight Operations
  slug: flight-operations
common:
- title: ''
  type: Website
  url: https://www.aa.com/
- title: ''
  type: DeveloperPortal
  url: https://developer.aa.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/AmericanAirlines
- title: ''
  type: Blog
  url: https://tech.aa.com/
- title: ''
  type: GitHubRepository
  url: https://github.com/AmericanAirlines/backstage
- title: Flight Engine Mock API
  type: Tools
  url: https://github.com/AmericanAirlines/Flight-Engine
- title: Hangar Hackathon Tool
  type: Tools
  url: https://github.com/AmericanAirlines/Hangar
created: '2026-04-19'
description: American Airlines is one of the world's largest airlines, operating an extensive domestic and international route network. The company's Runway developer experience platform, built on Spotify's Backstage, provides internal developer tooling and API management for engineering teams. American Airlines exposes flight data, status, and booking capabilities through its developer portal, and maintains an active open-source presence via the AmericanAirlines GitHub organization.
features:
- description: Internal developer platform built on Spotify's Backstage providing centralized API management, service catalog, and self-service infrastructure tooling for engineering teams.
  name: Runway Developer Experience Platform
- description: APIs for querying flight schedules, routes, status information, and operational data across American Airlines' domestic and international network.
  name: Flight Data APIs
- description: APIs supporting flight search, booking, reservation management, and passenger services integration for travel applications.
  name: Booking and Reservation APIs
- description: Runway provides integrated API management with security, authentication toggles, and corporate authentication capabilities for development teams.
  name: Built-In API Management
- description: Kong-based service mesh enabling reliable microservices communication and traffic management across the American Airlines platform.
  name: Service Mesh Integration
- description: American Airlines maintains open-source tools including Flight Engine (mock flight data API), Hangar (hackathon management), and Backstage plugins via the AmericanAirlines GitHub organization.
  name: Open Source Tooling
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Runway developer portal is built on Spotify's Backstage platform for internal developer experience and service catalog management.
  name: Spotify Backstage
- description: American Airlines uses Kong's Kuma service mesh for microservices networking and API gateway capabilities.
  name: Kong Service Mesh
- description: Integration with HashiCorp Vault for secrets management in build pipelines via open-source vault-action GitHub Action.
  name: HashiCorp Vault
- description: Python API client for Dynatrace integration maintained in the AmericanAirlines GitHub organization.
  name: Dynatrace
jsonld:
- class_count: 5
  name: American Airlines Runway Context
  property_count: 12
  slug: american-airlines-runway-context
layout: provider
modified: '2026-04-19'
name: American Airlines
rules:
- name: American Airlines API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: american-airlines-spectral-rules
skills: []
slug: american-airlines
solutions: []
tags:
- Airlines
- Aviation
- Flights
- Travel
- Booking
- Developer Experience
url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/apis.yml
use_cases:
- description: Travel agencies and booking platforms integrate flight availability, pricing, and reservation APIs to offer American Airlines flights.
  name: Flight Search and Booking
- description: Applications query real-time flight status, departure, arrival, and delay information for American Airlines flights.
  name: Flight Status Tracking
- description: American Airlines engineering teams use Runway to self-service infrastructure, register APIs in the service catalog, and manage deployments.
  name: Internal Developer Tooling
- description: Open-source Hangar tool enables hackathon management for tech innovation events sponsored by or affiliated with American Airlines.
  name: Hackathon and Innovation
---

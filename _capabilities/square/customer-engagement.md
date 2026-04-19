---
consumed_apis:
- square
description: Unified workflow for customer relationship management combining customers, loyalty programs, gift cards, bookings, team management, and location management. Used by business owners and customer success teams to build relationships and manage operations.
layout: capability
name: Square Customer Engagement
operations:
- description: List customer profiles.
  method: GET
  name: list-customers
  path: /v1/customers
- description: Create a new customer.
  method: POST
  name: create-customer
  path: /v1/customers
- description: Get customer details.
  method: GET
  name: get-customer
  path: /v1/customers/{customer_id}
- description: Update a customer.
  method: PUT
  name: update-customer
  path: /v1/customers/{customer_id}
- description: Delete a customer.
  method: DELETE
  name: delete-customer
  path: /v1/customers/{customer_id}
- description: Get the loyalty program.
  method: GET
  name: get-loyalty-program
  path: /v1/loyalty
- description: List gift cards.
  method: GET
  name: list-gift-cards
  path: /v1/gift-cards
- description: Create a gift card.
  method: POST
  name: create-gift-card
  path: /v1/gift-cards
- description: List bookings.
  method: GET
  name: list-bookings
  path: /v1/bookings
- description: Create a booking.
  method: POST
  name: create-booking
  path: /v1/bookings
- description: Get booking details.
  method: GET
  name: get-booking
  path: /v1/bookings/{booking_id}
- description: Search team members.
  method: POST
  name: search-team-members
  path: /v1/team-members
- description: List business locations.
  method: GET
  name: list-locations
  path: /v1/locations
- description: Get merchant details.
  method: GET
  name: list-merchants
  path: /v1/merchants
personas: []
provider_name: Square
provider_slug: square
search_terms:
- update customer
- create a new customer profile.
- delete a customer profile.
- list customers
- get team member
- merchant information.
- inventory
- list all gift cards.
- gift cards
- team management
- list bookings.
- webhooks
- invoicing
- manage loyalty programs.
- retrieve a gift card.
- point of sale
- disputes
- merchants
- retrieve a booking.
- create team member
- update team member
- search loyalty accounts.
- search team members.
- list bookings
- subscriptions
- cancel a booking.
- terminal
- refunds
- manage locations.
- get merchant details.
- catalog
- update a booking.
- manage bookings.
- search customer profiles.
- get loyalty program
- search team members
- retail
- update a team member.
- manage team members.
- accumulate loyalty points
- search loyalty accounts
- get a team member.
- get location
- get location details.
- list locations
- manage a specific booking.
- create a new customer.
- create a location.
- checkout
- loyalty
- get customer details.
- get customer
- create loyalty reward
- get gift card
- redeem loyalty reward
- manage a specific customer.
- create a booking.
- financial technology
- manage gift cards.
- orders
- list merchants
- payments
- create a team member.
- customers
- retrieve the loyalty program.
- add points to a loyalty account.
- square
- create gift card
- bookings
- list customer profiles.
- create booking
- update a customer.
- cancel booking
- create a loyalty account.
- get booking
- create loyalty account
- list business locations.
- get details for a specific customer.
- team
- search customers
- create a loyalty reward.
- ecommerce
- create a gift card.
- create location
- list gift cards.
- create a digital gift card.
- delete a customer.
- get the loyalty program.
- delete customer
- update booking
- locations
- list gift cards
- labor
- manage customers.
- search for booking availability.
- search availability
- create customer
- redeem a loyalty reward.
- update a customer profile.
- get booking details.
slug: customer-engagement
tags:
- Square
- Customers
- Loyalty
- Gift Cards
- Bookings
- Team Management
tools:
- description: List customer profiles.
  hints:
    openWorld: true
    readOnly: true
  name: list-customers
- description: Create a new customer profile.
  hints:
    idempotent: false
    readOnly: false
  name: create-customer
- description: Search customer profiles.
  hints:
    openWorld: true
    readOnly: true
  name: search-customers
- description: Get details for a specific customer.
  hints:
    openWorld: true
    readOnly: true
  name: get-customer
- description: Update a customer profile.
  hints:
    idempotent: true
    readOnly: false
  name: update-customer
- description: Delete a customer profile.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-customer
- description: Retrieve the loyalty program.
  hints:
    openWorld: true
    readOnly: true
  name: get-loyalty-program
- description: Search loyalty accounts.
  hints:
    openWorld: true
    readOnly: true
  name: search-loyalty-accounts
- description: Create a loyalty account.
  hints:
    idempotent: false
    readOnly: false
  name: create-loyalty-account
- description: Add points to a loyalty account.
  hints:
    idempotent: false
    readOnly: false
  name: accumulate-loyalty-points
- description: Create a loyalty reward.
  hints:
    idempotent: false
    readOnly: false
  name: create-loyalty-reward
- description: Redeem a loyalty reward.
  hints:
    idempotent: false
    readOnly: false
  name: redeem-loyalty-reward
- description: List all gift cards.
  hints:
    openWorld: true
    readOnly: true
  name: list-gift-cards
- description: Create a digital gift card.
  hints:
    idempotent: false
    readOnly: false
  name: create-gift-card
- description: Retrieve a gift card.
  hints:
    openWorld: true
    readOnly: true
  name: get-gift-card
- description: List bookings.
  hints:
    openWorld: true
    readOnly: true
  name: list-bookings
- description: Create a booking.
  hints:
    idempotent: false
    readOnly: false
  name: create-booking
- description: Retrieve a booking.
  hints:
    openWorld: true
    readOnly: true
  name: get-booking
- description: Update a booking.
  hints:
    idempotent: true
    readOnly: false
  name: update-booking
- description: Cancel a booking.
  hints:
    destructive: true
    readOnly: false
  name: cancel-booking
- description: Search for booking availability.
  hints:
    openWorld: true
    readOnly: true
  name: search-availability
- description: Search team members.
  hints:
    openWorld: true
    readOnly: true
  name: search-team-members
- description: Create a team member.
  hints:
    idempotent: false
    readOnly: false
  name: create-team-member
- description: Get a team member.
  hints:
    openWorld: true
    readOnly: true
  name: get-team-member
- description: Update a team member.
  hints:
    idempotent: true
    readOnly: false
  name: update-team-member
- description: List business locations.
  hints:
    openWorld: true
    readOnly: true
  name: list-locations
- description: Create a location.
  hints:
    idempotent: false
    readOnly: false
  name: create-location
- description: Get location details.
  hints:
    openWorld: true
    readOnly: true
  name: get-location
- description: Get merchant details.
  hints:
    openWorld: true
    readOnly: true
  name: list-merchants
---

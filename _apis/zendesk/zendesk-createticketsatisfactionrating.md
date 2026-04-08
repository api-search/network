---
aid: zendesk:zendesk-createticketsatisfactionrating
name: Zendesk Post  Api V2 Tickets Ticket_id Satisfaction_rating
tags:
- Satisfaction Ratings
humanURL: 
properties: []
description: >-
  Creates a CSAT rating for a solved ticket, or for a ticket that was previously solved and then reopened.  Only the end user listed as the ticket requester can create a satisfaction rating for the ticket.  Only "good" and "bad" are valid values for the score when creating a rating. Other states, like "offered", are not valid and will result in a 422 error.  #### Allowed For  * End user who requested the ticket  The end user must be a verified user.

---

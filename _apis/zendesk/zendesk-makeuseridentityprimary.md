---
aid: zendesk:zendesk-makeuseridentityprimary
name: Zendesk Put  Api V2 Users User_id Identities User_identity_id Make_primary
tags:
- User Identities
humanURL: 
properties: []
description: >-
  Sets the specified identity as primary. To change other attributes, use the [Update  Identity](#update-identity) endpoint. This is a collection-level operation and the correct behavior for an API client is to subsequently reload the entire collection.  The first endpoint is the preferred option if authenticating as an agent. If authenticating as an end user, you can only use the second endpoint. In addition, an end user can only make an email identity primary if the email is verified.  #### A...

---

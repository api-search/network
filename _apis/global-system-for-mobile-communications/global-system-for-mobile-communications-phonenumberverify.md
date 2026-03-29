---
aid: global-system-for-mobile-communications:global-system-for-mobile-communications-phonenumberverify
name: Verifies if the received hashed/plain text phone number matches the phone number associated with the access token
tags:
- Phone number verify
humanURL: 
properties: []
description: >-
  Verifies if the specified phone number (either in plain text or hashed format) matches the one that the user is currently using. Only one of the plain or hashed formats must be provided. - The number verification will be done for the user that has authenticated via mobile network - It returns true/false depending on if the hashed phone number received as input matches the authenticated user's `device phone number` associated to the access token

---

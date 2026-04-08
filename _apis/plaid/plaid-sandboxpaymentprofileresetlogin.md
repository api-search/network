---
aid: plaid:plaid-sandboxpaymentprofileresetlogin
name: Plaid Reset the login of a Payment Profile
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/sandbox/payment_profile/reset_login/` forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.   After calling `/sandbox/payment_profile/reset_login`, calls to the `/transfer/authorization/create` with the Payment Profile will result in a `decision_rationale` `PAYMENT_PROFILE_LOGIN_REQUIRED`. You can then use update mode for Payment Profile to restore it into a good state.   In order to i...

---

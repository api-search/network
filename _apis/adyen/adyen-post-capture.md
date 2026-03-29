---
aid: adyen:adyen-post-capture
name: Capture an authorisation
tags:
- - - - Modifications
humanURL: 
properties: []
description: >-
  Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full authorisation amount is captured, however it's also possible to capture a smaller amount, which results in cancelling the remaining authorisation balance.  Payment methods that are captured automatically after authorisation don't need to be captured. However, submitting a capture request on these transactions will not result in double charges. If immediate or delayed auto-capture is e...

---

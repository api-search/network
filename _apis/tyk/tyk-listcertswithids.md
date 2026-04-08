---
aid: tyk:tyk-listcertswithids
name: Return one certificate or list multiple certificates in the Tyk Gateway given a comma separated list of cert IDs.
tags:
- CertsTag
humanURL: 
properties: []
description: >-
  Note that the certID path parameter can take a list of certIDs separated with commas (e.g /tyk/certs/certIDOne,certIDTwo).  If you send a single certID it will return a single CertificateMeta object otherwise if you send more than two certIDs is will return an array of certificateMeta objects.

---

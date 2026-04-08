---
aid: microsoft-graph:microsoft-graph-serviceprincipalsserviceprincipaladdtokensigningcertificate
name: Microsoft Graph Invoke action addTokenSigningCertificate
tags:
- servicePrincipals.servicePrincipal.Actions
humanURL: 
properties: []
description: >-
  Create a self-signed signing certificate and return a selfSignedCertificate object, which is the public part of the generated certificate.  The self-signed signing certificate is composed of the following objects, which are added to the servicePrincipal:  + The keyCredentials object with the following objects:     + A private key object with usage set to Sign.     + A public key object with usage set to Verify. + The passwordCredentials object.  All the objects have the same value of cust...

---

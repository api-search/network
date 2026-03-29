---
aid: amazon-web-services:amazon-web-services-amazonwebservicesrejectcertificatetransfer
name: Rejectcertificatetransfer
tags:
- API
humanURL: 
properties: []
description: >-
  Rejects a pending certificate transfer. After IoT rejects a certificate transfer, the certificate status changes from PENDING_TRANSFER to INACTIVE. To check for pending certificate transfers, call ListCertificates to enumerate your certificates. This operation can only be called by the transfer destination. After it is called, the certificate will be returned to the source's account in the INACTIVE state. Requires permission to access the RejectCertificateTransfer action.

---

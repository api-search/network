---
aid: microsoft-graph:microsoft-graph-domain-dns-records
name: Microsoft Graph Domain DNS Records
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/domaindnsrecords-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph domain DNS records are the programmatic way to discover and
  manage the DNS settings Microsoft 365 expects for a custom domain. When you
  add a domain, Graph exposes two main sets of records: verificationDnsRecords
  (typically TXT or MX) used to prove ownership, and serviceConfigurationRecords
  (MX, CNAME, TXT, SRV) used to configure services like Exchange Online (mail
  flow and Autodiscover), Teams/Skype, and device management. Each record is
  typed (for example DomainDnsTxtRecord, DomainDnsCnameRecord,
  DomainDnsMxRecord, DomainDnsSrvRecord) and includes details such as host name,
  target, and TTL. Apps can read these records to guide admins, automate
  onboarding, monitor when verification can succeed, and then invoke the domain
  verify action. Graph itself doesnt change your DNS; you publish the returned
  records at your DNS host, and Graph reflects their status for Microsoft 365
  setup and health checks.

---
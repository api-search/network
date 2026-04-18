---
channels:
- description: 'Channel for forwarded traffic logs. Traffic logs record the start and end of every network session passing through the firewall, including source and destination addresses, ports, protocols, applications identified by App-ID, actions taken, and session byte and packet counters. Traffic logs provide comprehensive network visibility and session tracking for security analytics and compliance reporting. Supported formats: CSV, LEEF, CEF, JSON, PARQUET.'
  name: log/traffic
  operation: subscribe
  operation_id: onTrafficLog
  summary: Forwarded traffic log entry
- description: 'Channel for forwarded threat logs. Threat logs record security events detected by the firewall''s threat prevention engines including antivirus, anti-spyware, vulnerability protection, DNS security, and custom threat signatures. Each entry identifies the threat, its severity, the action taken, attack direction, and session context. Supported formats: CSV, LEEF, CEF, JSON, PARQUET.'
  name: log/threat
  operation: subscribe
  operation_id: onThreatLog
  summary: Forwarded threat detection log entry
- description: 'Channel for forwarded URL filtering logs. URL filtering logs record web access events evaluated by the URL Filtering security profile. Each entry includes the requested URL, URL category, action taken, HTTP method, content type, and user identity when User-ID is enabled. Supported formats: CSV, LEEF, CEF, JSON, PARQUET.'
  name: log/url
  operation: subscribe
  operation_id: onUrlLog
  summary: Forwarded URL filtering log entry
- description: 'Channel for forwarded WildFire submission logs. WildFire logs record file analysis results from the WildFire cloud-based sandbox analysis service. Each entry includes the file name, type, SHA-256 hash, final verdict (benign, malware, grayware, phishing), and a link to the analysis report. Supported formats: CSV, LEEF, CEF, JSON, PARQUET.'
  name: log/wildfire
  operation: subscribe
  operation_id: onWildfireLog
  summary: Forwarded WildFire file analysis log entry
- description: 'Channel for forwarded authentication logs. Authentication logs record user authentication events processed by the firewall''s Authentication Policy, including SAML assertions, Kerberos ticket validations, LDAP binds, RADIUS authentications, and MFA challenges. Each entry captures the authentication method, result, user identity, and policy context. Supported formats: CSV, LEEF, CEF, JSON, PARQUET.'
  name: log/auth
  operation: subscribe
  operation_id: onAuthLog
  summary: Forwarded authentication event log entry
description: Strata Logging Service Log Forwarding enables security operations teams to forward security logs from Palo Alto Networks next-generation firewalls, Prisma Access, and other Strata products to external SIEM systems, data lakes, and log management platforms. Log forwarding profiles define which log types are forwarded, in which output format, and to which destination. Supported transport protocols include Syslog over TCP, UDP, and TLS, HTTPS REST endpoints, and Email. Supported output formats include CSV, LEEF (Log Event Extended Format), CEF (Common Event Format), JSON, and PARQUET. Log types available for forwarding include traffic, threat, URL filtering, data, WildFire malware analysis, authentication, decryption, and GlobalProtect logs. Each log type delivers structured security event data enabling comprehensive network visibility, compliance reporting, and security analytics in downstream platforms.
layout: asyncapi
messages:
- description: ''
  name: TrafficLog
  summary: A forwarded traffic log entry representing a network session that passed through or was blocked by the firewall
  title: Traffic Log Entry
- description: ''
  name: ThreatLog
  summary: A forwarded threat detection log entry for a security event caught by the firewall's threat prevention profiles
  title: Threat Log Entry
- description: ''
  name: UrlLog
  summary: A forwarded URL filtering log entry for a web access event evaluated by the URL Filtering security profile
  title: URL Filtering Log Entry
- description: ''
  name: WildfireLog
  summary: A forwarded WildFire file analysis log entry with the malware verdict returned by the WildFire cloud sandbox service
  title: WildFire Log Entry
- description: ''
  name: AuthLog
  summary: A forwarded authentication event log entry for a user authentication processed by the firewall's Authentication Policy
  title: Authentication Log Entry
name: Strata Logging Service Log Forwarding
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
servers:
- description: Syslog destination for log forwarding over TCP. Configure the syslog server address and port in Strata Logging Service Settings > Log Forwarding. Supports CEF, LEEF, and CSV output formats. Non-encrypted TCP syslog uses port 514 by default.
  name: syslog-tcp
  protocol: tcp
  url: '{syslogHost}:{syslogPort}'
- description: Syslog destination for log forwarding over TLS-encrypted TCP. TLS encryption is recommended for production deployments and requires uploading the syslog server's CA certificate for mutual authentication. Supports CEF, LEEF, and CSV output formats over TLS transport.
  name: syslog-tls
  protocol: tcp
  url: '{syslogHost}:{syslogTlsPort}'
- description: Syslog destination for log forwarding over UDP. UDP syslog provides lower overhead but without guaranteed delivery. Suitable for high-volume log forwarding in environments where occasional loss is acceptable.
  name: syslog-udp
  protocol: udp
  url: '{syslogHost}:{syslogUdpPort}'
- description: HTTPS destination for log forwarding via HTTP POST requests. Configure the HTTPS endpoint URL in Strata Logging Service Settings > Log Forwarding. The endpoint must accept POST requests and return a 2xx response. Supports JSON, CEF, LEEF, and PARQUET output formats. Authentication is configured via custom HTTP headers or OAuth2 client credentials.
  name: https-endpoint
  protocol: https
  url: '{httpsUrl}'
slug: palo-alto-strata-logging-forwarding-asyncapi-original
spec_file: asyncapi/palo-alto-strata-logging-forwarding-asyncapi-original.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/asyncapi/palo-alto-strata-logging-forwarding-asyncapi-original.yml
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---

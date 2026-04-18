---
description: Schema for a forwarded PAN-OS URL filtering log entry. URL logs capture web access events evaluated by the URL Filtering security profile, providing visibility into browsing activity, policy enforcement, and URL category decisions.
layout: schema
name: UrlLogPayload
properties_list:
- description: Timestamp when the URL log entry was received by Strata Logging Service.
  name: receive_time
  type: string
- description: Serial number of the Palo Alto Networks device that generated this URL log entry.
  name: serial
  type: string
- description: Log type identifier, always URL for URL filtering log entries.
  name: type
  type: string
- description: Source IP address of the client making the web request.
  name: src
  type: string
- description: Destination IP address of the web server being accessed.
  name: dst
  type: string
- description: Source port number of the HTTP/HTTPS session.
  name: sport
  type: integer
- description: Destination port number of the HTTP/HTTPS session.
  name: dport
  type: integer
- description: Application identified by App-ID for the web session (e.g., web-browsing, ssl, google-base).
  name: app
  type: string
- description: The full URL that was requested, including protocol, hostname, path, and query parameters if present.
  name: url
  type: string
- description: URL category classification assigned by PAN-DB URL filtering database (e.g., business-and-economy, malware, social-networking, command-and-control).
  name: url_category
  type: string
- description: Action applied to the URL request by the URL Filtering security profile configured on the matching security policy rule.
  name: action
  type: string
- description: HTTP method of the web request.
  name: http_method
  type: string
- description: MIME content type of the HTTP response.
  name: content_type
  type: string
- description: Source user identity associated with the web request if User-ID is enabled.
  name: src_user
  type: string
- description: Name of the security policy rule that matched the session containing this URL request.
  name: rule_name
  type: string
- description: Hostname of the firewall that generated this URL log entry.
  name: device_name
  type: string
- description: Virtual system name or identifier on the firewall.
  name: vsys
  type: string
- description: Name of the log forwarding profile that forwarded this log entry.
  name: log_forwarding_profile
  type: string
- description: Output format in which this log entry was forwarded.
  name: output_format
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-forwarding-url-log-payload-schema.json
slug: strata-logging-forwarding-url-log-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: UrlLogPayload
---

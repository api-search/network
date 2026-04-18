---
description: Schema for a forwarded PAN-OS WildFire submission log entry. WildFire logs record the results of file analysis by the WildFire cloud-based sandbox malware analysis service, providing verdicts and analysis report links for detected threats.
layout: schema
name: WildfireLogPayload
properties_list:
- description: Timestamp when the WildFire log entry was received by Strata Logging Service.
  name: receive_time
  type: string
- description: Serial number of the Palo Alto Networks device that submitted the file to WildFire and generated this log entry.
  name: serial
  type: string
- description: Log type identifier, always WILDFIRE for WildFire log entries.
  name: type
  type: string
- description: Source IP address of the session from which the file was captured.
  name: src
  type: string
- description: Destination IP address of the session from which the file was captured.
  name: dst
  type: string
- description: Application identified by App-ID in the session from which the file was captured.
  name: app
  type: string
- description: Name of the file that was submitted to WildFire for analysis.
  name: filename
  type: string
- description: File type of the submitted file (e.g., PE, PDF, APK, Adobe Flash, Microsoft Office, script, Java Applet).
  name: filetype
  type: string
- description: SHA-256 cryptographic hash of the submitted file, used as the unique file identifier in the WildFire cloud database.
  name: file_hash
  type: string
- description: Size of the submitted file in bytes.
  name: file_size
  type: integer
- description: WildFire analysis verdict for the submitted file indicating whether it is benign, malicious malware, potentially unwanted grayware, a phishing document, or pending analysis completion.
  name: verdict
  type: string
- description: Action applied to the file by the WildFire security profile based on the analysis verdict.
  name: action
  type: string
- description: URL to the full WildFire analysis report in the Palo Alto Networks WildFire portal, providing detailed behavioral analysis results.
  name: report_url
  type: string
- description: Source user identity if User-ID is enabled.
  name: src_user
  type: string
- description: Name of the security policy rule under which the file was captured and submitted to WildFire.
  name: rule_name
  type: string
- description: Hostname of the firewall that captured the file and generated this WildFire log entry.
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
schema_file: json-schema/strata-logging-forwarding-wildfire-log-payload-schema.json
slug: strata-logging-forwarding-wildfire-log-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: WildfireLogPayload
---

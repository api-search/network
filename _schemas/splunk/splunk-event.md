---
description: Schema for a Splunk event, the fundamental unit of data in Splunk. An event represents a single entry of machine data that has been indexed by Splunk, containing the raw event data along with metadata fields used for searching, filtering, and organizing data. Events are ingested through various data inputs including HTTP Event Collector (HEC), file monitors, TCP/UDP inputs, and scripted inputs.
layout: schema
name: Splunk Event
properties_list:
- description: The timestamp of the event. When submitting via HEC, this is epoch time in seconds. When retrieved from search results, the format depends on the output mode. If omitted during ingestion, Splunk assig
  name: time
  type: object
- description: The indexed timestamp of the event as stored in Splunk. This is the canonical time field used in search results and is always present on indexed events.
  name: _time
  type: string
- description: The original raw text of the event as it was received by Splunk. This contains the complete, unmodified event data before field extraction.
  name: _raw
  type: string
- description: 'The event payload when submitting via HTTP Event Collector. Can be a string for raw text events or a JSON object for structured events. This field is required when using the /services/collector/event '
  name: event
  type: object
- description: The hostname, IP address, or fully qualified domain name of the system that generated the event. This is a default metadata field that Splunk assigns during data ingestion.
  name: host
  type: string
- description: The source of the event data, typically a file path, network port, or data input name. Identifies where the data originated from on the host.
  name: source
  type: string
- description: The source type classifies the event data format and determines how Splunk parses and extracts fields. Splunk includes many built-in sourcetypes and custom ones can be defined.
  name: sourcetype
  type: string
- description: The name of the Splunk index where the event is stored. Indexes are the primary data repositories in Splunk.
  name: index
  type: string
- description: The time at which the event was indexed by Splunk, as opposed to when the event occurred. Stored as epoch time.
  name: _indextime
  type: string
- description: A sequence number assigned to the event within the search results. Used for ordering and pagination.
  name: _serial
  type: integer
- description: Internal Splunk field containing the bucket ID and offset for the event. Used for direct event access.
  name: _cd
  type: string
- description: The bucket ID where the event is stored within the index. Format is <index_name>~<bucket_id>~<guid>.
  name: _bkt
  type: string
- description: Server and index information as a two-element array containing the Splunk server name and the index name.
  name: _si
  type: array
- description: The number of lines in the raw event text
  name: linecount
  type: integer
- description: The name of the Splunk server that indexed this event. Relevant in distributed search environments.
  name: splunk_server
  type: string
- description: The server group of the Splunk server that indexed this event. Used in indexer clustering.
  name: splunk_server_group
  type: string
- description: The event type classification assigned by Splunk based on configured eventtype definitions.
  name: eventtype
  type: string
- description: Tags associated with the event based on field values and tag configurations.
  name: tag
  type: array
- description: Additional metadata fields to associate with the event during HEC ingestion. These are indexed as metadata and can be searched as indexed fields without being part of the raw event data.
  name: fields
  type: object
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-event-schema.json
slug: splunk-event
tags:
- Analytics
- Data Analysis
- Logging
- Machine Data
- Monitoring
- Observability
- Platform
- Security
- SIEM
title: Splunk Event
---

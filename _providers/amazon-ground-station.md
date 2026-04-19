---
api_count: 1
apis:
- description: The AWS Ground Station API provides programmatic access to manage satellite contacts, mission profiles, configs, ground stations, and dataflow endpoint groups for satellite communications and data pro
  name: AWS Ground Station API
  slug: aws-ground-station-api
capabilities:
- description: Workflow capability for satellite operators and mission control teams using Amazon Ground Station. Covers contact scheduling, mission profile management, satellite tracking, and dataflow configuration
  name: Amazon Ground Station Satellite Operations
  slug: amazon-ground-station-satellite-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/ground-station/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ground-station/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/publicsector/tag/aws-ground-station/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/groundstation/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-ground-station-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-ground-station-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-ground-station-satellite-operations.yaml
created: '2026-03-16'
description: AWS Ground Station is a fully managed service that lets you control satellite communications, process satellite data, and scale your satellite operations without having to worry about building or managing your own ground station infrastructure.
features:
- description: AWS manages a global network of antennas so you do not need to build or operate your own ground station infrastructure.
  name: Managed Ground Station Infrastructure
- description: Schedule satellite contacts through a simple API, selecting the satellite, time window, and ground station location.
  name: Satellite Contact Scheduling
- description: Access AWS ground station antennas deployed at strategic worldwide locations for maximum satellite coverage.
  name: Global Antenna Network
- description: Receive satellite data directly into AWS cloud services for processing, storage, and analysis.
  name: Data Downlink and Processing
- description: Configure mission profiles specifying dataflow endpoints, antenna frequencies, and processing parameters.
  name: Mission Profile Configuration
- description: Stream satellite data directly into Amazon S3, Kinesis, EC2, and other AWS services for processing.
  name: Integration with AWS Services
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Store downlinked satellite data directly in S3 for archival and processing.
  name: Amazon S3
- description: Stream real-time satellite data into Kinesis for immediate processing.
  name: Amazon Kinesis
- description: Process satellite data on EC2 compute instances co-located with ground station endpoints.
  name: Amazon EC2
- description: Trigger Lambda functions when satellite contact data arrives for automated processing.
  name: AWS Lambda
- description: Apply machine learning to satellite imagery and telemetry data.
  name: Amazon SageMaker
jsonld:
- class_count: 114
  name: Amazon Ground Station Context
  property_count: 155
  slug: amazon-ground-station-context
layout: provider
modified: '2026-04-19'
name: Amazon Ground Station
rules:
- name: Amazon Ground Station API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 2
  slug: amazon-ground-station-spectral-rules
skills: []
slug: amazon-ground-station
solutions: []
tags:
- AWS
- Data Processing
- IoT
- Satellite Communications
- Space Technology
url: https://raw.githubusercontent.com/api-evangelist/amazon-ground-station/refs/heads/main/apis.yml
use_cases:
- description: Collect and process satellite imagery for environmental monitoring, agriculture, and urban planning.
  name: Earth Observation
- description: Receive data from weather satellites for meteorological analysis and forecasting.
  name: Weather Forecasting
- description: Track ship positions and maritime assets using satellite AIS data.
  name: Maritime Tracking
- description: Use geostationary satellites for communications relay applications.
  name: Communications Relay
- description: Support space-based scientific missions with managed data collection and downlink.
  name: Scientific Research
---

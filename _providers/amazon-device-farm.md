---
api_count: 1
apis:
- description: 'The AWS Device Farm API enables programmatic access to create and manage test runs, device pools, projects, and jobs for testing mobile and web applications across real devices and browsers. Supports '
  name: AWS Device Farm API
  slug: ''
capabilities:
- description: Workflow capability for QA engineers and mobile developers to run automated tests on real physical devices and desktop browsers using AWS Device Farm. Combines project management, device pool configur
  name: AWS Device Farm Mobile and Browser Testing
  slug: mobile-browser-testing
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/device-farm/
- title: ''
  type: Website
  url: https://aws.amazon.com/device-farm/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/devicefarm/
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
  url: https://aws.amazon.com/blogs/mobile/category/mobile-services/aws-device-farm/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/devicefarm/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-device-farm-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-device-farm-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/mobile-browser-testing.yaml
created: '2026-03-16'
description: AWS Device Farm is an application testing service that lets you improve the quality of your web and mobile apps by testing them across an extensive range of desktop browsers and real mobile devices without having to provision and manage any testing infrastructure.
features:
- description: Test mobile apps on thousands of real physical Android and iOS devices without managing any device infrastructure.
  name: Real Device Testing
- description: Test web applications on desktop browsers using Selenium RemoteWebDriver through Device Farm's test grid.
  name: Desktop Browser Testing
- description: Supports popular test frameworks including Appium, XCTest, Espresso, Calabash, and built-in fuzz testing.
  name: Automated Test Frameworks
- description: Interactively access real devices via remote desktop to manually test and debug your app.
  name: Remote Access Sessions
- description: Simulate different network conditions including bandwidth, latency, and packet loss using network profiles.
  name: Network Condition Simulation
- description: Provision and manage private dedicated devices for exclusive use in testing your applications.
  name: Private Device Fleet
- description: Test apps hosted in private VPCs using VPC endpoint configurations without exposing them publicly.
  name: VPC Integration
- description: Run tests in parallel across multiple devices simultaneously to reduce overall testing time.
  name: Parallel Test Execution
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Integrate Device Farm tests as a stage in your CodePipeline CI/CD pipelines for automated testing.
  name: AWS CodePipeline
- description: Trigger Device Farm test runs from CodeBuild projects as part of build and deploy workflows.
  name: AWS CodeBuild
- description: Run Device Farm tests from Jenkins CI using the AWS Device Farm plugin for Jenkins.
  name: Jenkins
- description: Supports Appium test scripts for both Android and iOS cross-platform mobile testing.
  name: Appium
- description: Integrates with Selenium RemoteWebDriver for automated desktop browser testing.
  name: Selenium
- description: Trigger Device Farm test runs using the AWS Device Farm GitHub Action in your workflows.
  name: GitHub Actions
jsonld:
- class_count: 29
  name: Amazon Device Farm Context
  property_count: 115
  slug: amazon-device-farm-context
layout: provider
modified: '2026-04-19'
name: Amazon Device Farm
rules:
- name: Amazon Device Farm API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 4
    warn: 8
  slug: amazon-device-farm-spectral-rules
skills: []
slug: amazon-device-farm
solutions: []
tags:
- Application Testing
- AWS
- Device Testing
- Mobile Testing
- Quality Assurance
url: https://aws.amazon.com/device-farm/
use_cases:
- description: Validate mobile app functionality, performance, and compatibility across a wide range of real Android and iOS devices.
  name: Mobile App Quality Assurance
- description: Ensure your app behaves correctly on different device manufacturers, screen sizes, OS versions, and hardware configurations.
  name: Cross-Device Compatibility Testing
- description: Run Selenium-based browser tests against your web application across multiple desktop browser environments.
  name: Web Application Browser Testing
- description: Integrate device testing into your continuous integration and deployment pipelines for automated quality gates.
  name: CI/CD Test Integration
- description: Measure app performance metrics including CPU usage, memory consumption, and network activity across different devices.
  name: App Performance Benchmarking
---

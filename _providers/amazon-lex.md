---
api_count: 1
apis:
- description: The Amazon Lex API provides programmatic access to manage bots, bot aliases, bot channels, intents, slots, and slot types for building conversational AI interfaces and chatbots.
  name: Amazon Lex API
  slug: ''
capabilities:
- description: Unified workflow capability for Amazon Lex combining resource management and operations.
  name: Amazon Lex Workflow
  slug: amazon-lex-workflow
common:
- title: ''
  type: portal
  url: https://aws.amazon.com/
- title: ''
  type: website
  url: https://aws.amazon.com/lex/
- title: ''
  type: documentation
  url: https://docs.aws.amazon.com/lex/
- title: ''
  type: terms-of-service
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: privacy-policy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: blog
  url: https://aws.amazon.com/blogs/machine-learning/
- title: ''
  type: github
  url: https://github.com/aws
- title: ''
  type: console
  url: https://console.aws.amazon.com/lex/
- title: ''
  type: sign-up
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: login
  url: https://signin.aws.amazon.com/
- title: ''
  type: status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: knowledge-center
  url: https://repost.aws/knowledge-center
- title: ''
  type: youtube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: stack-overflow
  url: https://stackoverflow.com/questions/tagged/amazon-lex
- title: ''
  type: contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: security
  url: https://aws.amazon.com/security/
- title: ''
  type: compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-lex-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-lex-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-lex-vocabulary.yaml
created: '2024-01-15'
description: Amazon Lex is a fully managed artificial intelligence (AI) service with advanced natural language models to design, build, test, and deploy conversational interfaces in applications. It provides the deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, enabling you to build applications with highly engaging user experiences and lifelike conversational interactions.
features:
- description: Convert speech to text with high accuracy using the same deep learning technology as Amazon Alexa.
  name: Automatic Speech Recognition
- description: Understand the intent behind user input to build conversational interfaces.
  name: Natural Language Understanding
- description: Deploy bots across web, mobile, messaging channels (Slack, Facebook Messenger, Twilio), and contact centers.
  name: Multi-Channel Deployment
- description: Build intelligent contact center bots with native integration with Amazon Connect.
  name: Amazon Connect Integration
- description: Support multi-turn streaming conversations for complex dialog flows.
  name: Streaming Conversations
- description: Recognize user intents and extract slot values from natural language input.
  name: Intent Recognition
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Deploy Lex bots in Amazon Connect contact flows for IVR and agent assist.
  name: Amazon Connect
- description: Combine Lex for dialog management with Kendra for intelligent document search.
  name: Amazon Kendra
- description: Use Lambda for fulfillment logic and business rules in bot conversations.
  name: AWS Lambda
- description: Convert bot text responses to natural speech using Amazon Polly TTS.
  name: Amazon Polly
jsonld:
- class_count: 2
  name: Amazon Lex Context
  property_count: 7
  slug: amazon-lex-context
layout: provider
modified: '2026-04-19'
name: Amazon Lex
rules:
- name: Amazon Lex API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-lex-spectral-rules
skills: []
slug: amazon-lex
solutions: []
tags: []
url: https://apis.io/amazon-lex
use_cases:
- description: Build self-service chatbots for customer support and FAQ handling.
  name: Customer Service Chatbot
- description: Automate contact center interactions with intelligent IVR and agent assist.
  name: Contact Center Automation
- description: Create employee-facing bots for IT help desk and HR self-service.
  name: Internal Help Desk
- description: Build shopping assistants that understand natural language product queries.
  name: E-Commerce Assistant
---
